from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):

    def __init__(self):
        super().__init__()
        self.battle = Battle()
        self.arena = Arena()

    def main(self):
        # self.memu.taskbar_pin_img.search_click()
        gifts_img = Image("png\\ffbe\\friends\\gifts.png")
        receive_all_img = Image("png\\ffbe\\friends\\receive_all.png")
        back_img = Image("png\\ffbe\\friends\\back.png")
        try:
            while True:
                gifts_img.search_click(10)
                receive_all_img.search_click(10)
                back_img.search_click(10)

        except ImageException:
            screenshot_ts()


if __name__ == '__main__':
    m = Run()
    m.run()
