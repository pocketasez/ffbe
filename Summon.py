from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):

    def __init__(self):
        super().__init__()
        self.battle = Battle()
        self.arena = Arena()

    def main(self):
        summon_img = Image("png\\ffbe\\summon\\1000.png")
        summon2_img = Image("png\\ffbe\\summon\\1000.png")
        next_img = Image("png\\ffbe\\summon\\next.png")
        next2_img = Image("png\\ffbe\\summon\\next.png")
        below_summon2_pix = Pixel()
        try:
            while True:
                summon_img.search_click(10)
                time.sleep(1)
                summon2_img.search_click()
                below_summon2_pix.x = summon2_img.x
                below_summon2_pix.y = summon2_img.y - 400
                while True:
                    try:
                        next_img.search_click()
                        break
                    except ImageException:
                        below_summon2_pix.click()
                time.sleep(1)
                while True:
                    try:
                        next2_img.search_click()
                        break
                    except ImageException:
                        below_summon2_pix.click()

        except ImageException:
            screenshot_ts()


if __name__ == '__main__':
    m = Run()
    m.run()
