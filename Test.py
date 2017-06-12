from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        taskbar_pin_i = Image("png\\memu\\taskbar_pin.png")
        taskbar_pin_i.search_click()
        menu = Menu()
        battle = Battle()
        try:
            # menu.start()
            battle.repeat_i.search(2)
        except Exception:
            screenshot_ts()
            raise


if __name__ == '__main__':
    m = Run()
    m.run()
