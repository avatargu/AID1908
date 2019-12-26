"""
    游戏逻辑控制器，负责处理游戏核心算法．
"""

from model import Direction
from model import Coordinate
from random import randrange
from random import choice

class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map_move = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]
        self.__list_zero_coordinates = []

    @property
    def map_move(self):
        return self.__map_move

    def __zeros_to_end(self):
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        self.__zeros_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def __generate_random_number(self):
        random_number = randrange(10)
        return 4 if random_number == 0 else 2

    def __get_zero_coordinates(self):
        self.__list_zero_coordinates.clear()
        for r in range(len(self.__map_move)):
            for c in range(len(self.__map_move[r])):
                if self.__map_move[r][c] == 0:
                    self.__list_zero_coordinates.append(Coordinate(r,c))

    def __generate_random_coordinate(self):
        self.__get_zero_coordinates()
        return choice(self.__list_zero_coordinates) if len(self.__list_zero_coordinates) > 0 else None

    def generate_random_map(self):
        random_coordinate = self.__generate_random_coordinate()
        if random_coordinate != None:
            self.__map_move[random_coordinate.row_index][random_coordinate.column_index] \
                = self.__generate_random_number()
            self.__list_zero_coordinates.remove(random_coordinate)

    def __move_left(self):
        for line in self.__map_move:
            self.__list_merge = line
            self.__merge()

    def __move_right(self):
        for line in self.__map_move:
            self.__list_merge = line
            self.__list_merge.reverse()
            self.__merge()
            self.__list_merge.reverse()

    def __transpose(self):
        for row in range(len(self.__map_move) - 1):
            for column in range(row + 1, len(self.__map_move)):
                self.__map_move[row][column], self.__map_move[column][row] \
                    = self.__map_move[column][row], self.__map_move[row][column]

    def __move_up(self):
        self.__transpose()
        self.__move_left()
        self.__transpose()

    def __move_down(self):
        self.__transpose()
        self.__move_right()
        self.__transpose()

    def move(self,direction):
        if direction == Direction.UP:
            self.__move_up()
        elif direction == Direction.DOWN:
            self.__move_down()
        elif direction == Direction.LEFT:
            self.__move_left()
        elif direction == Direction.RIGHT:
            self.__move_right()

    def is_game_over(self):
        if len(self.__list_zero_coordinates) == 0:
            for r in range(len(self.__map_move)):
                for c in range(len(self.__map_move[r]) - 1):
                    if self.__map_move[r][c] == self.__map_move[r][c + 1] \
                            or self.__map_move[c][r] == self.__map_move[c + 1][r]:
                        return False
            return True
        return False

if __name__ == "__main__":
    direction_model = Direction()
    game_core_controller = GameCoreController()
    print(game_core_controller.map_move)
    game_core_controller.move(Direction.LEFT)
    print(game_core_controller.map_move)
    print(game_core_controller.is_game_over())

