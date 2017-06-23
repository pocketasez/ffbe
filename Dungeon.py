from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        taskbar_pin_i = Image("png\\memu\\taskbar_pin.png")
        taskbar_pin_i.search_click(3)

        menu = Menu()
        dungeon = Dungeon()
        battle = Battle()

        dungeon.adventure_i = DepartureIs.get("1_2")
        try:
            while True:
                dungeon.depart()
                try:
                    battle.auto()
                    dungeon.results()
                except ImageException:
                    menu.start()
                    try:
                        battle.repeat_i.search(30)
                        battle.auto()
                    except ImageException:
                        battle.wait_end()
                    dungeon.results()
        except ImageException:
            screenshot_ts()

if __name__ == '__main__':
    m = Run()
    m.run()
