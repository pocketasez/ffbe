from libs.Img import *

pyautogui.FAILSAFE = False

Is = Images("libs\\ffbe\\%s.png")
MenuIs = Images("libs\\ffbe\\menu\\%s.png")
MemuIs = Images("libs\\memu\\%s.png")

ArenaIs = Images("libs\\ffbe\\arena\\%s.png")
SummonIs = Images("libs\\ffbe\\summon\\%s.png")
UnitIs = Images("libs\\ffbe\\unit\\%s.png")

AbilityIs = Images("libs\\ffbe\\ability\\%s.png")

DepartureIs = Images("libs\\ffbe\\departure\\%s.png")
BattleIs = Images("libs\\ffbe\\battle\\%s.png")
ResultsIs = Images("libs\\ffbe\\results\\%s.png")
WorldIs = Images("libs\\ffbe\\world\\%s.png")

BattleIs.set("repeat", confidence=0.99999)
BattleIs.set("auto", confidence=0.99999)
BattleIs.set("repeat_disabled", confidence=0.99999)
BattleIs.set("menu", confidence=0.99)  # Try finding this first
BattleIs.set("menu_disabled", confidence=0.99999)


def set_region(nw_x=0, nw_y=0, se_x=1920, se_y=1080):
    Is.set_region(nw_x, nw_y, se_x, se_y)
    MenuIs.set_region(nw_x, nw_y, se_x, se_y)
    MemuIs.set_region(nw_x, nw_y, se_x, se_y)

    ArenaIs.set_region(nw_x, nw_y, se_x, se_y)
    SummonIs.set_region(nw_x, nw_y, se_x, se_y)
    UnitIs.set_region(nw_x, nw_y, se_x, se_y)

    AbilityIs.set_region(nw_x, nw_y, se_x, se_y)

    DepartureIs.set_region(nw_x, nw_y, se_x, se_y)
    BattleIs.set_region(nw_x, nw_y, se_x, se_y)
    ResultsIs.set_region(nw_x, nw_y, se_x, se_y)
    WorldIs.set_region(nw_x, nw_y, se_x, se_y)


class Base(object):
    def __init__(self):
        self.img_set = None
        self.cooldown_sec = 1

    def cooldown(self, factor=1.0):
        time.sleep(self.cooldown_sec * factor)


class Menu(Base):
    def __init__(self):
        super().__init__()
        self.app_i = MenuIs.get("app")
        self.main_i = MenuIs.get("main")
        self.crash_ok_i = MenuIs.get("crash_ok")

    def start(self):
        try:
            self.crash_ok_i.search_click_clear(3)
        except ImageException:
            pass
        self.app_i.search_click(3)
        for _ in range(30):
            try:
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


class Exploration(Base):
    def __init__(self):
        super().__init__()
        self.menu_img = Image("libs\\ffbe\\exploration\\menu.png")
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


class Battle(Base):
    def __init__(self):
        super().__init__()

        self.auto_i = BattleIs.get("auto")
        self.repeat_i = BattleIs.get("repeat")
        self.repeat_disabled_i = BattleIs.get("repeat_disabled")
        self.menu_80_i = Image("libs\\ffbe\\battle\\menu.png")
        self.menu_i = BattleIs.get("menu")
        self.menu_disabled_i = BattleIs.get("menu_disabled")
        self.back_i = BattleIs.get("back")
        self.mp_i = BattleIs.get("mp")

        self.r_gil_i = ResultsIs.get("gil")

        self.repeat_disabled_i = BattleIs.get("repeat_disabled")
        self.play_yes_i = BattleIs.get("play_yes")

        self.pos_arr = []
        self.is_arr = []

        for i in range(6):
            self.is_arr.append(Images("libs\\ffbe\\ability\\%s.png"))
            self.pos_arr.append(Pixel())
        self.lower_drag_pix = Pixel()
        self.upper_drag_pix = Pixel()

    def ready_wait(self):
        self.cooldown()
        self.repeat_i.search(30)
        self.cooldown()

    def setup(self):
        self.cooldown()
        self.repeat_i.search(30)
        self.cooldown()
        try:  # Sometimes repeat doesnt start disable on battle.
            self.repeat_i.search()
        except ImageException:
            self.repeat_i.search(30)
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
        # try:
        #     self.tm_ok_i.search_click(3)
        # except ImageException:
        #     pass
        self.cooldown(3)
        self.wait_end()

    def wait_turn_end(self, search=30):
        self.menu_disabled_i.search(search)

    def wait_end(self):
        self.menu_80_i.wait_cleared()

    def repeat(self):
        self.repeat_i.search_click(40)
        self.cooldown()

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
        ability_i.search_click(3)
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


class Arena(Base):
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
        self.results_ok_i = ArenaIs.get("results_ok", confidence=0.99999)
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
        self.results_ok_i.search_click(20)
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
            self.results_ok_i.click()
        except ImageException:
            pass


class Dungeon(Base):
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
        self.connection_error_i = DepartureIs.get("connection_error")

        self.connecting_i = DepartureIs.get("connecting")
        self.nrg_i = DepartureIs.get("nrg")

        self.m_crash_ok_i = MemuIs.get("crash_ok")

        self.b_repeat_i = BattleIs.get("repeat")

        self.r_gil_i = ResultsIs.get("gil")
        self.r_unit_exp = ResultsIs.get("unit_exp")
        self.r_rank_exp = ResultsIs.get("rank_exp")
        self.r_next = ResultsIs.get("next")

        self.r_unit_exp_2 = ResultsIs.get("unit_exp_2")
        self.r_items_obtained = ResultsIs.get("items_obtained")
        self.r_units_obtained = ResultsIs.get("units_obtained")
        self.r_next_2 = ResultsIs.get("next_2")
        self.r_dont_request = ResultsIs.get("dont_request")

        self.r_error_ok = ResultsIs.get("error_ok")
        self.r_friends_ok = ResultsIs.get("friends_ok")

        self.b_daily_quest_close_i = Is.get("daily_quest_close")

        # Raid specific
        self.r_damage_i = ResultsIs.get("damage")
        self.r_event_pt_i = ResultsIs.get("event_pt")
        self.r_total_i = ResultsIs.get("total")

    def _depart_rank(self):
        try:
            self.rank_i.search_click(10)
        except ImageException:  # Sometimes the click doesnt go to the next page
            self.next_i.search_click(5)
            self.rank_i.search_click(10)
        self.manage_items_i.search(10)
        self.depart_i.search_click(5)

    def _depart_end(self):
        self._depart_rank()
        self.connecting_i.wait_cleared()
        for _ in range(5):
            try:
                # time.sleep(0.5)  # Sometimes it doesn't find it and fails
                self.b_repeat_i.search(20)
                break
            except ImageException:
                try:
                    self.r_error_ok.search_click()
                    self._depart_rank()
                    self.connecting_i.wait_cleared()
                except ImageException:
                    self.connection_error_i.search_click()
                    self.unit_data_ok_i.search_click()
                    self.connecting_i.wait_cleared()

    def depart(self, use_lapis=True):
        try:
            self.adventure_i.search_click(5)
        except ImageException:
            try:
                self.b_daily_quest_close_i.search_click()
                self.adventure_i.search_click(5)
            except ImageException:
                try:
                    self.adventure_i.search_click(5)
                except ImageException:
                    self.r_friends_ok.search_click(2)
                    self.adventure_i.search_click(5)

        try:
            self.next_i.search_click(3)
        except ImageException:
            if use_lapis:
                self.use_lapis_i.search_click(3)
                self.yes_i.search_click(3)
                self.next_i.search_click(10)
            else:
                raise
        self._depart_end()

    def depart_bonus(self, use_lapis=True):
        self.adventure_i.search_click(3)
        try:
            self.next_i.search_click(3)
        except ImageException:
            if use_lapis:
                self.use_lapis_i.search_click(3)
                self.yes_i.search_click(3)
                self.next_i.search_click(3)
            else:
                raise
        for _ in range(4):
            try:
                self.bonus_i.search(2)
                break
            except ImageException:
                self.next_i.drag(y=-400)
        try:
            self.bonus_i.search_click(3)
        except ImageException:
            self.rank_i.search_click(5)
        self.manage_items_i.search(10)
        self.depart_i.search_click(5)

    def depart_unit(self, unit: str):
        self.adventure_i.search_click(3)
        try:
            self.next_i.search_click(3)
        except ImageException:
            self.use_lapis_i.search_click(3)
            self.yes_i.search_click(3)
            self.next_i.search_click(3)
        unit_i = UnitIs.get(unit)
        unit_i.cache_enable = False
        for _ in range(6):
            try:
                unit_i.search(2)
            except ImageException:
                self.next_i.drag(y=-300)
        unit_i.search_click(3)
        self.manage_items_i.search(10)
        self.depart_i.search_click(5)

    def results(self, gil_search=20):
        self.connecting_i.wait_cleared()
        try:
            self.r_gil_i.search_click(gil_search)
        except ImageException:
            self.r_error_ok.search_click(3)
            self.r_gil_i.search_click(15)
        try:
            self.r_unit_exp.search_click(2)
        except ImageException:
            self.m_crash_ok_i.search_click(2)
            self.cooldown()
            self.r_unit_exp.search_click(2)
        self.r_next.search_click(2)
        self.r_unit_exp_2.search_click_clear(10)  # "Level up" would require 2 clicks
        # self.r_items_obtained.search_click(5)
        self.r_items_obtained.search_click(10)
        self.r_next_2.search_click(10)
        # try:
        #     self.r_dont_request.search_click(2)
        # except ImageException:
        #     pass

    def results_units(self):
        try:
            self.r_gil_i.search_click(10)
        except ImageException:
            self.r_error_ok.search_click(3)
            self.r_gil_i.search_click(10)
        self.cooldown()
        try:
            self.r_unit_exp.search_click(3)
        except ImageException:
            self.m_crash_ok_i.search_click(3)
            self.cooldown()
            self.r_unit_exp.search_click(3)
        self.r_next.search_click(3)
        self.r_unit_exp_2.search_click_clear(10)  # "Level up" would require 2 clicks
        self.r_units_obtained.search_click(5)
        self.r_next_2.search_click(10)
        try:
            self.r_dont_request.search_click(3)
        except ImageException:
            pass

    def results_raid(self):
        try:
            self.r_gil_i.search_click(10)
        except ImageException:
            self.r_error_ok.search_click(3)
            self.r_gil_i.search_click(10)
        self.cooldown()
        try:
            self.r_unit_exp.search_click(2)
            self.r_rank_exp.search_click_clear(2)
        except ImageException:
            pass
        self.r_damage_i.search_click(3)
        self.r_event_pt_i.search_click(3)
        self.r_total_i.search_click(3)
        self.r_total_i.search_click(3)
        self.r_next.search_click(3)

        self.r_unit_exp_2.search_click_clear(10)  # "Level up" would require 2 clicks
        self.r_items_obtained.search_click(10)
        self.r_next_2.search_click(10)
        try:
            self.r_dont_request.search_click(2)
        # except ImageException:
        except Exception:
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
