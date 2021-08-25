import copy

import arcade

from constants import (SCREEN_HEIGHT, SCREEN_WIDTH, TITLE)
from utils import (create_grid, create_cell_list,
                   update_cell_list)

EMPTY = arcade.color.WHITE
FILLED = arcade.color.RED


class GameOfLife(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.shape_grid = self.cell_list_first = self.cell_list_second = None
        self.cell_list = create_cell_list()
        self.update_grid()

    def on_draw(self):
        arcade.start_render()
        self.shape_grid.draw()

    def update_grid(self):
        self.cell_list_first = copy.deepcopy(self.cell_list)
        self.cell_list_second = copy.deepcopy(self.cell_list)
        self.shape_grid = create_grid(self.cell_list)

    def on_update(self, delta_time: float):
        self.cell_list = update_cell_list(self.cell_list_first,
                                          self.cell_list_second)
        self.update_grid()


def main():
    GameOfLife(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
