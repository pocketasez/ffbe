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
            battle.ability(0, -400, "full_break")
            battle.ability(1, -400, "bladeblitz")
            battle.ability(2, -400, "bladeblitz")
            battle.ability(3, -400, "bladeblitz")
            battle.ability(4, -320, "fire_flask")
            try:
                battle.ability(5, -400, "divine_ruination")
            except ImageException:
                pass
            # exit()
            battle.engage_all()
            for _ in range(2):
                battle.repeat()
            battle.setup()
            battle.ability(4, 0, "osmose")
            battle.engage(4)
            battle.repeat()
            battle.cooldown()

            battle.setup()
            battle.ability(4, -320, "fire_flask")
            battle.engage(4)

            dungeon.repeat_results()
            dungeon.results()

if __name__ == '__main__':
    m = Run()
    m.run()
