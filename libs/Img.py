import pyautogui

from libs.Core import *


class ImageException(Exception):
    pass


def screenshot_ts():
    pyautogui.screenshot(time.strftime('%Y%m%d_%H%M%S.png'))


class Pixel(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def click(self):
        Log.info("Pixel.click: Clicking on (%i,%i)", self.x, self.y)
        pyautogui.click(self.x, self.y)

    def drag(self, x=0, y=0):
        self.move()
        pyautogui.dragTo(self.x + x, self.y + y, 0.2, button='left')
        # time.sleep(0.5)

    def move(self, x=0, y=0):
        pyautogui.moveTo(self.x + x, self.y + y)

    def click_repeat(self, repeat: int):
        for _ in range(repeat):
            self.click()
            time.sleep(1)


class Image(Pixel):
    def __init__(self, path: str, cooldown=1.0, confidence=0.9):
        super().__init__()
        self.path = path
        self.x = 0
        self.y = 0
        self.cooldown = cooldown
        self.confidence = confidence

    def search_once(self):
        try:
            Log.debug("Image.search_once: Searching for %s", self.path)
            self.x, self.y = pyautogui.locateCenterOnScreen(
                self.path, confidence=self.confidence
            )
        except TypeError:
            Log.debug("Image.search_once: %s not found. Cooling down for %d", self.path, self.cooldown)
            time.sleep(self.cooldown)
            raise ImageException

    def search(self, attempts=1):
        for i in range(attempts):
            try:
                self.search_once()
                Log.info('Image.search: Found %s on attempt %i', self.path, i + 1)
                return
            except ImageException:
                pass
        Log.info('Image.search: %s not found after %i attempts', self.path, attempts)
        raise ImageException

    def clear(self):
        try:
            self.search_once()
        except ImageException:
            return
        raise ImageException

    def click_clear(self, wait_flt=None):
        self.click()
        if wait_flt is None:
            time.sleep(self.cooldown)
        else:
            time.sleep(wait_flt)
        try:
            self.search()
        except ImageException:
            Log.info('Image.click_clear: %s disappeared', self.path)
        else:
            raise ImageException

    def search_click(self, attempts=1):
        self.search(attempts)
        self.click()

    def search_click_clear(self, attempts=1):
        for _ in range(attempts):
            try:
                self.search()
                self.click_clear()
                return
            except ImageException:
                pass

class Images(object):
    def __init__(self, path_format: str):
        self.path_format = path_format
        self.image_dict = {}

    def set(self, name: str, cooldown=1.0, confidence=0.9):
        self.image_dict[name] = Image(self.path_format % name, cooldown=cooldown, confidence=confidence)

    def get(self, name: str, cooldown=1.0, confidence=0.9) -> Image:
        try:
            return self.image_dict[name]
        except KeyError:
            self.set(name, cooldown, confidence)
            return self.image_dict[name]


