from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        super().main()
        world_i = WorldIs.get("world")
        olderion_i = WorldIs.get("olderion")
        grandshelt_i = WorldIs.get("grandshelt")
        grandshelt_isles_i = WorldIs.get("grandshelt_isles")
        ordol_port_i = WorldIs.get("ordol_port")
        earth_shrine_i = WorldIs.get("earth_shrine")


        menu = Menu()
        dungeon = Dungeon()
        battle = Battle()

        dungeon.adventure_i = DepartureIs.get("1_2")
        # dungeon.adventure_i = DepartureIs.get("15_4")
        while True:
            try:
                dungeon.depart()
                battle.auto()
                dungeon.results()
            except ImageException:
                menu.start()
                i = 0
                for i in range(15):
                    try:
                        menu.play_ok_i.search_click(1)
                    except ImageException:
                        pass
                    try:
                        battle.menu_i.search(1)
                        battle.auto()
                        dungeon.results()
                        break
                    except ImageException:
                        pass
                    try:
                        battle.menu_disabled_i.search(1)
                        dungeon.results()
                        break
                    except ImageException:
                        pass
                    try:
                        world_i.search_click(1)
                        olderion_i.search(5)
                        olderion_i.drag(-200)
                        grandshelt_i.search_click(5)
                        grandshelt_isles_i.search_click(5)
                        ordol_port_i.search(5)
                        ordol_port_i.drag(200)
                        earth_shrine_i.search_click_clear(5)
                        break
                    except ImageException:
                        pass
                    try:
                        dungeon.r_gil_i.search()
                        dungeon.results()
                        break
                    except ImageException:
                        pass
                if i > 13:
                    raise ImageException
if __name__ == '__main__':
    m = Run()
    m.run()
