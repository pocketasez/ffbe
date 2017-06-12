from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):

    def __init__(self):
        super().__init__()
        self.battle = Battle()
        self.arena = Arena()

    def main(self):
        # self.memu.taskbar_pin_img.search_click()
        summon_img = Image("png\\ffbe\\summon\\summon_raid.png")
        next_img = Image("png\\ffbe\\summon\\next.png")
        try:
            while True:
                summon_img.search_click(10)
                time.sleep(0.5)
                summon_img.search_click(10)
                summon_img.y -= 400
                while True:
                    try:
                        next_img.search_click()
                        break
                    except ImageException:
                        summon_img.click()
                time.sleep(1)
                while True:
                    try:
                        next_img.search_click()
                        break
                    except ImageException:
                        summon_img.click()

        except ImageException:
            screenshot_ts()


if __name__ == '__main__':
    m = Run()
    m.run()
