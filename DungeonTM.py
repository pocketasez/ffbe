from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        super().main()

        menu = Menu()
        dungeon = Dungeon()
        battle = Battle()

        dungeon.adventure_i = DepartureIs.get("1_2")
        # dungeon.adventure_i = DepartureIs.get("15_4")
        while True:
            try:
                dungeon.depart()
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

if __name__ == '__main__':
    m = Run()
    m.run()
