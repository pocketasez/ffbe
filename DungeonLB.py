from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        taskbar_pin_i = Image("png\\memu\\taskbar_pin.png")
        taskbar_pin_i.search_click(3)

        menu = Menu()
        dungeon = Dungeon()
        battle = Battle()

        dungeon.adventure_i = DepartureIs.get("1_3")
        # dungeon.adventure_i = DepartureIs.get("15_4")
        monster_1_p = Pixel()
        while True:
            try:
                dungeon.depart()
                # Prepare
                battle.repeat_i.search(15)
                battle.auto_i.search()
                monster_1_p.x = battle.repeat_i.x
                monster_1_p.y = battle.repeat_i.y - 630

                # Turn 1
                battle.repeat_i.search(15)
                monster_1_p.click()
                battle.auto_i.click()
                battle.cooldown()
                battle.menu_disabled_i.search(30)
                battle.auto_i.click()

                # Turn 2
                battle.repeat_i.search(15)
                monster_1_p.click()
                battle.auto_i.click()
                battle.cooldown()
                battle.menu_disabled_i.search(30)
                battle.auto_i.click()

                # Turn 3
                battle.repeat_i.search(15)
                monster_1_p.click()
                battle.auto_i.click()

                # dungeon.repeat_results()

                dungeon.results(30)
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
