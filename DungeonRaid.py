from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        battle = Battle()
        dungeon = Dungeon()
        dungeon.adventure_i = DepartureIs.get("1_1")
        while True:
            try:
                dungeon.depart_unit("fryevia")
            except ImageException:
                pass

            battle.setup()
            battle.ability(0, -400, "arms_eraser")
            battle.ability(1, -150, "shadow_guard", 0)
            battle.ability(2, -400, "synthesis")
            battle.ability(3, -400, "frost_flower_blitz")
            battle.ability(4, -400, "frost_flower_blitz")
            try:
                battle.ability(5, -400, "frost_flower_blitz")
            except ImageException:
                battle.back_i.search_click(3)
                time.sleep(1)
                battle.ability(5, -300, "frost_flower_blitz")

            battle.engage_all()

            try:
                for i in range(3):
                    battle.ready_wait()
                    battle.ability(0, -400, "light_is_with_us")
                    battle.ability(1, -400, "guard_order", 0)
                    battle.ability(2, -130, "hyper_nullall", 0)
                    battle.engage(0)
                    battle.engage(1)
                    battle.engage(2)
                    battle.repeat()

                    battle.ready_wait()
                    battle.guard(0)
                    battle.ability(1, -400, "assault_order", 0)
                    battle.ability(2, -400, "al_bhed_potion", 0)
                    battle.engage(0)
                    battle.engage(1)
                    battle.engage(2)
                    battle.repeat()

                    battle.ready_wait()
                    battle.ability(0, -400, "arms_eraser")
                    battle.ability(1, -150, "shadow_guard", 0)
                    battle.ability(2, -180, "synthesis")
                    battle.engage(0)
                    battle.engage(1)
                    battle.engage(2)
                    battle.repeat()

            except ImageException:
                pass

            dungeon.results_raid()


if __name__ == '__main__':
    m = Run()
    m.run()
