

# print("Most exciting class ever!!!")
# print("I want to sleep \\\\hi\\\\")
# print("What does\ndo? It\nis weird.")
# print("""Wow
# the professor
# has
# gone
# crazy""")


# ch 11
# 'for loops' - when you know how many times to loop
# 'while loop' - loop until a condition

# i represent increment, can be replaced with any variable


# sentinel variable, teh variable watched until exiting a function
# Running total
# Boolean variables are true and false

# lists use brackets, functions use parenthesis

# Write your function below:


# This is some code you can use to test:


# my_list = [4, 2, 56, 2, 0]
# positive_outlook_list = []
# for item in my_list:
#     if item > 0:
#         positive_outlook_list.append(item)


# print(positive_outlook_list)


""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

    def on_draw(self):
        arcade.start_render()


def main():
    """ Main method """
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()