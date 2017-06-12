from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        taskbar_pin_i = Image("png\\memu\\taskbar_pin.png")

        taskbar_pin_i.search_click(3)

        dungeon = Dungeon()
        battle = Battle()
        while True:
            dungeon.depart_bonus()

            battle.setup()
            battle.dual_ability(
                2, -400, "dual_black_magic",
                400, "osmose", None,
                -100, "meteor"
            )
            battle.engage_all()

            battle.repeat()

            battle.repeat()

            battle.setup()
            battle.ability(0, -300, "deprotect")
            battle.ability(1, -300, "imperil")
            battle.dual_ability(
                2, -400, "dual_black_magic",
                220, "meteor"
            )
            battle.ability(3, -300, "deshell")
            battle.ability(4, -350, "dark_nebula")
            battle.engage_all()

            battle.repeat()

            dungeon.repeat_results()

if __name__ == '__main__':
    m = Run()
    m.run()
