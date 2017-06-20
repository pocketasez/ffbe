import logging
import time
import os
import pyautogui


class Executable(object):
    def main(self):
        print("ASDf")
        logging.error("asdf")
        raise ValueError

    def run(self):
        try:
            os.mkdir("logs")
        except FileExistsError:
            pass
        log_file = time.strftime("logs\\%Y%m%d_%H%M%S.log")
        logging_format = "%(asctime)-15s:%(levelname)-5s: %(message)s"
        logging.basicConfig(level=logging.INFO, format=logging_format)
        logger = logging.getLogger()
        formatter = logging.Formatter(logging_format)
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        try:
            self.main()
        except Exception:
            logging.exception("Unhandled exception")
            now_str = time.strftime("logs\\%Y%m%d_%H%M%S")
            fh.close()
            os.rename(log_file, "%s.err" % now_str)
            pyautogui.screenshot("%s.png" % now_str)

if __name__ == '__main__':
    x = Executable()
    x.run()
