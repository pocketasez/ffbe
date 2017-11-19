from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        battle = Battle()
        dungeon = Dungeon()
        dungeon.adventure_i = DepartureIs.get("25_5")
        boss_i = Image("tmp\\magitek.png")

        while True:
            dungeon.depart_bonus(False)
            battle.setup()
            battle.ability(0, -400, "imperil")
            battle.ability(1, -100, "deprotect")
            battle.ability(2, -100, "protect", 4)
            battle.ability(3, -400, "deshell")
            battle.ability(4, -400, "frost_flash")
            battle.guard(5)

            # try:
            #     battle.ability(5, -400, "divine_ruination")
            # except ImageException:
            #     pass
            # exit()
            battle.engage_all()
            while True:
                battle.setup()
                try:
                    boss_i.search()
                    break
                except ImageException:
                    battle.repeat()

            battle.ability(4, -400, "frost_flower_blitz")
            battle.engage(4)
            battle.repeat()

            dungeon.repeat_results()
            dungeon.results()

if __name__ == '__main__':
    m = Run()
    m.run()
