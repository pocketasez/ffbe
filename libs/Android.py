from libs.Img import *

pyautogui.FAILSAFE = False


# raise FailSafeException('PyAutoGUI fail-safe triggered from mouse moving to upper-left corner. To disable this
# fail-safe, set pyautogui.FAILSAFE to False.')

class Ffbe(object):
    def __init__(self):
        # App init
        self.main_screen_img = Image("png\\ffbe\\main_screen.png")
        self.start_icon_img = Image("png\\ffbe\\start_icon.png")
        self.cooldown_flt = 0.5

        # Depart Images
        self.next_img = Image("png\\ffbe\\next.png")
        self.rank_img = Image("png\\ffbe\\rank.png")
        self.manage_items_img = Image("png\\ffbe\\manage_items.png")
        self.depart_img = Image("png\\ffbe\\depart.png")
        self.adventure_img = None

        # Battle Images
        self.auto_img = Image("png\\ffbe\\auto.png", confidence_flt=0.99999)
        self.repeat_img = Image("png\\ffbe\\repeat.png", confidence_flt=0.99999)
        self.repeat_disabled_img = Image("png\\ffbe\\repeat_disabled.png", confidence_flt=0.99999)
        self.menu_img = Image("png\\ffbe\\menu.png", confidence_flt=0.99999)
        self.menu_disabled_img = Image("png\\ffbe\\menu_disabled.png", confidence_flt=0.99999)
        self.battle_pos_ary = []
        for i in range(6):
            self.battle_pos_ary.append(Pixel())
        self.lower_drag_pix = Pixel()
        self.upper_drag_pix = Pixel()

        # Post Battle
        self.results_gil_img = Image("png\\ffbe\\gil.png")
        self.results_unit_exp_img = Image("png\\ffbe\\results_unit_exp.png")
        self.results_next_img = Image("png\\ffbe\\results_next.png")
        self.unit_exp_next_img = Image("png\\ffbe\\unit_exp.png")
        self.missions_next_img = Image("png\\ffbe\\missions_next.png", confidence_flt=0.8)
        self.items_obtained_img = Image("png\\ffbe\\items_obtained.png")
        self.results_next_2_img = Image("png\\ffbe\\results_next_2.png")

        # Ability
        self.dual_black_magic_img = Image("png\\ffbe\\ability\\dual_black_magic.png")

        # Exception Images
        self.use_lapis_img = Image("png\\use_lapis.png")
        self.yes_lapis_img = Image("png\\yes_lapis.png")
        self.error_ok_img = Image("png\\error_ok.png")
        self.reward_close_img = Image("png\\ffbe\\reward_close.png")
        self.dont_request_img = Image("png\\ffbe\\dont_request.png")
        self.teamviewer_ok = Image("png\\tm_ok.png")
        self.services_stopped_ok = Image("png\\ffbe\\services_stopped_ok.png")
        self.unit_data_img = Image("png\\ffbe\\unit_data.png")
        self.unit_data_ok_img = Image("png\\ffbe\\unit_data_ok.png")

    def set_adventure(self, adventure_img):
        self.adventure_img = adventure_img

    def start_app(self):
        self.start_icon_img.search_click(60)
        self.main_screen_img.search_click_clear(60, 3)

    def cooldown(self):
        time.sleep(self.cooldown_flt)

    def close_app(self):
        pass

    def battle_ready_wait(self):
        self.repeat_img.search(50)

    def battle_setup(self):
        self.repeat_img.search(30)
        self.auto_img.search(5)
        y = 300
        for i in range(3):
            assert isinstance(self.battle_pos_ary[i], Pixel)
            self.battle_pos_ary[i].x = self.auto_img.x
            self.battle_pos_ary[i].y = self.auto_img.y - y
            y -= 100
        y = 300
        for i in range(3, 6):
            assert isinstance(self.battle_pos_ary[i], Pixel)
            self.battle_pos_ary[i].x = self.auto_img.x + 250
            self.battle_pos_ary[i].y = self.auto_img.y - y
            y -= 100
        self.lower_drag_pix.x = self.auto_img.x + 210
        self.lower_drag_pix.y = self.auto_img.y - 60
        self.upper_drag_pix.x = self.auto_img.x + 210
        self.upper_drag_pix.y = self.auto_img.y - 260

    def battle_engage(self, pos_int):
        assert isinstance(self.battle_pos_ary[pos_int], Pixel)
        self.battle_pos_ary[pos_int].click()

    def battle_engage_all(self):
        for pos_pix in self.battle_pos_ary:
            assert isinstance(pos_pix, Pixel)
            pos_pix.click()

    def battle_guard(self, pos_int):
        assert isinstance(self.battle_pos_ary[pos_int], Pixel)
        self.battle_pos_ary[pos_int].drag(y=150)

    def battle_guard_all(self):
        for pos_pix in self.battle_pos_ary:
            assert isinstance(pos_pix, Pixel)
            pos_pix.drag(y=150)

    def battle_ability(self, pos_int, y_drag_int, ability_img):
        assert isinstance(self.battle_pos_ary[pos_int], Pixel)
        assert isinstance(ability_img, Image)
        self.battle_pos_ary[pos_int].drag(x=150)
        self.cooldown()
        self.lower_drag_pix.drag(y=y_drag_int)
        self.cooldown()
        ability_img.search_click(3)
        self.cooldown()

    def battle_dual_black_magic(self, pos_int, y_drag_int, y_drag_up_int, ability_img):
        self.battle_ability(pos_int, y_drag_int, self.dual_black_magic_img)
        assert isinstance(ability_img, Image)
        self.upper_drag_pix.drag(y=y_drag_up_int)
        self.cooldown()
        self.cooldown()
        ability_img.search_click(3)
        self.cooldown()
        ability_img.click()
        self.cooldown()

    def battle_dual_ability(
            self, pos_int, scroll_int, dual_ability_img, scroll_up_int, ability_1_img, ability_2_img=None
    ):
        assert isinstance(self.battle_pos_ary[pos_int], Pixel)
        assert isinstance(dual_ability_img, Image)
        assert isinstance(ability_1_img, Image)
        if ability_2_img is None:
            ability_2_img = ability_1_img
        assert isinstance(ability_2_img, Image)
        self.battle_ability(pos_int, scroll_int, dual_ability_img)
        for _ in range(scroll_up_int):
            self.upper_drag_pix.drag(y=145)
        self.cooldown()
        try:
            ability_1_img.search_click(2)
        except ImageException:
            self.upper_drag_pix.drag(y=145)
            self.cooldown()
            ability_1_img.search_click(2)
        self.cooldown()
        ability_2_img.search_click(2)
        self.cooldown()

    def auto_battle(self):
        self.auto_img.search_click(40)
        try:
            time.sleep(2)
            self.repeat_disabled_img.search_once()
        except ImageException:  # Auto not clicked properly
            self.auto_img.search_click(40)

    def depart(self, lapis_bln=True):
        try:
            self.next_img.search_click(5)
        except ImageException:
            if lapis_bln is True:
                self.use_lapis_img.search_click(5)
                self.yes_lapis_img.search_click(5)
                try:
                    self.next_img.search_click(5)
                except ImageException:
                    self.error_ok_img.search_click(3)
                    self.next_img.search_click(5)
            else:
                raise
        self.rank_img.search_click(5)
        self.manage_items_img.search(10)
        self.depart_img.search_click(5)
        try:
            self.repeat_img.search(10)
        except ImageException:
            self.unit_data_img.search_click(3)
            self.unit_data_ok_img.search_click(3)
            self.rank_img.search_click(5)
            self.manage_items_img.search(10)
            self.depart_img.search_click(5)
            self.repeat_img.search(20)

    def end_results(self, completed_bln=True):
        try:
            self.results_gil_img.search_click(60)
        except ImageException:
            self.error_ok_img.search_click(5)
            self.results_gil_img.search_click(30)
        self.cooldown()
        self.results_unit_exp_img.search_click(2)
        self.results_next_img.search_click(2)
        self.unit_exp_next_img.search_click_clear(10, 3)  # "Level up" would require 2 clicks
        if completed_bln is False:
            self.missions_next_img.search_click(5)
        try:
            self.items_obtained_img.search_click(5)
        except ImageException:
            pass
        self.results_next_2_img.search_click(5)
        try:
            self.dont_request_img.search_click(2)
        except ImageException:
            pass

class Memu(object):
    # Requires nox icon pinned on windows start bar
    def __init__(self):
        self.taskbar_pin_img = Image("png\\memu\\taskbar_pin.png")
        self.close_img = Image("png\\memu\\close.png")

    def start_app(self):
        self.taskbar_pin_img.search_click(20)

    def close_app(self):
        self.close_img.search_click(20)
        time.sleep(20)
        # self.close_ok_img.click(20)


if __name__ == '__main__':
    pyautogui.screenshot('my_screenshot.png')
