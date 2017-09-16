from libs.FFBE import *
from libs.Core import *
# Have on Menu -> Auto continuous battle = False, Auto burst = True


class Main(Executable):
    def __init__(self):
        super().__init__()

    def main(self):
        wifi = Image("libs\\ffbe\\wifi.png")
        wifi.search()
        set_region(wifi.x, wifi.y, wifi.x + 570, wifi.y + 1012)