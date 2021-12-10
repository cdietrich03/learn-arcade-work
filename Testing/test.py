

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



# Create game where win if get to top and try to win quickest, more enemies spawn over time
# reach gold star in top right corner
# Need winning music, need losing music, background music, sound win jump, sound when hit star, sound when hit bee

import random
import arcade

SPRITE_SCALING = 0.5

DEFAULT_SCREEN_WIDTH = 600
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Alien Dash"

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7

# Amount of bees spawned at one time
BEE_COUNT = 7
#
# done = False


# Menu view for the screen
class Menu(arcade.View):

    def on_show(self):
        arcade.set_background_color(arcade.color.BANGLADESH_GREEN)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Alien Dash", 130, 300, arcade.color.WHITE, 50)
        arcade.draw_text("Click for instructions", 190, 270, arcade.color.WHITE_SMOKE, 15)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # When the screen is pressed, move to instruction screen
        instructions = Instructions()
        self.window.show_view(instructions)


# Instructions for the game
class Instructions(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions", 140, 400, arcade.color.BLACK, 50)
        arcade.draw_text("Jump to the top of the game as quickly as possible.", 60, 310, arcade.color.DARK_GRAY, 15)
        arcade.draw_text("Do not touch any bees along the way.", 120, 275, arcade.color.DARK_GRAY, 15)
        arcade.draw_text("As time continues, more bees will spawn.", 105, 250, arcade.color.DARK_GRAY, 15)
        arcade.draw_text("Use the arrow keys to move around.", 125, 225, arcade.color.DARK_GRAY, 15)
        arcade.draw_text("Hit the gold star in order to win the game.", 105, 200, arcade.color.DARK_GRAY, 15)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # After click, move to the game view
        game = MyGame()
        game.setup()
        self.window.show_view(game)


# Create the bee sprite
class Bee(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


# The game view
class MyGame(arcade.View):

    def __init__(self):
        super().__init__()

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.star_list = None
        self.bee_list = None
        self.game_over = False
        self.tile_map = None

        # For the timer
        self.total_time = 0.0
        self.output = "00:00:00"

        # Set up the player
        self.player_sprite = None
        self.bee_sprite = None
        self.spawn_new_enemy_timer = 0

        self.level = 1
        self.max_level = 2

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()
        self.bee_list = arcade.SpriteList()

        # The total time
        self.total_time = 0.0

        # Set up the player, image from kenney.nl
        self.player_sprite = arcade.Sprite("alienPink_front.png", scale=0.3)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        # set up star, image from kenney.nl, 1470, 1750
        star = arcade.Sprite("star.png", 0.4)
        star.center_x = 1470
        star.center_y = 1750
        self.star_list.append(star)

        self.load_level(self.level)

    def load_level(self, level):
        map_name = f"level_{level}.json"
        self.tile_map = arcade.load_tilemap(map_name, scaling=SPRITE_SCALING)
        self.wall_list = self.tile_map.sprite_lists["walls"]

        # Use the background color of the tile map
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=0.5)


    # Do not show the mouse
    def on_show(self):
        self.window.set_mouse_visible(False)

    def on_draw(self):

        # This command has to happen before we start drawing
        arcade.start_render()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.star_list.draw()
        self.bee_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Show the timer on the screen
        arcade.draw_text(self.output, 485, 570,
                         arcade.color.WHITE, 20)

        # Show the amount of bees on the screen
        output = f"Bees on screen: {len(self.bee_list)}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 12)

    def on_key_press(self, key, modifiers):

        # How high the sprite can jump when the up key is pressed
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = 12

        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        # Make the game less touchy

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):

        # If the game is not over, keep spawning new bees
        if not self.game_over:
            self.spawn_new_enemy_timer += delta_time

            # Spawn 7 new bees every 3 seconds
            if self.spawn_new_enemy_timer > 3:
                self.spawn_new_enemy_timer = 0

                for i in range(BEE_COUNT):
                    bee = Bee("bee.png", sprite_scaling=0.2)
                    # image from kenney.nl
                    bee_placed_successfully = False

                    # Keep trying until success
                    while not bee_placed_successfully:

                        bee.center_x = random.randrange(64, 1856)
                        bee.center_y = random.randrange(64, 1856)
                        bee.change_x = 5
                        bee.change_y = 0

                        wall_hit_list = arcade.check_for_collision_with_list(bee, self.wall_list)

                        # See if the bee is hitting bee
                        bee_hit_list = arcade.check_for_collision_with_list(bee, self.bee_list)

                        if len(wall_hit_list) == 0 and len(bee_hit_list) == 0:
                            bee_placed_successfully = True

                    self.bee_list.append(bee)

            self.physics_engine.update()

            # Keep the timer going
            self.total_time += delta_time

            # Calculate the time on the clock
            minutes = int(self.total_time) // 60
            seconds = int(self.total_time) % 60
            hundreths = int((self.total_time - seconds) * 100)

            # The clock all put together
            self.output = f"{minutes:02d}:{seconds:02d}:{hundreths:02d}"

            bee_player_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bee_list)

            # If the player collides with a bee, send to the game over screen
            if len(bee_player_hit_list) > 0:
                self.game_over = True
                game_over_view = GameOver()
                game_over_view.total_time = self.total_time
                game_over_view.bee_list = self.bee_list
                self.window.set_mouse_visible(True)
                self.window.show_view(game_over_view)

            self.bee_list.update()

            # If the player collides with the star, send to the win screen
            if len(arcade.check_for_collision_with_list(self.player_sprite, self.star_list)) == 1:
                if self.level < self.max_level:
                    self.level += 1
                    self.load_level(self.level)
                    self.player_sprite.center_x = 100
                    self.player_sprite.center_y = 100

            elif len(arcade.check_for_collision_with_list(self.player_sprite, self.star_list)) == 2:
                self.game_over = True
                win_view = WinView()
                win_view.total_time = self.total_time
                win_view.bee_list = self.bee_list
                self.window.set_mouse_visible(True)
                self.window.show_view(win_view)

            # The boundaries of the bee and reversing
            for bee in self.bee_list:
                # If the enemy hit a wall, reverse
                if len(arcade.check_for_collision_with_list(bee, self.wall_list)) > 0:
                    bee.change_x *= -1
                # If the enemy hit the left boundary, reverse
                elif bee.boundary_left is not None and bee.left < bee.boundary_left:
                    bee.change_x *= -1
                # If the enemy hit the right boundary, reverse
                elif bee.boundary_right is not None and bee.right > bee.boundary_right:
                    bee.change_x *= -1

            # Scroll the screen to the player
            self.scroll_to_player()

    def scroll_to_player(self):

        # Scroll the screen around the player
        position = self.player_sprite.center_x - DEFAULT_SCREEN_WIDTH / 2, \
            self.player_sprite.center_y - DEFAULT_SCREEN_HEIGHT / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):

        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


# When the game is over, show this screen
class GameOver(arcade.View):
    def __init__(self):
        super().__init__()
        self.total_time = 0
        self.bee_list = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.BRICK_RED)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("GAME OVER", 100, 400, arcade.color.WHITE, 50)
        arcade.draw_text("Click to play again", 210, 375, arcade.color.WHITE, 15)

        time_format = f"{round(self.total_time, 2)} seconds"
        arcade.draw_text(f"Time: {time_format}", 210, 225, arcade.color.WHITE, 15)

        output_bees = f"Bees on screen: {len(self.bee_list)}"
        arcade.draw_text(output_bees, 215, 200, arcade.color.WHITE, 15)

    # When the screen is clicked, move back to the game
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        game = MyGame()
        game.setup()
        self.window.show_view(game)

    # def on_key_press(self, key, modifiers):
        # if key == arcade.key.SPACE:
        #     done = True
        #


# Show this screen when the player wins
class WinView(arcade.View):
    def __init__(self):
        super().__init__()
        self.total_time = 0
        self.bee_list = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.GOLD)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("YOU WIN!", 140, 400, arcade.color.WHITE, 50)
        arcade.draw_text("Click to play again", 215, 375, arcade.color.WHITE, 15)

        time_format = f"{round(self.total_time, 2)} seconds"
        arcade.draw_text(f"Time: {time_format}", 210, 225, arcade.color.WHITE, 15)

        output_bees = f"Bees on screen: {len(self.bee_list)}"
        arcade.draw_text(output_bees, 210, 200, arcade.color.WHITE, 15)

    # When the screen is pressed, play the game again
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        game = MyGame()
        game.setup()
        self.window.show_view(game)


def main():
    """ Main function """
    window = arcade.Window(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = Menu()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()

# Create game where win if get to top and try to win quickest, more enemies spawn over time
# reach gold star in top right corner
# add levels
import random
import arcade

SPRITE_SCALING = 0.5

DEFAULT_SCREEN_WIDTH = 600
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Alien Dash"

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7

# Amount of bees spawned at one time
BEE_COUNT = 7
BEE_LEFT = 0
BEE_RIGHT = 1


# Menu view for the screen
class Menu(arcade.View):

    def on_show(self):
        arcade.set_background_color(arcade.color.BANGLADESH_GREEN)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Alien Dash", 130, 300, arcade.color.WHITE, 50)
        arcade.draw_text("Click for instructions", 190, 270, arcade.color.WHITE_SMOKE, 15)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # When the screen is pressed, move to instruction screen
        instructions = Instructions()
        self.window.show_view(instructions)


# Instructions for the game
class Instructions(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions", 140, 400, arcade.color.BLACK, 50)
        arcade.draw_text("Jump to the top of the game in as quickly as possible.", 60, 300, arcade.color.DARK_GRAY, 15)
        arcade.draw_text("Do not touch any bees along the way.", 120, 275, arcade.color.DARK_GRAY, 15)
        arcade.draw_text("As time continues, more bees will spawn.", 105, 250, arcade.color.DARK_GRAY, 15)
        arcade.draw_text("Use the arrow keys to move around.", 125, 225, arcade.color.DARK_GRAY, 15)
        arcade.draw_text("Hit the gold star in order to win the game.", 105, 200, arcade.color.DARK_GRAY, 15)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # After click, move to the game view
        game = MyGame()
        game.setup()
        self.window.show_view(game)


# Create the bee sprite
class Bee(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.scale = 0.2
        self.textures = []

        texture = arcade.load_texture("bee.png")
        self.textures.append(texture)
        texture = arcade.load_texture("bee.png", flipped_horizontally=True)
        self.textures.append(texture)

        self.texture = texture

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_x < 0:
            self.texture = self.textures[BEE_LEFT]
        elif self.change_x > 0:
            self.texture = self.textures[BEE_RIGHT]


# The game view
class MyGame(arcade.View):
    # done = False
    # while not done:
    def __init__(self):
        super().__init__()

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.star_list = None
        self.bee_list = None
        self.game_over = False
        self.lose_sound = None

        # For the timer
        self.total_time = 0.0
        self.output = "00:00:00"

        # Set up the player
        self.player_sprite = None
        self.bee_sprite = None
        self.spawn_new_enemy_timer = 0

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()
        self.bee_list = arcade.SpriteList()

        # The total time
        self.total_time = 0.0

        # Set up the player, image from kenney.nl
        self.player_sprite = arcade.Sprite("alienPink_front.png", scale=0.3)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        # Load the map from tiled and add them to the wall list
        map_name = "Final.json"
        self.tile_map = arcade.load_tilemap(map_name, scaling=SPRITE_SCALING)
        self.wall_list = self.tile_map.sprite_lists["walls"]

        # set up star, image from kenney.nl
        star = arcade.Sprite("star.png", 0.4)
        star.center_x = 1470
        star.center_y = 1750
        self.star_list.append(star)

        # Use the background color of the tile map
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=0.5)

    # Do not show the mouse
    def on_show(self):
        self.window.set_mouse_visible(False)

    def on_draw(self):

        # This command has to happen before we start drawing
        arcade.start_render()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.star_list.draw()
        self.bee_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Show the timer on the screen
        arcade.draw_text(self.output, 485, 570,
                         arcade.color.WHITE, 20)

        # Show the amount of bees on the screen
        output = f"Bees on screen: {len(self.bee_list)}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 12)

    def on_key_press(self, key, modifiers):

        # How high the sprite can jump when the up key is pressed
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = 12
                jump_sound = arcade.load_sound("arcade_resources_sounds_jump4.wav")
                arcade.play_sound(jump_sound)

        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        # elif key == arcade.key.SPACE:
        #     done = True

    def on_key_release(self, key, modifiers):
        # Make the game less touchy

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):

        # If the game is not over, keep spawning new bees
        if not self.game_over:
            self.spawn_new_enemy_timer += delta_time

            # Spawn 7 new bees every 3 seconds
            if self.spawn_new_enemy_timer > 3:
                self.spawn_new_enemy_timer = 0

                for i in range(BEE_COUNT):
                    bee = Bee("bee.png", sprite_scaling=0.2)
                    # image from kenney.nl
                    bee_placed_successfully = False

                    # Keep trying until success
                    while not bee_placed_successfully:

                        bee.center_x = random.randrange(64, 1856)
                        bee.center_y = random.randrange(64, 1856)
                        bee.change_x = 5
                        bee.change_y = 0

                        wall_hit_list = arcade.check_for_collision_with_list(bee, self.wall_list)

                        # See if the bee is hitting bee
                        bee_hit_list = arcade.check_for_collision_with_list(bee, self.bee_list)

                        if len(wall_hit_list) == 0 and len(bee_hit_list) == 0:
                            bee_placed_successfully = True

                    self.bee_list.append(bee)

            self.physics_engine.update()

            # Keep the timer going
            self.total_time += delta_time

            # Calculate the time on the clock
            minutes = int(self.total_time) // 60
            seconds = int(self.total_time) % 60
            hundreths = int((self.total_time - seconds) * 100)

            # The clock all put together
            self.output = f"{minutes:02d}:{seconds:02d}:{hundreths:02d}"

            # If the player collides with a bee, send to the game over screen
            if len(arcade.check_for_collision_with_list(self.player_sprite, self.bee_list)) > 0:
                if not self.lose_sound:
                    self.lose_sound = arcade.load_sound(":resources:sounds/gameover5.wav")
                    arcade.play_sound(self.lose_sound)
                self.game_over = True
                game_over_view = GameOver()
                game_over_view.total_time = self.total_time
                game_over_view.bee_list = self.bee_list
                self.window.set_mouse_visible(True)
                self.window.show_view(game_over_view)

            self.bee_list.update()

            # If the player collides with the star, send to the win screen
            if len(arcade.check_for_collision_with_list(self.player_sprite, self.star_list)) > 0:
                self.game_over = True
                win_view = WinView()
                win_view.total_time = self.total_time
                win_view.bee_list = self.bee_list
                self.window.set_mouse_visible(True)
                self.window.show_view(win_view)

            # The boundaries of the bee and reversing
            for bee in self.bee_list:
                # If the enemy hit a wall, reverse
                if len(arcade.check_for_collision_with_list(bee, self.wall_list)) > 0:
                    bee.change_x *= -1
                # If the enemy hit the left boundary, reverse
                elif bee.boundary_left is not None and bee.left < bee.boundary_left:
                    bee.change_x *= -1
                # If the enemy hit the right boundary, reverse
                elif bee.boundary_right is not None and bee.right > bee.boundary_right:
                    bee.change_x *= -1

            # Scroll the screen to the player
            self.scroll_to_player()

    def scroll_to_player(self):

        # Scroll the screen around the player
        position = self.player_sprite.center_x - DEFAULT_SCREEN_WIDTH / 2, \
            self.player_sprite.center_y - DEFAULT_SCREEN_HEIGHT / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):

        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


# When the game is over, show this screen
class GameOver(arcade.View):
    def __init__(self):
        super().__init__()
        self.total_time = 0
        self.bee_list = 0


    def on_show(self):
        arcade.set_background_color(arcade.color.BRICK_RED)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("GAME OVER", 100, 400, arcade.color.WHITE, 50)
        arcade.draw_text("Click to play again", 210, 375, arcade.color.WHITE, 15)

        time_format = f"{round(self.total_time, 2)} seconds"
        arcade.draw_text(f"Time: {time_format}", 210, 225, arcade.color.WHITE, 15)

        output_bees = f"Bees on screen: {len(self.bee_list)}"
        arcade.draw_text(output_bees, 215, 200, arcade.color.WHITE, 15)

    # When the screen is clicked, move back to the game
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        game = MyGame()
        game.setup()
        self.window.show_view(game)


# Show this screen when the player wins
class WinView(arcade.View):
    def __init__(self):
        super().__init__()
        self.total_time = 0
        self.bee_list = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.GOLD)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("YOU WIN!", 140, 400, arcade.color.BLACK, 50)
        arcade.draw_text("Click to play again", 215, 375, arcade.color.BLACK, 15)

        time_format = f"{round(self.total_time, 2)} seconds"
        arcade.draw_text(f"Time: {time_format}", 210, 225, arcade.color.BLACK, 15)

        output_bees = f"Bees on screen: {len(self.bee_list)}"
        arcade.draw_text(output_bees, 210, 200, arcade.color.BLACK, 15)

    # When the screen is pressed, play the game again
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        game = MyGame()
        game.setup()
        self.window.show_view(game)


def main():
    """ Main function """
    window = arcade.Window(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = Menu()
    window.show_view(start_view)
    arcade.run()


#     high_score = get_high_score()
#     current_score = 00.00
#
#     current_score = int(input(f"What is your score?"))
#
#     if current_score > high_score:
#         print("New high score!")
#         save_high_score(current_score)
#     else:
#         print("Better luck next time!")
#
#
# def get_high_score():
#     high_score_time = 00.00
#     try:
#         high_score_file = open("high_score")
#         high_score_time = int(high_score_file.read())
#         high_score_file.close()
#         print(f"High score: {high_score_time}")
#     except IOError:
#         print(f"No high score")
#     except ValueError:
#         print("Starting with no high score")
#
#     return high_score_time
#
#
# def save_high_score(new_high_score):
#     try:
#         high_score_file = open("high_score")
#         high_score_file.write(str(new_high_score))
#         high_score_file.close()
#     except IOError:
#         print(f"Not able to save high score")
#

if __name__ == "__main__":
    main()