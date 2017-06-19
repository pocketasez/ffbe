from libs.Img import *

Is = Images("png\\ffbe\\%s.png")
MenuIs = Images("png\\ffbe\\menu\\%s.png")
MemuIs = Images("png\\memu\\%s.png")

ArenaIs = Images("png\\ffbe\\arena\\%s.png")
SummonIs = Images("png\\ffbe\\summon\\%s.png")
UnitIs = Images("png\\ffbe\\unit\\%s.png")

AbilityIs = Images("png\\ffbe\\ability\\%s.png")

DepartureIs = Images("png\\ffbe\\departure\\%s.png")
BattleIs = Images("png\\ffbe\\battle\\%s.png")
ResultsIs = Images("png\\ffbe\\results\\%s.png")
WorldIs = Images("png\\ffbe\\world\\%s.png")

BattleIs.set("repeat", confidence=0.99999)
BattleIs.set("auto", confidence=0.99999)
BattleIs.set("repeat", confidence=0.99999)
BattleIs.set("repeat_disabled", confidence=0.99999)
BattleIs.set("menu.png", confidence=0.99999)
BattleIs.set("menu_disabled", confidence=0.99999)


class FFBEBase(object):
    def __init__(self):
        self.cooldown_sec = 1
        
    def cooldown(self, factor=1.0):
        time.sleep(self.cooldown_sec * factor)


class Menu(FFBEBase):
    def __init__(self):
        super().__init__()
        self.app_i = MenuIs.get("app")
        self.main_i = MenuIs.get("main")
        self.isnt_responding_i = MemuIs.get("isnt_responding")
        self.launcher_stop_i = MemuIs.get("launcher_stop")
        self.ok_i = MemuIs.get("ok")

    def start(self):
        self.app_i.search_click(3)
        for _ in range(30):
            try:
                self.isnt_responding_i.search()
                self.ok_i.search_click(3)
                self.app_i.search_click(3)
                self.main_i.search(30)  #
            except ImageException:
                pass
            try:
                self.main_i.search()
                break
            except ImageException:
                self.app_i.click()
        self.main_i.search_click_clear(3)


class Exploration(FFBEBase):
    def __init__(self):
        super().__init__()
        self.menu_img = Image("png\\ffbe\\exploration\\menu.png")
        self.north_pix = Pixel()
        self.south_pix = Pixel()
        self.east_pix = Pixel()
        self.west_pix = Pixel()

        self.north_west_pix = Pixel()
        self.south_east_pix = Pixel()

    def setup(self):
        self.menu_img.search(10)
        x = self.menu_img.x - 240
        y = self.menu_img.y - 500
        self.north_pix.x = x
        self.north_pix.y = y - 40
        self.south_pix.x = x
        self.south_pix.y = y + 40
        self.east_pix.x = x - 40
        self.east_pix.y = y
        self.west_pix.x = x + 40
        self.west_pix.y = y

        self.north_west_pix.y = self.north_pix.y
        self.north_west_pix.x = self.west_pix.x

        self.south_east_pix.y = self.south_pix.y
        self.south_east_pix.x = self.east_pix.x

    def n(self):
        self.north_pix.click()
        self.menu_img.search()

    def s(self):
        self.south_pix.click()
        self.menu_img.search()

    def e(self):
        self.east_pix.click()
        self.menu_img.search()

    def w(self):
        self.west_pix.click()
        self.menu_img.search()

    def nw(self):
        self.north_west_pix.click()
        self.menu_img.search()

    def se(self):
        self.south_east_pix.click()
        self.menu_img.search()


class Battle(FFBEBase):
    def __init__(self):
        super().__init__()

        self.auto_i = BattleIs.get("auto")
        self.repeat_i = BattleIs.get("repeat")
        self.repeat_disabled_i = BattleIs.get("repeat_disabled")
        self.menu_i = BattleIs.get("menu")
        self.menu_disabled_i = BattleIs.get("menu_disabled")
        self.back_i = BattleIs.get("back")
        self.mp_i = BattleIs.get("mp")

        self.r_gil_i = ResultsIs.get("gil")

        self.tm_ok_i = Is.get("tm_ok")
        self.ffbe_app_i = Is.get("ffbe_app")

        self.pos_arr = []
        self.is_arr = []

        for i in range(6):
            self.is_arr.append(Images("png\\ffbe\\ability\\%s.png"))
            self.pos_arr.append(Pixel())
        self.lower_drag_pix = Pixel()
        self.upper_drag_pix = Pixel()

    def ready_wait(self):
        self.repeat_i.search(50)

    def setup(self):
        self.cooldown()
        self.repeat_i.search(40)
        self.repeat_i.search(40)
        self.auto_i.search(5)
        y = 300
        for i in range(3):
            assert isinstance(self.pos_arr[i], Pixel)
            self.pos_arr[i].x = self.auto_i.x
            self.pos_arr[i].y = self.auto_i.y - y
            y -= 100
        y = 300
        for i in range(3, 6):
            assert isinstance(self.pos_arr[i], Pixel)
            self.pos_arr[i].x = self.auto_i.x + 250
            self.pos_arr[i].y = self.auto_i.y - y
            y -= 100
        self.lower_drag_pix.x = self.auto_i.x + 210
        self.lower_drag_pix.y = self.auto_i.y - 60
        self.upper_drag_pix.x = self.auto_i.x + 210
        self.upper_drag_pix.y = self.auto_i.y - 260

    def get_pos_pix(self, pos_int) -> Pixel:
        return self.pos_arr[pos_int]

    def auto(self):
        self.auto_i.search_click(20)
        try:
            self.tm_ok_i.search_click(3)
        except ImageException:
            pass
        self.cooldown(3)
        self.wait_end()

    def wait_end(self):
        try:
            while True:
                self.menu_i.search()
                self.cooldown()
        except ImageException:
            pass

    def repeat(self):
        self.cooldown()
        self.repeat_i.search_click(40)

    def engage(self, pos_int):
        assert isinstance(self.pos_arr[pos_int], Pixel)
        self.pos_arr[pos_int].click()

    def engage_all(self):
        for pos_pix in self.pos_arr:
            assert isinstance(pos_pix, Pixel)
            pos_pix.click()

    def guard(self, pos_int):
        assert isinstance(self.pos_arr[pos_int], Pixel)
        self.pos_arr[pos_int].drag(y=150)

    def guard_all(self):
        for pos_pix in self.pos_arr:
            assert isinstance(pos_pix, Pixel)
            pos_pix.drag(y=150)

    def ability(self, pos_int, scroll_y_int=0, ability_str=None, cast_to_int=None):
        pos_pix = self.get_pos_pix(pos_int)
        pos_pix.drag(x=150)
        self.mp_i.search(2)
        self._ability(pos_int, scroll_y_int, ability_str, cast_to_int)

    def _ability(self, pos_int, scroll_y_int=0, ability_str=None, cast_to_int=None):
        ability_i = self.is_arr[pos_int].get(ability_str)
        self.scroll_y(scroll_y_int)
        try:
            ability_i.search_click(3)
        except ImageException:
            self.back_i.search_click(3)
            self.cooldown()
            raise
        self.cooldown()
        if cast_to_int is not None:
            assert isinstance(cast_to_int, int)
            cast_to_pix = self.get_pos_pix(cast_to_int)
            cast_to_pix.click()
            self.cooldown()

    def dual_black_magic(
            self, pos_int, scroll_y_int, scroll_y_2_int, ability_str, scroll_y_3_int=0, ability_2_str=None
    ):
        if ability_2_str is None:
            ability_2_str = ability_str
        self.ability(pos_int, scroll_y_int, "dual_black_magic")
        self._ability(scroll_y_2_int, ability_str)
        self._ability(scroll_y_3_int, ability_2_str)

    def dual_ability(
            self, pos_int, scroll_y_int, dual_ability_str: str,
            scroll_y_2_int, ability_str, cast_to_int=None,
            scroll_y_3_int=0, ability_2_str=None, cast_to_2_int=None
    ):
        self.ability(pos_int, scroll_y_int, dual_ability_str)
        self._ability(pos_int, scroll_y_2_int, ability_str, cast_to_int)
        if ability_2_str is None:
            ability_i = self.is_arr[pos_int].get(ability_str)
            ability_i.click()
            self.cooldown()
            if cast_to_int is not None:
                assert isinstance(cast_to_int, int)
                cast_to_pix = self.get_pos_pix(cast_to_int)
                cast_to_pix.click()
                self.cooldown()
        else:
            self._ability(pos_int, scroll_y_3_int, ability_2_str, cast_to_2_int)

    def scroll_y(self, y: int):
        if y > 0:
            self.upper_drag_pix.drag(y=y)
            self.cooldown()
        elif y < 0:
            self.lower_drag_pix.drag(y=y)
            self.cooldown()


class Arena(FFBEBase):
    def __init__(self):
        super(Arena, self).__init__()

        self.setup_empty_i = ArenaIs.get("setup_empty", confidence=0.99999)
        self.setup_i = ArenaIs.get("setup")
        self.ok_i = ArenaIs.get("ok")
        self.rank_i = ArenaIs.get("rank")
        self.yes_i = ArenaIs.get("yes")
        self.begin_i = ArenaIs.get("begin")

        self.results_i = ArenaIs.get("results")
        self.won_i = ArenaIs.get("won")
        self.result_ok_i = ArenaIs.get("result_ok", confidence=0.99999)
        self.rank_ok_i = ArenaIs.get("rank_ok", confidence=0.99999)
        self.rewards_ok_i = ArenaIs.get("rewards_ok", confidence=0.99999)

    def begin(self):
        self.setup_i.search_click(5)
        self.ok_i.search_click(5)
        self.rank_i.search_click(5)
        self.yes_i.search_click(5)
        self.begin_i.search(5)
        self.cooldown(3)
        self.begin_i.click()

    def results(self):
        self.won_i.search_click(20)
        self.cooldown()
        for _ in range(3):
            self.won_i.click()
            self.cooldown()
        self.result_ok_i.search_click(20)
        for _ in range(3):
            self.won_i.click()
            self.cooldown()
        self.rank_ok_i.search_click(20)
        self.cooldown()
        self.cooldown()
        try:
            self.rewards_ok_i.search(3)
            self.cooldown()
            self.rewards_ok_i.search_click_clear(3)
            self.cooldown()
            self.cooldown()
            self.result_ok_i.click()
        except ImageException:
            pass


class Dungeon(FFBEBase):
    def __init__(self):
        super().__init__()

        self.adventure_i = DepartureIs.get("elt")

        self.next_i = DepartureIs.get("next")
        self.use_lapis_i = DepartureIs.get("use_lapis")
        self.yes_i = DepartureIs.get("yes")

        self.rank_i = DepartureIs.get("rank")
        self.manage_items_i = DepartureIs.get("manage_items")
        self.depart_i = DepartureIs.get("depart")

        self.bonus_i = DepartureIs.get("bonus")
        self.unit_data_i = DepartureIs.get("unit_data")
        self.unit_data_ok_i = DepartureIs.get("unit_data_ok")

        self.b_repeat_i = BattleIs.get("repeat")

        self.r_gil_i = ResultsIs.get("gil")
        self.r_unit_exp = ResultsIs.get("unit_exp")
        self.r_rank_exp = ResultsIs.get("rank_exp")
        self.r_next = ResultsIs.get("next")

        self.r_unit_exp_2 = ResultsIs.get("unit_exp_2")
        self.r_items_obtained = ResultsIs.get("items_obtained")
        self.r_items_obtained = ResultsIs.get("units_obtained")
        self.r_next_2 = ResultsIs.get("next_2")
        self.r_dont_request = ResultsIs.get("dont_request")

        self.r_error_ok = ResultsIs.get("error_ok")

        self.b_daily_quest_close_i = Is.get("daily_quest_close")

    def _depart_rank(self):
        try:
            self.rank_i.search_click(10)
        except ImageException:
            self.next_i.search_click(10)
            self.rank_i.search_click(5)
        self.manage_items_i.search(10)
        self.depart_i.search_click(5)

    def depart(self):
        try:
            self.adventure_i.search_click(5)
        except ImageException:
            self.b_daily_quest_close_i.search_click()
            self.adventure_i.search_click(5)
        try:
            self.next_i.search_click(3)
        except ImageException:
            self.use_lapis_i.search_click(3)
            self.yes_i.search_click(3)
        self._depart_rank()
        try:
            self.b_repeat_i.search(20)
        except ImageException:
            self.unit_data_i.search_click(3)
            self.unit_data_ok_i.search_click(3)
            self._depart_rank()
            self.b_repeat_i.search(20)

    def depart_bonus(self):
        self.adventure_i.search_click(3)
        try:
            self.next_i.search_click(3)
        except ImageException:
            self.use_lapis_i.search_click(3)
            self.yes_i.search_click(3)
        self.next_i.search_click(3)
        for _ in range(4):
            try:
                self.bonus_i.search(2)
            except ImageException:
                self.next_i.drag(y=-400)
        try:
            self.bonus_i.search_click(3)
        except ImageException:
            self.rank_i.search_click(5)
        self.manage_items_i.search(10)
        self.depart_i.search_click(5)

    def results(self):
        # try:
        self.r_gil_i.search_click(30)
        # except ImageException:
        #     self.r_error_ok.search_click(5)
        #     self.r_gil_i.search_click(5)
        self.cooldown()
        self.r_unit_exp.search_click(2)
        self.r_next.search_click(2)
        self.r_unit_exp_2.search_click_clear(10)  # "Level up" would require 2 clicks
        # self.r_items_obtained.search_click(5)
        self.r_items_obtained.search_click(5)
        self.r_next_2.search_click(5)
        try:
            self.r_dont_request.search_click(2)
        except ImageException:
            pass

    def repeat_results(self):
        for _ in range(100):
            try:
                self.b_repeat_i.search_click()
            except ImageException:
                pass
            try:
                self.r_gil_i.search()
                break
            except ImageException:
                pass
        self.results()
