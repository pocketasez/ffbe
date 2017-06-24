from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        taskbar_pin_i = Image("png\\memu\\taskbar_pin.png")
        vargas_i = Image("png\\ffbe\\tmp\\holy_flame_vargas.png")
        taskbar_pin_i.search_click()
        menu = Menu()
        battle = Battle()
        dungeon = Dungeon()
        dungeon.adventure_i = DepartureIs.get("25_3")
        while True:
            dungeon.depart_bonus()
            battle.setup()

            battle.ability(2, -200, "genesis")
            battle.engage_all()

            battle.repeat()

            try:
                battle.ready_wait()
                vargas_i.search(3)
            except ImageException:
                battle.repeat()
                battle.cooldown()

            battle.ready_wait()
            battle.ability(1, -400, "ravaging_blow")
            battle.ability(2, -100, "destiny")
            battle.ability(4, -300, "celestial_light", 1)
            battle.engage(4)
            battle.engage_all()

            dungeon.results()

if __name__ == '__main__':
    m = Run()
    m.run()
