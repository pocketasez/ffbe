from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        summon_img = Image("png\\ffbe\\summon\\10.png")
        next_img = Image("png\\ffbe\\summon\\next.png")
        while True:
            summon_img.search_click(10)
            time.sleep(1)
            summon_img.search_click()
            summon_img.y = summon_img.y - 400
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


if __name__ == '__main__':
    m = Run()
    m.run()
