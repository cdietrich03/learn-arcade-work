import random
import arcade

# Constants
SPRITE_SCALING_ADVENTURER = 0.65
SPRITE_SCALING_KEY = 0.5
SPRITE_SCALING_CACTUS = 0.5
KEY_COUNT = 25
CACTUS_COUNT = 25

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class Cactus(arcade.Sprite):
    def reset_pos(self):
        self.center_x = random.randrange(SCREEN_WIDTH)
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)

    def update(self):
        self.center_x -= 1
        self.center_y += 1

        if self.top < 0:
            self.reset_pos()


class Key(arcade.Sprite):
    def reset(self):
        self.center_x = random.randrange(SCREEN_WIDTH)
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)

    def update(self):
        # Moving the key
        self.center_y += 1

        # See if we went off-screen
        if self.top > 600:
            self.reset()


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8 - Sprites")

        # Lists for game
        self.adventurer_list = None
        self.key_list = None
        self.cactus_list = None

        # The adventurer information
        self.adventurer_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BABY_BLUE_EYES)

    def setup(self):

        self.adventurer_list = arcade.SpriteList()
        self.key_list = arcade.SpriteList()
        self.cactus_list = arcade.SpriteList()

        self.score = 0

        # Sprite from the arcade library
        self.adventurer_sprite = arcade.Sprite("femaleAdventurer_idle.png", SPRITE_SCALING_ADVENTURER)
        self.adventurer_sprite.center_x = 300
        self.adventurer_sprite.center_y = 300
        self.adventurer_list.append(self.adventurer_sprite)

        # Make the keys
        for i in range(KEY_COUNT):
            key = Key("keyYellow.png", SPRITE_SCALING_KEY)

            # Position the keys
            key.center_x = random.randrange(SCREEN_WIDTH)
            key.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the key to the list of keys
            self.key_list.append(key)

        for i in range(CACTUS_COUNT):
            cactus = Cactus("cactus.png", SPRITE_SCALING_CACTUS)

            # Position the cacti
            cactus.center_x = random.randrange(SCREEN_WIDTH)
            cactus.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the cactus to the list of cacti
            self.cactus_list.append(cactus)

    def on_draw(self):
        arcade.start_render()

        self.key_list.draw()
        self.adventurer_list.draw()
        self.cactus_list.draw()

        # Put the score in the bottom left corner
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 10, arcade.color.BLACK, 12)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.adventurer_sprite.center_x = x
        self.adventurer_sprite.center_y = y

    def update(self, delta_time):
        self.key_list.update()

        # Check if key collides with adventurer
        keys_hit_list = arcade.check_for_collision_with_list(self.adventurer_sprite, self.key_list)

        # Remove key and add score if hit
        for key in keys_hit_list:
            self.key.reset()
            self.score += 1

        self.cactus_list.update()
        # Check if cactus collides with adventurer
        cactus_hit_list = arcade.check_for_collision_with_list(self.adventurer_sprite, self.cactus_list)

        # Remove cactus and subtract score if hit
        for cactus in cactus_hit_list:
            cactus.remove_from_sprite_lists()
            self.score -= 1


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
