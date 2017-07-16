from Main import *


class FFBEMain(Main):
    def __init__(self):
        super().__init__()
        self.exp = Exploration()
        self.battle = Battle()

    def main(self):
        exp = Exploration()
        battle = Battle()
        items_i = Image("png\\ffbe\\exploration\\items_obtained.png")

        exp.setup()

        i = 0
        zone_1 = 15
        zone_2 = 15
        try:
            for i in range(zone_1):
                try:
                    while True:
                        exp.nw()
                        exp.se()
                except ImageException:
                    logging.info("Battle %i of %i", i, zone_1)
                    battle.setup()
                    battle.ability(2, -100, "waylay")
                    battle.dual_black_magic(4, -400, 310, "osmose", -10, "thundaga")
                    battle.engage(2)
                    battle.cooldown()
                    battle.engage_all()
                    items_i.search_click(40)
                    battle.cooldown(2)
        except ImageException:
            logging.warning("STOPPED on %i of %i", i, zone_1)
            screenshot_ts()

if __name__ == '__main__':
    m = FFBEMain()
    m.run()
