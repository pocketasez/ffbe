from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        taskbar_pin_i = Image("png\\memu\\taskbar_pin.png")
        taskbar_pin_i.search_click()
        battle = Battle()
        dungeon = Dungeon()
        dungeon.adventure_i = DepartureIs.get("25_5")
        hein_i = Image("tmp\\hein.png")

        while True:
            dungeon.depart_bonus(False)
            battle.setup()
            battle.ability(0, -400, "deshell")
            battle.ability(1, -200, "shell", 3)
            battle.ability(2, -400, "shell", 4)
            battle.ability(3, -400, "frost_flash")
            battle.ability(4, -400, "frost_flash")
            # try:
            #     battle.ability(5, -400, "divine_ruination")
            # except ImageException:
            #     pass
            # exit()
            battle.engage_all()
            while True:
                battle.setup()
                try:
                    hein_i.search()
                    break
                except ImageException:
                    battle.repeat()

            battle.ability(3, -400, "frost_flower_blitz")
            battle.ability(4, -400, "frost_flower_blitz")
            battle.engage(3)
            battle.engage(4)
            battle.repeat()

            dungeon.repeat_results()
            dungeon.results()

if __name__ == '__main__':
    m = Run()
    m.run()
