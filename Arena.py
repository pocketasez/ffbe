from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):

    def __init__(self):
        super().__init__()
        self.battle = Battle()
        self.arena = Arena()

    def main(self):
        MemuIs.get("taskbar_pin").search_click()
        try:
            while True:
                self.arena.begin()
                self.battle.setup()

                try:
                    # self.battle.guard(0)
                    self.battle.ability(0, -400, "provoke")
                    # self.battle.dual_ability(0, -400, "dualcast", 200, "curaja", 0)
                except ImageException:
                    self.battle.mp_i.search_click(2)
                try:
                    self.battle.ability(1, -230, "blizzard_flask")
                    # self.battle.ability(1, -230, "fire_flask")
                except ImageException:
                    self.battle.mp_i.search_click(2)
                try:
                    self.battle.ability(2, -300, "blizzard_flask")
                    # self.battle.ability(2, -300, "fire_flask")
                except ImageException:
                    self.battle.mp_i.search_click(2)
                try:
                    self.battle.ability(3, -200, "meteor")
                    # self.battle.dual_ability(3, -400, "dual_black_magic", 210, "meteor")
                    # self.battle.ability(3, -400, "aero_blitz")
                except ImageException:
                    self.battle.mp_i.search_click(2)
                try:
                    self.battle.ability(4, -200, "meteor")
                    # self.battle.dual_ability(4, -400, "dual_black_magic", 210, "meteor")
                    # self.battle.ability(4, -400, "aero_blitz")
                except ImageException:
                    self.battle.mp_i.search_click(2)
                # exit()
                self.battle.engage_all()
                for _ in range(100):
                    try:
                        self.battle.repeat_i.search_click()
                    except ImageException:
                        pass
                    try:
                        self.arena.won_i.search()
                        break
                    except ImageException:
                        pass
                self.arena.results()
        except ImageException:
            pass


if __name__ == '__main__':
    m = Run()
    m.run()
