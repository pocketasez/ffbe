from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        taskbar_pin_i = Image("png\\memu\\taskbar_pin.png")
        taskbar_pin_i.search_click(3)

        dungeon = Dungeon()
        battle = Battle()

        # dungeon.adventure_i = DepartureIs.get("1_3")
        dungeon.adventure_i = DepartureIs.get("masters")
        while True:
            dungeon.depart(False)
            battle.auto()
            dungeon.results()

if __name__ == '__main__':
    m = Run()
    m.run()
