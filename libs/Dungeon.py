from libs.FFBE import *


class Departure(Base):

    def __init__(self):
        super().__init__()
        self.img_set = Images("png\\ffbe\\departure\\%s.png")

        self.adventure_i = self.img_set.get("elt")

        self.next_i = self.img_set.get("next")
        self.use_lapis_i = self.img_set.get("use_lapis")
        self.yes_i = self.img_set.get("yes")

        self.rank_i = self.img_set.get("rank")
        self.manage_items_i = self.img_set.get("manage_items")
        self.depart_i = self.img_set.get("depart")

        self.bonus_i = self.img_set.get("bonus")

        self.unit_data_i = self.img_set.get("unit_data")
        self.unit_data_ok_i = self.img_set.get("unit_data_ok")
        self.connection_error_i = self.img_set.get("connection_error")
        self.connecting_i = self.img_set.get("connecting")

        self.daily_quest_close_i = self.img_set.get("daily_quest_close")

    def _depart_rank(self):
        self.rank_i.search_click(10)
        self.manage_items_i.search(10)
        self.depart_i.search_click(5)

    def depart(self, use_lapis=True):
        try:
            self.adventure_i.search_click(5)
        except ImageException:
            self.daily_quest_close_i.search_click()
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
        self._depart_rank()
        self.connecting_i.wait_cleared()

    def bonus(self):
        pass

    def vortex(self):
        pass

    def raid(self):
        pass


class Results(object):
    pass

