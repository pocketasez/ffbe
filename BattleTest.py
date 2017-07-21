from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        taskbar_pin_i = Image("png\\memu\\taskbar_pin.png")
        taskbar_pin_i.search_click()
        battle = Battle()
        wifi = Image("png\\ffbe\\connecting.png")
        while True:
            wifi.search()
            time.sleep(0.5)
        logging.info("%i, %i", wifi.x, wifi.y)
        #
        # W = 570
        # H = 1012
        # battle.setup()
        # battle.ability(3, -400, "frost_flower_blitz")
        # battle.ability(4, -400, "frost_flower_blitz")
        # battle.ability(5, -400, "frost_flower_blitz")


if __name__ == '__main__':
    m = Run()
    m.run()
