"""
Scroll around a large screen.

Artwork from https://kenney.nl and arcade.academy

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""

import random
import arcade

SPRITE_SCALING = 1

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 20

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7

NUMBER_OF_GEMS = 25


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.gem_list = None
        self.score = 0

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("femaleAdventurer_idle (1).png", scale=0.4)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 450
        self.player_list.append(self.player_sprite)

        # The outer boundaries for the outer wall
        for x in range(200, 1200, 64):
            wall = arcade.Sprite("platformPack_tile007.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)
        for x in range(200, 1200, 64):
            wall = arcade.Sprite("platformPack_tile007.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 1246
            self.wall_list.append(wall)
        for y in range(414, 1214, 64):
            wall = arcade.Sprite("platformPack_tile007.png", SPRITE_SCALING)
            wall.center_x = 200
            wall.center_y = y
            self.wall_list.append(wall)
        for y in range(414, 1214, 64):
            wall = arcade.Sprite("platformPack_tile007.png", SPRITE_SCALING)
            wall.center_x = 1160
            wall.center_y = y
            self.wall_list.append(wall)

        # Blocks of 7
        for i in range(7):
            wall = arcade.Sprite("platformPack_tile008.png", SPRITE_SCALING)
            wall.center_x = i * 64 + 328
            wall.center_y = 478
            self.wall_list.append(wall)
        for i in range(7):
            wall = arcade.Sprite("platformPack_tile008.png", SPRITE_SCALING)
            wall.center_x = i * 64 + 712
            wall.center_y = 862
            self.wall_list.append(wall)
        for i in range(7):
            wall = arcade.Sprite("platformPack_tile008.png", SPRITE_SCALING)
            wall.center_x = i * 64 + 264
            wall.center_y = 990
            self.wall_list.append(wall)

        # Blocks of 3
        for i in range(3):
            wall = arcade.Sprite("platformPack_tile008.png", SPRITE_SCALING)
            wall.center_x = i * 64 + 904
            wall.center_y = 478
            self.wall_list.append(wall)
        for i in range(3):
            wall = arcade.Sprite("platformPack_tile008.png", SPRITE_SCALING)
            wall.center_x = i * 64 + 712
            wall.center_y = 606
            self.wall_list.append(wall)
        for i in range(3):
            wall = arcade.Sprite("platformPack_tile008.png", SPRITE_SCALING)
            wall.center_x = i * 64 + 712
            wall.center_y = 862
            self.wall_list.append(wall)
        for i in range(3):
            wall = arcade.Sprite("platformPack_tile008.png", SPRITE_SCALING)
            wall.center_x = i * 64 + 456
            wall.center_y = 798
            self.wall_list.append(wall)

        # Blocks of 2
        for i in range(2):
            wall = arcade.Sprite("platformPack_tile008.png", SPRITE_SCALING)
            wall.center_x = i * 64 + 968
            wall.center_y = 606
            self.wall_list.append(wall)
        for i in range(2):
            wall = arcade.Sprite("platformPack_tile008.png", SPRITE_SCALING)
            wall.center_x = i * 64 + 264
            wall.center_y = 734
            self.wall_list.append(wall)
        for i in range(2):
            wall = arcade.Sprite("platformPack_tile008.png", SPRITE_SCALING)
            wall.center_x = i * 64 + 840
            wall.center_y = 1054
            self.wall_list.append(wall)
        for i in range(2):
            wall = arcade.Sprite("platformPack_tile008.png", SPRITE_SCALING)
            wall.center_x = i * 64 + 264
            wall.center_y = 1118
            self.wall_list.append(wall)

        # Blocks of 5
        for i in range(5):
            wall = arcade.Sprite("platformPack_tile008.png", SPRITE_SCALING)
            wall.center_x = i * 64 + 264
            wall.center_y = 606
            self.wall_list.append(wall)

        # Vertical Wall
        # Blocks of 2
        for i in range(2):
            wall = arcade.Sprite("platformPack_tile008.png", SPRITE_SCALING)
            wall.center_x = 1032
            wall.center_y = i * 64 + 734
            self.wall_list.append(wall)
        for i in range(2):
            wall = arcade.Sprite("platformPack_tile008.png", SPRITE_SCALING)
            wall.center_x = 584
            wall.center_y = i * 64 + 1054
            self.wall_list.append(wall)
        for i in range(2):
            wall = arcade.Sprite("platformPack_tile008.png", SPRITE_SCALING)
            wall.center_x = 712
            wall.center_y = i * 64 + 1118
            self.wall_list.append(wall)

        # Blocks of 3
        for i in range(3):
            wall = arcade.Sprite("platformPack_tile008.png", SPRITE_SCALING)
            wall.center_x = 392
            wall.center_y = i * 64 + 734
            self.wall_list.append(wall)

        # Blocks of 4
        for i in range(4):
            wall = arcade.Sprite("platformPack_tile008.png", SPRITE_SCALING)
            wall.center_x = 968
            wall.center_y = i * 64 + 926
            self.wall_list.append(wall)

            # Place some rocks
            wall = arcade.Sprite("meteorGrey_med1.png", 1.3)
            wall.center_x = 500
            wall.center_y = 541
            self.wall_list.append(wall)

            wall = arcade.Sprite("meteorGrey_med1.png", 1.3)
            wall.center_x = 780
            wall.center_y = 925
            self.wall_list.append(wall)

            wall = arcade.Sprite("meteorGrey_med1.png", 1.3)
            wall.center_x = 454
            wall.center_y = 1053
            self.wall_list.append(wall)

            wall = arcade.Sprite("meteorGrey_med1.png", 1.3)
            wall.center_x = 1096
            wall.center_y = 605
            self.wall_list.append(wall)

            wall = arcade.Sprite("meteorGrey_med1.png", 1.3)
            wall.center_x = 776
            wall.center_y = 734
            self.wall_list.append(wall)

        for x in range(NUMBER_OF_GEMS):
            gem = arcade.Sprite("platformPack_item004.png", 0.6)

            # Boolean variable if we successfully placed the gem
            gem_placed_well = False

            # Keep trying until success
            while not gem_placed_well:
                # Position the gem
                gem.center_x = random.randrange(200, 1200)
                gem.center_y = random.randrange(414, 1150)

                # See if the gem is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(gem, self.wall_list)

                # See if the gem is hitting another gem
                gem_hit_list = arcade.check_for_collision_with_list(gem, self.gem_list)

                if len(wall_hit_list) == 0 and len(gem_hit_list) == 0:
                    # It is!
                    gem_placed_well = True

            # Add the gem to the lists
            self.gem_list.append(gem)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.DARK_GRAY)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.gem_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        output = f"Gems Left: {len(self.gem_list)}"
        arcade.draw_text(output, 10, 30, arcade.color.BLACK, 12)

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 10, arcade.color.BLACK, 12)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        self.gem_list.update()

        gem_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.gem_list)

        for gem in gem_hit_list:
            gem.remove_from_sprite_lists()
            self.score += 1
        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = self.player_sprite.center_x - self.width / 2, self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
