

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


# Import functions into 'my_functions' namespace

# Start - sorting wks example - selection sort
# 15 57 14 33 72 79 26 56 42 40

# 14 is smallest, swap 14 to pos 0
# 14 57 33 72 79 26 56 42 40

# 15 is next smallest, swap 15 to pos 1
# 14 15 57 33 72 79 26 56 42 40

# 26 is next smallest, swap 26 to pos 2
# 14 15 26 33 72 79 57 56 42 40

# n = 10, 10 * 5 = 50
# n = 100, 100 * 50 = 5000
# n = 1000, 1000 * 500 = 500000
# n * (n/2) = n^2 / 2

# import random
# import arcade
#
# SPRITE_SCALING = 0.5
#
# DEFAULT_SCREEN_WIDTH = 800
# DEFAULT_SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"
#
# # How many pixels to keep as a minimum margin between the character
# # and the edge of the screen.
# VIEWPORT_MARGIN = 220
#
# # How fast the camera pans to the player. 1.0 is instant.
# CAMERA_SPEED = 0.1
#
# # How fast the character moves
# PLAYER_MOVEMENT_SPEED = 7
#
# TEXTURE_LEFT = 0
# TEXTURE_RIGHT = 1
# TEXTURE_STRAIGHT = 2
# BEE_COUNT = 30
# GEM_COUNT = 30
#
#
# class Bee(arcade.Sprite):
#     def __init__(self, filename, sprite_scaling):
#
#         super().__init__(filename, sprite_scaling)
#         # self.scale = 0.2
#         # self.textures = []
#         #
#         # texture = arcade.load_texture("bee.png", 0.2)
#         # self.textures.append(texture)
#         #
#         # texture = arcade.load_texture("bee.png", 0.2, flipped_horizontally=True)
#         # self.textures.append(texture)
#         #
#         # self.texture = texture
#
#         self.change_x = 0
#         self.change_y = 0
#
#     def update(self):
#         self.center_x += self.change_x
#         self.center_y += self.change_y
#
#         # if self.change_x < 0:
#         #     self.texture = self.textures[TEXTURE_LEFT]
#         # elif self.change_x > 0:
#         #     self.texture = self.textures[TEXTURE_RIGHT]
#
#         # If we are out-of-bounds, then 'bounce'
#         # if self.left < 0:
#         #     self.change_x *= -1
#         #
#         # if self.right > 1856:
#         #     self.change_x *= -1
#
#
# class MyGame(arcade.Window):
#     """ Main application class. """
#
#     def __init__(self, width, height, title):
#         """
#         Initializer
#         """
#         super().__init__(width, height, title, resizable=True)
#
#         # Sprite lists
#         self.player_list = None
#         self.wall_list = None
#         self.gem_list = None
#         self.bee_list = None
#         self.score = 0
#         self.game_over = False
#
#         # Set up the player
#         self.player_sprite = None
#         self.bee_sprite = None
#
#         # Physics engine so we don't run into walls.
#         self.physics_engine = None
#
#         # Create the cameras. One for the GUI, one for the sprites.
#         # We scroll the 'sprite world' but not the GUI.
#         self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
#         self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
#
#     def setup(self):
#         """ Set up the game and initialize the variables. """
#
#
#         # Sprite lists
#         self.player_list = arcade.SpriteList()
#         self.wall_list = arcade.SpriteList()
#         self.gem_list = arcade.SpriteList()
#         self.bee_list = arcade.SpriteList()
#
#         # Set up the player
#         self.player_sprite = arcade.Sprite("alienPink_front.png", scale=0.3)
#         self.player_sprite.center_x = 100
#         self.player_sprite.center_y = 100
#         self.player_list.append(self.player_sprite)
#
#         map_name = "Final.json"
#         self.tile_map = arcade.load_tilemap(map_name, scaling=SPRITE_SCALING)
#
#         self.wall_list = self.tile_map.sprite_lists["walls"]
#
#         for i in range(BEE_COUNT):
#             bee = Bee("bee.png", sprite_scaling=0.2)
#             bee_placed_successfully = False
#
#             # Keep trying until success
#             while not bee_placed_successfully:
#
#                 bee.center_x = random.randrange(64, 1856)
#                 bee.center_y = random.randrange(64, 1856)
#                 bee.change_x = 5
#                 bee.change_y = 0
#
#                 wall_hit_list = arcade.check_for_collision_with_list(bee, self.wall_list)
#
#                 # See if the coin is hitting another coin
#                 bee_hit_list = arcade.check_for_collision_with_list(bee, self.bee_list)
#
#                 if len(wall_hit_list) == 0 and len(bee_hit_list) == 0:
#                     # It is!
#                     bee_placed_successfully = True
#
#         # if bee.right > 1152:
#         #     bee.change_x *= -1
#         # if bee.left < 832:
#         #     bee.change_x *= -1
#             self.bee_list.append(bee)
#
#
#         for i in range(GEM_COUNT):
#
#
#         if self.tile_map.background_color:
#             arcade.set_background_color(self.tile_map.background_color)
#
#
#         self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
#                                                              self.wall_list,
#                                                              gravity_constant=0.5)
#
#         # Set the background color
#
#     def on_draw(self):
#         """
#         Render the screen.
#         """
#
#         # This command has to happen before we start drawing
#         arcade.start_render()
#
#         # Select the camera we'll use to draw all our sprites
#         self.camera_sprites.use()
#
#         # Draw all the sprites.
#         self.wall_list.draw()
#         self.player_list.draw()
#         self.gem_list.draw()
#         self.bee_list.draw()
#
#         # Select the (unscrolled) camera for our GUI
#         self.camera_gui.use()
#
#     def on_key_press(self, key, modifiers):
#         """Called whenever a key is pressed. """
#
#         if key == arcade.key.UP:
#             if self.physics_engine.can_jump():
#                 self.player_sprite.change_y = 12
#
#         elif key == arcade.key.LEFT:
#             self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
#         elif key == arcade.key.RIGHT:
#             self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
#
#     def on_key_release(self, key, modifiers):
#         """Called when the user releases a key. """
#
#         if key == arcade.key.UP or key == arcade.key.DOWN:
#             self.player_sprite.change_y = 0
#         elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
#             self.player_sprite.change_x = 0
#
#     def on_update(self, delta_time):
#         """ Movement and game logic """
#
#         # Call update on all sprites (The sprites don't do much in this
#         # example though.)
#
#         if not self.game_over:
#             self.physics_engine.update()
#
#             if len(arcade.check_for_collision_with_list(self.player_sprite, self.bee_list)) > 0:
#                 self.game_over = True
#
#             self.bee_list.update()
#
#             for bee in self.bee_list:
#                 # If the enemy hit a wall, reverse
#                 if len(arcade.check_for_collision_with_list(bee, self.wall_list)) > 0:
#                     bee.change_x *= -1
#                 # If the enemy hit the left boundary, reverse
#                 elif bee.boundary_left is not None and bee.left < bee.boundary_left:
#                     bee.change_x *= -1
#                 # If the enemy hit the right boundary, reverse
#                 elif bee.boundary_right is not None and bee.right > bee.boundary_right:
#                     bee.change_x *= -1
#
#             # Scroll the screen to the player
#             self.scroll_to_player()
#
#
#     def scroll_to_player(self):
#         """
#         Scroll the window to the player.
#         if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
#         Anything between 0 and 1 will have the camera move to the location with a smoother
#         pan.
#         """
#
#         position = self.player_sprite.center_x - self.width / 2, \
#             self.player_sprite.center_y - self.height / 2
#         self.camera_sprites.move_to(position, CAMERA_SPEED)
#
#     def on_resize(self, width, height):
#         """
#         Resize window
#         Handle the user grabbing the edge and resizing the window.
#         """
#         self.camera_sprites.resize(int(width), int(height))
#         self.camera_gui.resize(int(width), int(height))
#
#
# def main():
#     """ Main function """
#     window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
#     window.setup()
#     arcade.run()
#
#
# if __name__ == "__main__":

# my_list = [70, 32, 98, 88, 92, 36, 81, 83, 87, 66]
# temp = my_list[0]
# my_list[1] = my_list[0]
# my_list[0] = temp
#
#
# print(my_list)

"""
Platformer Game
"""
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 10
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

# Player starting position
PLAYER_START_X = 64
PLAYER_START_Y = 225

# Layer Names from our TileMap
LAYER_NAME_PLATFORMS = "Platforms"
LAYER_NAME_COINS = "Coins"
LAYER_NAME_FOREGROUND = "Foreground"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_DONT_TOUCH = "Don't Touch"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Our TileMap Object
        self.tile_map = None

        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # A Camera that can be used for scrolling the screen
        self.camera = None

        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        # Keep track of the score
        self.score = 0

        # Where is the right edge of the map?
        self.end_of_map = 0

        # Level
        self.level = 1

        # Load sounds
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.game_over = arcade.load_sound(":resources:sounds/gameover1.wav")

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Setup the Cameras
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)

        # Map name
        map_name = f":resources:tiled_maps/map2_level_{self.level}.json"

        # Layer Specific Options for the Tilemap
        layer_options = {
            LAYER_NAME_PLATFORMS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_COINS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_DONT_TOUCH: {
                "use_spatial_hash": True,
            },
        }

        # Load in TileMap
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        # Initiate New Scene with our TileMap, this will automatically add all layers
        # from the map as SpriteLists in the scene in the proper order.
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Keep track of the score
        self.score = 0

        # Add Player Spritelist before "Foreground" layer. This will make the foreground
        # be drawn after the player, making it appear to be in front of the Player.
        # Setting before using scene.add_sprite allows us to define where the SpriteList
        # will be in the draw order. If we just use add_sprite, it will be appended to the
        # end of the order.
        self.scene.add_sprite_list_before("Player", LAYER_NAME_FOREGROUND)

        # Set up the player, specifically placing it at these coordinates.
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.scene.add_sprite("Player", self.player_sprite)

        # --- Load in a map from the tiled editor ---

        # Calculate the right edge of the my_map in pixels
        self.end_of_map = self.tile_map.width * GRID_PIXEL_SIZE

        # --- Other stuff
        # Set the background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            gravity_constant=GRAVITY,
            walls=self.scene[LAYER_NAME_PLATFORMS],
        )

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        arcade.start_render()

        # Activate the game camera
        self.camera.use()

        # Draw our Scene
        self.scene.draw()

        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()

        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(
            score_text,
            10,
            10,
            arcade.csscolor.BLACK,
            18,
        )

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

        # See if we hit any coins
        coin_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene[LAYER_NAME_COINS]
        )

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            # Remove the coin
            coin.remove_from_sprite_lists()
            # Play a sound
            arcade.play_sound(self.collect_coin_sound)
            # Add one to the score
            self.score += 1

        # Did the player fall off the map?
        if self.player_sprite.center_y < -100:
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y

            arcade.play_sound(self.game_over)

        # Did the player touch something they should not?
        if arcade.check_for_collision_with_list(
            self.player_sprite, self.scene[LAYER_NAME_DONT_TOUCH]
        ):
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y

            arcade.play_sound(self.game_over)

        # See if the user got to the end of the level
        if self.player_sprite.center_x >= self.end_of_map:
            # Advance to the next level
            self.level += 1

            # Load the next level
            self.setup()

        # Position the camera
        self.center_camera_to_player()


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()