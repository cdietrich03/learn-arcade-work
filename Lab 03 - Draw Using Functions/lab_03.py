"""
This is a program to show how to draw using the Python programming
language and drawing with functions
"""

# Import the "arcade" library
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground"""
    arcade.draw_lrtb_rectangle_filled(0, 600, 200, 0, arcade.color.ENGLISH_GREEN)


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


def draw_smoke():
    arcade.draw_circle_filled(435, 335, 8, arcade.color.DARK_GRAY, num_segments=32)
    arcade.draw_circle_filled(440, 340, 8, arcade.color.DARK_GRAY, num_segments=32)
    arcade.draw_circle_filled(450, 350, 8, arcade.color.DARK_GRAY, num_segments=32)
    arcade.draw_circle_filled(465, 355, 5, arcade.color.DARK_GRAY, num_segments=32)


def draw_window(x, y):
    arcade.draw_lrtb_rectangle_filled(365 + x - 372, 380 + x - 372, 230 + y - 222, 215 + y - 222, arcade.color.SKY_BLUE)
    arcade.draw_line(372 + x - 372, 215 + y - 222, 372 + x - 372, 231 + y - 222, arcade.color.RED, 1)
    arcade.draw_line(364 + x - 372, 222 + y - 222, 380 + x - 372, 222 + y - 222, arcade.color.RED, 1)


def draw_walkway():
    """ Draw the walkway"""
    arcade.draw_polygon_filled(((300, 0),
                                (400, 0),
                                (390, 150),
                                (410, 150),
                                (390, 150)),
                               arcade.color.DESERT)


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


def draw_moon():
    """ Draw the moon """

    # Draw moon
    arcade.draw_circle_filled(100, 500, 30, arcade.color.DARK_GRAY)

    # Draw the craters
    arcade.draw_circle_filled(105, 504, 3, arcade.color.GRAY, num_segments=32)
    arcade.draw_circle_filled(87, 490, 3, arcade.color.GRAY, num_segments=32)
    arcade.draw_circle_filled(107, 483, 4, arcade.color.GRAY, num_segments=32)
    arcade.draw_circle_filled(90, 520, 5, arcade.color.GRAY, num_segments=32)
    arcade.draw_circle_filled(110, 520, 2, arcade.color.GRAY, num_segments=32)
    arcade.draw_circle_filled(120, 500, 2, arcade.color.GRAY, num_segments=32)


def draw_star(x, y):
    """ Draw a star """
    arcade.draw_point(x, y, arcade.color.EGGSHELL, 5)


def main():
    # Open up a window.
    # From the "arcade" library, use a function called "open_window"
    # Set the dimensions (width and height)
    arcade.open_window(600, 600, "House")

    # Set the background color
    arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)

    # Get ready to draw
    arcade.start_render()

    draw_grass()
    draw_house(400, 238)
    draw_walkway()
    draw_moon()
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
    draw_window(372, 222)
    draw_window(427, 222)
    draw_smoke()

    # Finish the drawing
    arcade.finish_render()

    # Keep the window open until someone closes it.
    arcade.run()


# call the main function to get the program started.
main()
