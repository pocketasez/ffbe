from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):

    def main(self):
        # self.memu.taskbar_pin_img.search_click()
        # for _ in range(30):
        asdf = pyautogui.locateOnScreen("png\\ffbe\\world\\world.png", confidence=0.8)
        print(asdf)

if __name__ == '__main__':
    m = Run()
    m.run()
