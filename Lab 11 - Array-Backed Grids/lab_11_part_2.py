import arcade

WIDTH = 20
HEIGHT = 20
MARGIN = 5
COLUMN_COUNT = 10
ROW_COUNT = 10

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.grid = []

        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

    def on_draw(self):
        arcade.start_render()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    color = arcade.color.LIGHT_YELLOW
                else:
                    color = arcade.color.BLUE_BELL

                x = WIDTH / 2 + column * (WIDTH + MARGIN) + MARGIN
                y = HEIGHT / 2 + row * (HEIGHT + MARGIN) + MARGIN

                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        row = y // (HEIGHT + MARGIN)
        column = x // (WIDTH + MARGIN)

        # Flip the location between 1 and 0.
        if self.grid[row][column] == 0:
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = 0

        cell_count = 0
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    cell_count += 1
        print("Total of", cell_count, "cells are selected.")

        for row in range(ROW_COUNT):
            row_num = 0
            continuous_count = 0
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    row_num += 1
                    continuous_count += 1
                else:
                    if continuous_count > 2:
                        print("There are", continuous_count, "continuous blocks selected on row", row)
                        continuous_count = 0

            print("Row", row, "has", row_num, "cells selected.")

        for column in range(COLUMN_COUNT):
            column_num = 0
            for row in range(ROW_COUNT):
                if self.grid[row][column] == 1:
                    column_num += 1

            print("Column", column, "has", column_num, "cells selected.")


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
