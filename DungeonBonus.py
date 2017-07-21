from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        taskbar_pin_i = Image("png\\memu\\taskbar_pin.png")
        taskbar_pin_i.search_click()
        battle = Battle()
        dungeon = Dungeon()
        dungeon.adventure_i = DepartureIs.get("25_5")
        while True:
            dungeon.depart_bonus()
            battle.setup()
            battle.ability(0, -400, "resist_stop", 0)
            battle.ability(1, -400, "imperil")
            battle.ability(2, -400, "deprotect")
            battle.ability(3, -400, "deshell")
            battle.ability(4, -400, "frost_flower_blitz")
            battle.engage_all()

            dungeon.repeat_results()
            dungeon.results()

if __name__ == '__main__':
    m = Run()
    m.run()
