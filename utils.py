import random

import arcade

from constants import (COLUMN_COUNT, HEIGHT, MARGIN, ROW_COUNT, WIDTH)
from cell_strategy import mutation_context

EMPTY = arcade.color.WHEAT
FILLED = arcade.color.RED


def create_cell_list() -> list:
    """
    Generate random 2-dim list with alive or dead cells
    :return: list
    """

    list_representation = []

    for _ in range(ROW_COUNT):
        column_repr = []
        for _ in range(COLUMN_COUNT):
            random_int = random.randrange(2)
            label = 1 if random_int >= 1 else 0
            column_repr.append(label)
        list_representation.append(column_repr)

    return list_representation


def create_grid(list_representation: list) -> arcade.SpriteList:
    """
    Create grid with generated above 2-dim list

    :param list_representation: cells 2-dim list
    :return: SpriteList
    """

    grid = arcade.SpriteList()

    for row_index, row in enumerate(list_representation):
        for value_index, value in enumerate(row):
            x_coord = (MARGIN + WIDTH) * value_index + MARGIN + WIDTH // 2
            y_coord = (MARGIN + HEIGHT) * row_index + MARGIN + HEIGHT // 2
            color = FILLED if value else EMPTY

            circle = arcade.SpriteCircle(WIDTH // 2, color)
            circle.center_x = x_coord
            circle.center_y = y_coord

            grid.append(circle)

    return grid


def neighborhood_color(list_, row, column) -> bool:
    """
    Retrieve neighborhood color, if exists
    If not - return false, for simplifying

    :param list_: cell list
    :param row: int index
    :param column: int index
    :return: int 1\0 status (True or False in bool)
    """

    if row < 0 or column < 0:
        return False
    if row + 1 >= ROW_COUNT or column + 1 >= COLUMN_COUNT:
        return False

    return list_[row][column]


def update_cell_list(old: list, new: list) -> list:
    """
    Get cells list, both are same list
    To keep consistency - updates should be only in "new" list

    :param old: list
    :param new: list
    :return: list
    """

    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            upper = neighborhood_color(old, row - 1, column)
            lower = neighborhood_color(old, row + 1, column)

            left = neighborhood_color(old, row, column - 1)
            right = neighborhood_color(old, row, column + 1)

            upper_left = neighborhood_color(old, row - 1, column - 1)
            upper_right = neighborhood_color(old, row - 1, column + 1)

            lower_left = neighborhood_color(old, row + 1, column - 1)
            lower_right = neighborhood_color(old, row + 1, column + 1)

            neighborhood_count = sum((upper, lower, left, right, upper_left,
                                      upper_right, lower_left, lower_right))

            mutated = mutation_context(old[row][column], neighborhood_count)

            if mutated is None:
                mutated = old[row][column]

            new[row][column] = mutated

    return new
