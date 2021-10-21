""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5


class Moon:
    def __init__(self, position_x, position_y, change_x, change_y):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        # Draw the moon
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y, 30,
                                  arcade.color.DARK_GRAY)

        # Draw the craters
        arcade.draw_circle_filled(5 + self.position_x,
                                  10 + self.position_y, 3,
                                  arcade.color.GRAY,
                                  num_segments=32)
        arcade.draw_circle_filled(15 + self.position_x,
                                  -20 + self.position_y, 3,
                                  arcade.color.GRAY,
                                  num_segments=32)
        arcade.draw_circle_filled(-15 + self.position_x,
                                  -15 + self.position_y, 4,
                                  arcade.color.GRAY,
                                  num_segments=32)
        arcade.draw_circle_filled(-17 + self.position_x,
                                  2 + self.position_y, 5,
                                  arcade.color.GRAY,
                                  num_segments=32)
        arcade.draw_circle_filled(-10 + self.position_x,
                                  17 + self.position_y, 2,
                                  arcade.color.GRAY,
                                  num_segments=32)
        arcade.draw_circle_filled(10 + self.position_x,
                                  3 + self.position_y, 2,
                                  arcade.color.GRAY,
                                  num_segments=32)

    def update(self):
        # Move the moon
        self.position_y += self.change_y
        self.position_x += self.change_x


class House:
    def __init__(self, position_x, position_y, change_x, change_y):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):

        def draw_house(x, y):
            """ Draw the house"""

            # Draw the front
            arcade.draw_lrtb_rectangle_filled(350 + x - 400,
                                              450 + x - 400,
                                              250 + y - 238,
                                              150 + y - 238,
                                              arcade.color.FLATTERY)

            # Draw the roof
            arcade.draw_triangle_filled(340 + x - 400,
                                        250 + y - 238,
                                        460 + x - 400,
                                        250 + y - 238,
                                        400 + x - 400,
                                        325 + y - 238,
                                        arcade.color.BLACK)

            # Draw chimney
            arcade.draw_lrtb_rectangle_filled(415 + x - 400,
                                              435 + x - 400,
                                              330 + y - 238,
                                              275 + y - 238,
                                              arcade.color.GRAY)

            # Draw the door
            arcade.draw_lrtb_rectangle_filled(390 + x - 400,
                                              410 + x - 400,
                                              185 + y - 238,
                                              150 + y - 238,
                                              arcade.color.REDWOOD)

        def draw_window(x, y):
            arcade.draw_lrtb_rectangle_filled(365 + x - 372,
                                              380 + x - 372,
                                              230 + y - 222,
                                              215 + y - 222,
                                              arcade.color.SKY_BLUE)
            arcade.draw_line(372 + x - 372,
                             215 + y - 222,
                             372 + x - 372,
                             231 + y - 222,
                             arcade.color.RED, 1)
            arcade.draw_line(364 + x - 372,
                             222 + y - 222,
                             380 + x - 372,
                             222 + y - 222,
                             arcade.color.RED, 1)

        # Call the window and house function
        draw_house(self.position_x, self.position_y)
        draw_window(self.position_x + 20, self.position_y - 10)
        draw_window(self.position_x - 20, self.position_y - 10)

    def update(self):
        # Move the house
        self.position_y += self.change_y
        self.position_x += self.change_x

        # Check if house hits edge of screen, play sound if does
        if self.position_x > SCREEN_WIDTH - 60:
            self.position_x = SCREEN_WIDTH - 60
            error_sound = arcade.load_sound(":resources:sounds/error1.wav")
            arcade.play_sound(error_sound)

        if self.position_x < 60:
            self.position_x = 60
            error_sound = arcade.load_sound(":resources:sounds/error1.wav")
            arcade.play_sound(error_sound)

        if self.position_y > SCREEN_HEIGHT - 93:
            self.position_y = SCREEN_HEIGHT - 93
            error_sound = arcade.load_sound(":resources:sounds/error1.wav")
            arcade.play_sound(error_sound)

        if self.position_y < 88:
            self.position_y = 88
            error_sound = arcade.load_sound(":resources:sounds/error1.wav")
            arcade.play_sound(error_sound)


def draw_star(x, y):
    """ Draw a star """
    arcade.draw_point(x, y, arcade.color.EGGSHELL, 5)


def draw_pine_tree(x, y):
    """ Draw a pine tree"""

    # Draw the trunk
    arcade.draw_lrtb_rectangle_filled(100 + x - 110,
                                      120 + x - 110,
                                      250 + y - 250,
                                      200 + y - 250,
                                      arcade.color.DARK_SIENNA)

    # Draw the top of tree
    arcade.draw_triangle_filled(85 + x - 110,
                                230 + y - 250,
                                135 + x - 110,
                                230 + y - 250,
                                110 + x - 110,
                                270 + y - 250,
                                arcade.color.DARTMOUTH_GREEN)
    arcade.draw_triangle_filled(85 + x - 110,
                                245 + y - 250,
                                135 + x - 110,
                                245 + y - 250,
                                110 + x - 110,
                                285 + y - 250,
                                arcade.color.DARTMOUTH_GREEN)
    arcade.draw_triangle_filled(85 + x - 110,
                                260 + y - 250,
                                135 + x - 110,
                                260 + y - 250,
                                110 + x - 110,
                                300 + y - 250,
                                arcade.color.DARTMOUTH_GREEN)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.set_mouse_visible(False)

        # Create the house
        self.house = House(100, 100, 0, 0)

        # Create the moon
        self.moon = Moon(50, 50, 0, 0)

    def on_draw(self):
        arcade.start_render()

        # Set the background color
        arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)

        # Draw the ground
        arcade.draw_lrtb_rectangle_filled(0, 600, 200, 0, arcade.color.ENGLISH_GREEN)

        # Calling the functions to draw the background
        draw_star(500, 400)
        draw_star(300, 450)
        draw_star(330, 500)
        draw_star(200, 420)
        draw_star(50, 360)
        draw_star(300, 330)
        draw_star(100, 550)
        draw_star(200, 570)
        draw_star(550, 575)
        draw_star(400, 400)
        draw_star(450, 500)
        draw_pine_tree(100, 200)
        draw_pine_tree(200, 150)
        draw_pine_tree(250, 250)
        draw_pine_tree(300, 175)
        draw_pine_tree(50, 75)
        draw_pine_tree(250, 90)
        draw_pine_tree(450, 90)
        draw_pine_tree(500, 230)
        draw_pine_tree(550, 150)

        # Drawing the moving objects
        self.house.draw()
        self.moon.draw()

    # Moving the moon with the mouse
    def on_mouse_motion(self, x, y, change_x, change_y):
        self.moon.position_x = x
        self.moon.position_y = y

    def update(self, delta_time):
        self.house.update()

    # Moving the house with the arrow keys
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.house.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.house.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.house.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.house.change_y = -MOVEMENT_SPEED

    # When the key is released, stop moving
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.house.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.house.change_y = 0

    # If left mouse button is clicked, play this sound
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            hurt_sound = arcade.load_sound(":resources:sounds/hurt5.wav")
            arcade.play_sound(hurt_sound)


def main():
    window = MyGame()
    arcade.run()


main()
