                                                                                                                                                                                                                                                                                        from Main import *


class TM(Main):
    def __init__(self):
        super().__init__()
        self.battle = Battle()

    def main(self):
        try:
            adventure_ie = ImageExcept("png\\ffbe\\tmp\\pro.png")
            bonus_img = Image("png\\ffbe\\tmp\\bonus.png")
            dual_black_magic_img = Image("png\\ffbe\\ability\\dual_black_magic.png")
            barfira_img = AbilityImage("barfira", confidence_flt=0.96)
            ice_blitz_img = AbilityImage("ice_blitz")
            ravaging_blow_img = AbilityImage("ravaging_blow")
            blizzard_flask_img = AbilityImage("blizzard_flask")
            blizzaga_img = AbilityImage("blizzaga", confidence_flt=0.96)

            self.ffbe.set_adventure(adventure_ie)
            self.memu.taskbar_pin_img.search_click()
            self.ffbe.adventure_ie.search_click_except(2, 6)
            self.ffbe.next_ie.search_click_except(2, 6)
            self.ffbe.rank_img.search_click(2)
            self.ffbe.manage_items_img.search(40)
            self.ffbe.depart_ie.search_click(5)

            self.ffbe.battle_setup()

            self.ffbe.battle_pos_ary[0].drag(x=150)
            self.ffbe.cooldown()
            self.ffbe.lower_drag_pix.drag(y=-250)
            self.ffbe.cooldown()
            barfira_img.search_click(3)
            self.ffbe.cooldown()
            self.ffbe.battle_pos_ary[0].click()
            self.ffbe.cooldown()

            self.ffbe.battle_pos_ary[1].drag(x=150)
            self.ffbe.cooldown()
            self.ffbe.lower_drag_pix.drag(y=-300)
            self.ffbe.cooldown()
            blizzard_flask_img.search_click(3)
            self.ffbe.cooldown()

            self.ffbe.battle_pos_ary[2].drag(x=150)
            self.ffbe.cooldown()
            self.ffbe.lower_drag_pix.drag(y=-150)
            self.ffbe.cooldown()
            ravaging_blow_img.search_click(3)
            self.ffbe.cooldown()

            self.ffbe.battle_pos_ary[3].drag(x=150)
            self.ffbe.cooldown()
            self.ffbe.lower_drag_pix.drag(y=-400)
            self.ffbe.cooldown()
            dual_black_magic_img.search_click(3)
            self.ffbe.cooldown()
            self.ffbe.upper_drag_pix.drag(y=210)
            self.ffbe.cooldown()
            blizzaga_img.search_click(3)
            self.ffbe.cooldown()
            blizzaga_img.click()
            self.ffbe.cooldown()

            self.ffbe.battle_pos_ary[4].drag(x=150)
            self.ffbe.cooldown()
            self.ffbe.lower_drag_pix.drag(y=-400)
            self.ffbe.cooldown()
            dual_black_magic_img.search_click(3)
            self.ffbe.cooldown()
            self.ffbe.upper_drag_pix.drag(y=310)
            self.ffbe.cooldown()
            blizzaga_img.search_click(3)
            self.ffbe.cooldown()
            blizzaga_img.click()
            self.ffbe.cooldown()

            self.ffbe.battle_engage(2)
            self.ffbe.cooldown()
            self.ffbe.battle_engage_all()

            try:
                self.ffbe.repeat_img.search_click(25)
            except ImageException:
                pass

        except ImageException:
            screenshot_ts()


if __name__ == '__main__':
    m = TM()
    m.run()
