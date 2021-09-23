"""
This is a program to show how to draw using the Python programming
language and the Arcade library
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "House")

# Set the background color
arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 600, 200, 0, arcade.color.ENGLISH_GREEN)

# Draw the house

# Draw the front
arcade.draw_lrtb_rectangle_filled(350, 450, 250, 150, arcade.color.FLATTERY)

# Draw the roof
arcade.draw_triangle_filled(340, 250, 460, 250, 400, 325, arcade.color.BLACK)

# Draw chimney
arcade.draw_lrtb_rectangle_filled(415, 435, 330, 275, arcade.color.GRAY)

# Draw smoke
arcade.draw_circle_filled(435, 335, 8, arcade.color.DARK_GRAY)
arcade.draw_circle_filled(440, 340, 8, arcade.color.DARK_GRAY)
arcade.draw_circle_filled(450, 350, 8, arcade.color.DARK_GRAY)

# Draw the door
arcade.draw_lrtb_rectangle_filled(390, 410, 185, 150, arcade.color.REDWOOD)

# Draw the windows
arcade.draw_lrtb_rectangle_filled(365, 380, 230, 215, arcade.color.SKY_BLUE)
arcade.draw_lrtb_rectangle_filled(420, 435, 230, 215, arcade.color.SKY_BLUE)

# Draw walkway
arcade.draw_polygon_filled(((300, 0),
                            (400, 0),
                            (390, 150),
                            (410, 150),
                            (390, 150)),
                           arcade.color.DESERT)

# Draw tree trunks
arcade.draw_lrtb_rectangle_filled(100, 120, 250, 200, arcade.color.DARK_SIENNA)
arcade.draw_lrtb_rectangle_filled(170, 190, 250, 200, arcade.color.DARK_SIENNA)
arcade.draw_lrtb_rectangle_filled(240, 260, 250, 200, arcade.color.DARK_SIENNA)
arcade.draw_lrtb_rectangle_filled(500, 520, 250, 200, arcade.color.DARK_SIENNA)

# Draw tree leaves
arcade.draw_circle_filled(110, 270, 30, arcade.color.DARTMOUTH_GREEN)
arcade.draw_circle_filled(180, 270, 30, arcade.color.DARTMOUTH_GREEN)
arcade.draw_circle_filled(250, 270, 30, arcade.color.DARTMOUTH_GREEN)
arcade.draw_triangle_filled(485, 225, 535, 225, 510, 300, arcade.color.DARTMOUTH_GREEN)

# Draw the moon
arcade.draw_circle_filled(100, 500, 30, arcade.color.DARK_GRAY)
arcade.draw_circle_filled(105, 504, 6, arcade.color.GRAY)
arcade.draw_circle_filled(87, 490, 6, arcade.color.GRAY)
arcade.draw_circle_filled(107, 483, 6, arcade.color.GRAY)
arcade.draw_circle_filled(90, 520, 6, arcade.color.GRAY)
arcade.draw_circle_filled(115, 520, 6, arcade.color.GRAY)

# Finish the drawing
arcade.finish_render()

# Keep the window open until someone closes it.
arcade.run()
