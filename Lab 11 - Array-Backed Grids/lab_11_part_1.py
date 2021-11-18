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

        print(self.grid)

    def on_draw(self):
        """
        Render the screen.
        """

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

        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        print(column, row)

        if row < ROW_COUNT and column < COLUMN_COUNT:

            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0

            if (row + 1) < ROW_COUNT:
                if self.grid[row + 1][column] == 0:
                    self.grid[row + 1][column] = 1
                else:
                    self.grid[row + 1][column] = 0
            if (column + 1) < COLUMN_COUNT:
                if self.grid[row][column + 1] == 0:
                    self.grid[row][column + 1] = 1
                else:
                    self.grid[row][column + 1] = 0
            if (row - 1) > 0:
                if self.grid[row - 1][column] == 0:
                    self.grid[row - 1][column] = 1
                else:
                    self.grid[row - 1][column] = 0

            if (column - 1) > 0:
                if self.grid[row][column - 1] == 0:
                    self.grid[row][column - 1] = 1
                else:
                    self.grid[row][column - 1] = 0


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
