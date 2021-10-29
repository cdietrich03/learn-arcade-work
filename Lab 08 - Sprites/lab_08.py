import random
import arcade

# Constants
SPRITE_SCALING_ADVENTURER = 0.5
SPRITE_SCALING_KEY = 0.5
SPRITE_SCALING_CACTUS = 0.35
KEY_COUNT = 40
CACTUS_COUNT = 25

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class Cactus(arcade.Sprite):
    # Reset cacti to random position on side of screen
    def reset_pos(self):
        self.center_x = random.randrange(SCREEN_WIDTH + 20, SCREEN_WIDTH + 75)
        self.center_y = random.randrange(SCREEN_HEIGHT)

    # Reset cacti to random position on bottom of screen
    def reset(self):
        self.center_x = random.randrange(SCREEN_WIDTH)
        self.center_y = random.randrange(SCREEN_HEIGHT - 700, SCREEN_HEIGHT - 620)

    # Move diagonally, up and left
    def update(self):
        self.center_x -= 1
        self.center_y += 1

        # If the bottom goes above the top or the right side goes past the screen, reset
        if self.bottom > 600:
            self.reset_pos()
        elif self.right < 0:
            self.reset()


class Key(arcade.Sprite):
    # Reset the key to a random position at the top of the screen
    def reset_pos(self):
        self.center_x = random.randrange(SCREEN_WIDTH)
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)

    # Move the key downwards
    def update(self):
        self.center_y -= 1

        # If key goes past the screen, reset position
        if self.top < 0:
            self.reset_pos()


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

        # Do not show cursor
        self.set_mouse_visible(False)

        self.lose_sound = None

        # Set the background color
        arcade.set_background_color(arcade.color.BABY_BLUE_EYES)

    def setup(self):

        # Create the lists
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

        # When all keys collected with no cacti, print you win
        if self.score == 40:
            arcade.draw_text(f"You Win!", 225, 300, arcade.color.BLACK, 30)

        if len(self.key_list) == 0 and self.score != 40:
            arcade.draw_text(f"Game Over!", 200, 300, arcade.color.BLACK, 30)

            if not self.lose_sound:
                self.lose_sound = arcade.load_sound(":resources:sounds/gameover5.wav")
                arcade.play_sound(self.lose_sound)

        # Put the score in the bottom left corner
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 10, arcade.color.BLACK, 12)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if len(self.key_list) != 0:
            self.adventurer_sprite.center_x = x
            self.adventurer_sprite.center_y = y

    def update(self, delta_time):
        # If the key list is zero then stop moving keys
        if len(self.key_list) != 0:
            self.key_list.update()

        # Check if key collides with adventurer
        keys_hit_list = arcade.check_for_collision_with_list(self.adventurer_sprite, self.key_list)

        # Remove key and add score if hit and play sound
        for key in keys_hit_list:
            key.remove_from_sprite_lists()
            self.score += 1
            key_sound = arcade.load_sound(":resources:sounds/coin2.wav")
            arcade.play_sound(key_sound)

        # If the key list is zero then stop moving cacti
        if len(self.key_list) != 0:
            self.cactus_list.update()

        # Check if cactus collides with adventurer
        cactus_hit_list = arcade.check_for_collision_with_list(self.adventurer_sprite, self.cactus_list)

        # Remove cactus and subtract score if hit
        for cactus in cactus_hit_list:
            cactus.remove_from_sprite_lists()
            self.score -= 1
            cactus_sound = arcade.load_sound(":resources:sounds/hurt3.wav")
            arcade.play_sound(cactus_sound)


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
