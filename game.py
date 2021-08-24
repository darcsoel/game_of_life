import copy
import random

import arcade

TITLE = 'Game of Life'
ROW_COUNT = 15
COLUMN_COUNT = 15
WIDTH = 30
HEIGHT = 30
MARGIN = 5

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

EMPTY = arcade.color.WHITE
FILLED = arcade.color.RED


def create_grid():
    grid = arcade.SpriteList()

    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
            y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
            random_int = random.randrange(5)

            color = FILLED if random_int > 3 else EMPTY

            circle = arcade.SpriteCircle(WIDTH // 2, color)
            circle.center_x = x
            circle.center_y = y

            grid.append(circle)

    return grid


def neighborhood_color(grid, row, column):
    if row < 0 or column < 0:
        return None
    return grid[row * column].color


def update_grid(grid):
    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            neighborhood_count = 0

            upper = neighborhood_color(grid, row - 1, column)
            lower = neighborhood_color(grid, row + 1, column)

            left = neighborhood_color(grid, row, column - 1)
            right = neighborhood_color(grid, row, column + 1)

            upper_left = neighborhood_color(grid, row - 1, column - 1)
            upper_right = neighborhood_color(grid, row - 1, column + 1)

            lower_left = neighborhood_color(grid, row + 1, column - 1)
            lower_right = neighborhood_color(grid, row + 1, column + 1)

            if row > 0 and grid[(row * column) + 1].color == FILLED:
                neighborhood_count += 1

    return grid


class GameOfLife(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.even_iteration = False
        self.shape_list_first = create_grid()
        self.shape_list_second = copy.deepcopy(self.shape_list_first)

    def on_draw(self):
        arcade.start_render()
        self.shape_list_first.draw()

    def on_update(self, delta_time: float):
        if not self.even_iteration:
            grid = update_grid(self.shape_list_first)
        else:
            grid = update_grid(self.shape_list_second)

        self.even_iteration = not self.even_iteration


def main():
    GameOfLife(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
