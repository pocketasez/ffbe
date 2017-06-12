from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):

    def __init__(self):
        super().__init__()
        self.battle = Battle()
        self.arena = Arena()

    def main(self):
        dungeon_img = Image("png\\ffbe\\dungeon\\elt.png")
        next_img = Image("png\\ffbe\\dungeon\\next.png")
        manage_items_img = Image("png\\ffbe\\dungeon\\manage_items.png")
        depart_img = Image("png\\ffbe\\dungeon\\depart.png")

        orlandeau_img = Image("png\\ffbe\\unit\\orlandeau.png")

        end_img = DungeonImage("end")
        gil_img = DungeonImage("gil")
        unit_img = DungeonImage("unit")
        rank_exp_img = DungeonImage("rank_exp")

        damage_img = DungeonImage("damage")
        event_pt_img = DungeonImage("event_pt")
        total_img = DungeonImage("total")
        results_next_img = DungeonImage("results_next")

        unit_exp_img = DungeonImage("unit_exp")

        items_next_img = DungeonImage("items_next")

        self.memu.taskbar_pin_img.search_click()
        try:
            while True:
                dungeon_img.search_click(3)
                next_img.search_click(3)
                for _ in range(4):
                    try:
                        orlandeau_img.search(2)
                        break
                    except ImageException:
                        next_img.drag(y=-400)
                orlandeau_img.search_click(2)
                manage_items_img.search(5)
                depart_img.search_click(3)

                self.battle.setup()
                self.battle.ability(0, -400, "focus", 0)
                self.battle.ability(1, -300, "blizzard_flask")
                self.battle.ability(2, -320, "omni_veil", 2)
                self.battle.ability(3, -400, "embolden", 3)
                self.battle.ability(4, -350, "blizzard_flask")
                self.battle.ability(5, 0, "divine_ruination")
                self.battle.engage(0)
                self.battle.engage(2)
                self.battle.engage(3)
                self.battle.engage(4)
                self.battle.engage(1)
                self.battle.engage(5)
                self.battle.cooldown()

                self.battle.setup()
                self.battle.guard(0)
                self.battle.guard(3)
                self.battle.ability(2, -200, "barrage")
                self.battle.engage(0)
                self.battle.engage(3)
                self.battle.engage(2)
                self.battle.repeat()

                try:
                    self.battle.setup()
                    self.battle.dual_ability(3, "dualcast", -400, 300, "curaja", 3)
                    self.battle.engage(3)
                    self.battle.repeat()

                    for _ in range(5):
                        self.battle.repeat()

                except ImageException:
                    end_img.search_click(40)
                    gil_img.search_click(40)
                    unit_img.search_click(3)
                    rank_exp_img.search_click(10)

                    damage_img.search_click(3)
                    event_pt_img.search_click(3)
                    total_img.search_click(3)
                    total_img.search_click(3)
                    results_next_img.search_click(20)

                    unit_exp_img.search_click(3)
                    items_next_img.search_click_clear(3)
        except ImageException:
            screenshot_ts()


if __name__ == '__main__':
    m = Run()
    m.run()
