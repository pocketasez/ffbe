from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        taskbar_pin_i = Image("png\\memu\\taskbar_pin.png")
        taskbar_pin_i.search_click()
        battle = Battle()
        dungeon = Dungeon()
        dungeon.adventure_i = DepartureIs.get("1_1")
        while True:
            dungeon.depart_unit("fryevia")

            battle.setup()
            battle.ability(2, -100, "goddess_miracle", 0)
            battle.engage(2)
            time.sleep(1)
            battle.ability(0, -400, "arms_eraser")
            battle.ability(1, 0, "celestial_light", 0)
            battle.ability(3, -400, "frost_flower_blitz")
            battle.ability(4, -400, "frost_flower_blitz")
            try:
                battle.ability(5, -400, "frost_flower_blitz")
            except ImageException:
                battle.ability(5, -100, "frost_flower_blitz")

            battle.engage_all()

            battle.ready_wait()
            battle.ability(0, -400, "armor_eraser")
            battle.ability(2, -200, "radiant_light", 0)
            battle.engage(0)
            battle.engage(2)
            battle.repeat()

            battle.ready_wait()
            battle.ability(0, -400, "arms_eraser")
            battle.engage(0)
            battle.repeat()

            dungeon.repeat_results()
            dungeon.results_raid()

if __name__ == '__main__':
    m = Run()
    m.run()
