"""
    2048控制台界面
"""

from bll import GameCoreController
from model import Direction
import os

class GameConsoleView:
    def __init__(self):
        self.__game_core_controller = GameCoreController()

    def main(self):
        self.__start()
        self.__update()

    def __start(self):
        self.__game_core_controller.generate_random_map()
        self.__game_core_controller.generate_random_map()
        self.__draw_map()

    def __draw_map(self):
        os.system("clear")
        for line in self.__game_core_controller.map_move:
            for item in line:
                print(item,end = " ")
            print()

    def __update(self):
        while True:
            self.__move_map_for_input()
            self.__game_core_controller.generate_random_map()
            self.__draw_map()
            if self.__game_core_controller.is_game_over():
                print("GAME OVER")
                break

    def __move_map_for_input(self):
        dir = input("请输入方向（ｗ，ｓ，ａ，ｄ）：")
        dict_dir = {
            "w":Direction.UP,
            "s":Direction.DOWN,
            "a":Direction.LEFT,
            "d":Direction.RIGHT
        }
        if dir in dict_dir:
            self.__game_core_controller.move(dict_dir[dir])





if __name__ == "__main__":
    game_console_view = GameConsoleView()
    game_console_view.main()
