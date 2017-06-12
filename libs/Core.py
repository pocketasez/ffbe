import argparse
import sys
import os
import shutil
import logging
import time


class Executable(object):
    def __init__(self):
        Log.init()
        self.hex_str = "%x" % (int(time.time()),)
        self.file = File(sys.argv[0])
        self.file.path_str = self.get_abs_path_str()
        self.log_file = LogFile("%s.nfo" % self.hex_str, self.file.path_str)
        self.sys = Sys()

    def main(self):
        pass

    def get_abs_path_str(self):
        # Workoround for PyInstaller:
        # http://stackoverflow.com/questions/13946650/pyinstaller-2-0-bundle-file-as-onefile
        if hasattr(sys, "_MEIPASS"):
            return sys._MEIPASS
        else:
            return self.file.path_str

    def run(self):
        self.log_file.init()
        try:
            self.main()
        except Exception:
            Log.exception("Unhandled exception")
            self.log_file.base_str = "%s.%s" % (self.log_file.base_str, "unhandled")
            self.sys.exit_int = 1
        self.log_file.close()
        self.sys.close()


# Helper Classes


class Withable(object):
    """
    Implements "with" support. It allows the class to be called using
    a with statement. i.e with Withable as w:
    """

    def close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exit_type, value, trace):
        self.close()


class Sys(Withable):
    def __init__(self):
        self.exit_bln = True
        self.exit_int = 0

    def close(self):
        if self.exit_bln is True:
            Log.debug("Exiting with code %i", self.exit_int)
            sys.exit(self.exit_int)


class Dir(Withable):
    def __init__(self, *args):
        self.path_str = os.path.abspath(os.path.join(*args))

    def makedirs(self):
        try:
            os.makedirs(self.path_str)
        except Exception:  # Both unix and win
            pass

    def rename_remove_(self):
        path, head = os.path.split(self.path_str)
        if head.startswith('_'):
            path = os.path.join(path, head[1:])
            logging.debug("os> mv %s %s", self.path_str, path)
            os.rename(self.path_str, path)
            self.path_str = path

    def get_base_dir_str(self):
        return os.path.split(self.path_str)[1]

    def get_parent_str(self):
        return os.path.split(self.path_str)[0]

    def get_parent_dir(self):
        return Dir(os.path.split(self.path_str)[0])

    def __str__(self):
        return self.path_str


class DirException(Exception):
    pass


class File(Dir):
    def __init__(self, file_name_str, *args):
        path_str, self.name_str = os.path.split(file_name_str)
        try:
            super(File, self).__init__(*args)
            self.path_str = os.path.join(self.path_str, path_str)
        except TypeError:
            self.path_str, self.name_str = os.path.split(os.path.abspath(file_name_str))
        self.base_str, self.ext_str = os.path.splitext(self.name_str)

    def open_fh(self, mode_str):
        return open(self.get_abs_name_str(), mode_str)

    def exists_bln(self):
        return os.path.exists(self.get_abs_name_str())

    def write(self, text_str):
        with open(self.get_abs_name_str(), 'w') as fh:
            fh.write(text_str)

    def get_size_int(self):
        return os.path.getsize(self.get_abs_name_str())

    def get_abs_base_str(self):
        return os.path.join(self.path_str, self.base_str)

    def get_abs_name_str(self):
        if self.ext_str != '':
            return "%s%s" % (self.get_abs_base_str(), self.ext_str)
        else:
            return self.get_abs_base_str()

    def delete(self):
        os.unlink(self.get_abs_name_str())

    def __str__(self):
        return self.get_abs_name_str()


class LogFile(File):
    def __init__(self, file_name_str, *args):
        super(LogFile, self).__init__(file_name_str, *args)
        self.err_dir = Dir(self.path_str)
        self.save_dir = Dir(self.path_str)
        self.save_bln = False
        self.init_abs_name_str = None
        self.init_bln = False

    def init(self):
        if self.init_bln is False:
            self.init_abs_name_str = self.get_abs_name_str()
            #Log.add_file(self.init_abs_name_str)
            self.init_bln = True

    def get_save_dir_str(self):
        return os.path.join(self.save_dir.path_str, "%s.log" % self.base_str)

    def close(self):
        """
        - Saves .err file if any errors were encountered
        - Closes log file handles
        - Deletes the main log file
        :return:
        """
        try:
            self.save()
        except IOError:
            pass
        handlers = list(Log.logger.handlers)
        for handle in handlers:
            try:
                Log.logger.removeHandler(handle)
                handle.flush()
                handle.close()
            except IOError:
                pass
        try:
            self.delete()
        except Exception:
            pass

    def save(self):
        self.save_dir.makedirs()
        if self.save_bln is True:
            try:
                self._save(self.save_dir.path_str, "%s.log" % self.base_str)
            except Exception:
                self._save(self.path_str, "%s.log" % self.base_str)
        if Log.err_count_int > 0:
            self.err_dir.makedirs()
            try:
                self._save(self.err_dir.path_str, "%s.err" % self.base_str)
            except Exception:
                self._save(self.path_str, "%s.err" % self.base_str)

    def _save(self, *args):
        shutil.copy(
            self.init_abs_name_str,
            os.path.join(*args)
        )


class Log(object):
    errors = list()
    notes = list()
    err_count_int = 0
    format = "%(asctime)-15s:%(levelname)-5s: %(message)s"
    logger = logging.getLogger()
    # level = logging.DEBUG
    level = logging.INFO

    @staticmethod
    def init():
        logging.basicConfig(level=Log.level, format=Log.format)

    @staticmethod
    def add_file(file_name_str):
        log_fh = logging.FileHandler(file_name_str)
        error_log_formatter = logging.Formatter(Log.format)
        log_fh.setFormatter(error_log_formatter)
        Log.logger.addHandler(log_fh)

    @staticmethod
    def debug(msg_str, *args, **kwargs):
        return logging.debug(msg_str, *args, **kwargs)

    @staticmethod
    def info(msg_str, *args, **kwargs):
        return logging.info(msg_str, *args, **kwargs)

    @staticmethod
    def warn(msg_str, *args, **kwargs):
        return logging.warn(msg_str, *args, **kwargs)

    @staticmethod
    def error(msg_str, *args, **kwargs):
        Log.err_count_int += 1
        return logging.error(msg_str, *args, **kwargs)

    @staticmethod
    def exception(msg_str="Unknown Exception", *args, **kwargs):
        Log.err_count_int += 1
        return logging.exception(msg_str, *args, **kwargs)

    @staticmethod
    def add_error(msg_str, *args, **kwargs):
        Log.errors.append(msg_str)
        Log.error(logging, msg_str, *args, **kwargs)

    @staticmethod
    def add_note(msg_str):
        Log.notes.append(msg_str)
