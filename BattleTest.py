from Main import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Run(Main):
    def main(self):
        i = Image("libs\\ffbe\\results\\results.png")
        for a in range(30):
            i.search_click()
        # test.search_click(3)

if __name__ == '__main__':
    m = Run()
    m.run()
