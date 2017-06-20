from Main import *


class FFBEMain(Main):
    def __init__(self):
        super().__init__()
        self.exp = Exploration()
        self.battle = Battle()
        self.items_img = Image("png\\ffbe\\exploration\\items_obtained.png")

    def main(self):
        self.memu.taskbar_pin_img.search_click()
        self.exp.setup()
        i = 0
        zone_1 = 15
        zone_2 = 15
        try:
            for i in range(zone_1):
                try:
                    while True:
                        self.exp.nw()
                        self.exp.se()
                except ImageException:
                    logging.info("Battle %i of %i", i, zone_1)
                    self.battle.setup()
                    self.battle.ability(2, -100, "waylay")
                    self.battle.dual_black_magic(4, -400, 310, "osmose", -10, "thundaga")
                    self.battle.engage(2)
                    self.battle.cooldown()
                    self.battle.engage_all()
                    self.items_img.search_click(40)
                    self.battle.cooldown(2)
        except ImageException:
            logging.warning("STOPPED on %i of %i", i, zone_1)
            screenshot_ts()

if __name__ == '__main__':
    m = FFBEMain()
    m.run()
