from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        taskbar_pin_i = Image("png\\memu\\taskbar_pin.png")
        # taskbar_pin_i.search_click()
        dungeon = Dungeon()
        dungeon.r_gil_i.search()
        # test.search_click(3)

if __name__ == '__main__':
    m = Run()
    m.run()
