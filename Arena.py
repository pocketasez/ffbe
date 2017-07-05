from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):

    def __init__(self):
        super().__init__()
        self.battle = Battle()
        self.arena = Arena()

    def main(self):
        MemuIs.get("taskbar_pin").search_click()
        # taskbar_pin_i = Image("png\\taskbar_nox.png")
        # taskbar_pin_i.search_click()
        try:
            while True:
                self.arena.begin()
                self.battle.setup()

                # self.battle.ability(0, -400, "provoke")
                try:
                    self.battle.ability(0, -400, "armor_eraser")
                except ImageException:
                    pass
                try:
                    self.battle.ability(1, -370, "thunder_flask")
                    # self.battle.ability(1, -300, "blizzard_flask")
                except ImageException:
                    pass
                try:
                    # self.battle.ability(2, -300, "blizzard_flask")
                    self.battle.ability(2, -320, "thunder_flask")
                except ImageException:
                    pass
                try:
                    self.battle.dual_ability(3, -400, "dual_black_magic", 220, "meteor")
                    # self.battle.ability(3, -200, "prism_heart")
                    # self.battle.ability(3, -400, "ice_blitz")
                except ImageException:
                    pass
                try:
                    # self.battle.ability(4, -200, "ice_age")
                    self.battle.dual_ability(4, -400, "dual_black_magic", 220, "meteor")
                    # self.battle.ability(4, -200, "meteor")
                except ImageException:
                    pass
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
