from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        super().main()

        menu = Menu()
        dungeon = Dungeon()
        battle = Battle()

        #
        dungeon.adventure_i = DepartureIs.get("15_4")

        # dungeon.adventure_i = DepartureIs.get("faeries")  # Black, Green, White
        # dungeon.adventure_i = DepartureIs.get("masters")  # Guard, Power, Tech
        # dungeon.adventure_i = DepartureIs.get("wise")  # Healing, Support

        # for _ in range(3):
        while True:
            dungeon.depart()
            battle.auto()
            dungeon.results()

if __name__ == '__main__':
    m = Run()
    m.run()
