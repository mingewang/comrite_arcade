""" Sprite Sample Program """

import arcade
import random

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Sprite lists
        self.player_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None

        # This variable holds our simple "physics engine"
        self.physics_engine = None

        self.laser_sound = arcade.load_sound(":resources:sounds/laser3.wav")
        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Reset the score
        self.score = 0

        # Create the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_jump.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 0
        self.player_sprite.center_y = 0 
        self.player_list.append(self.player_sprite)

        # --- Manually place walls

        # Manually create and position a box at 300, 200
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        # Manually create and position a box at 364, 200
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 364
        wall.center_y = 200
        self.wall_list.append(wall)

        # --- Place boxes inside a loop
        for x in range(173, 650, 64):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        # --- Place walls with a list
        coordinate_list = [[400, 500],
                           [470, 500],
                           [400, 570],
                           [470, 570]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # --- Place walls with a list
        coordinate_list = [[1400, 500],
                           [1470, 500],
                           [1400, 570],
                           [1470, 570]]

        # --- Place walls with a list
        for i in range(1000):
            tmp_wall = [random.randint(-1000,4000), random.randint(-2000,5000)]
            coordinate_list.append(tmp_wall)

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        #self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, gravity_constant=0, walls=self.wall_list)

    def on_draw(self):
        arcade.start_render()

        # Select the scrolled camera for our sprites 
        # select this camera for use. Do this right before you draw.
        self.camera_for_sprites.use()

        # Draw the sprites
        self.wall_list.draw()
        self.player_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_for_gui.use()
        text = f"GUI: ({self.camera_for_gui.position[0]:1.0f}," \
               f"{self.camera_for_gui.position[1]:1.0f})" \
               f"score: {self.score}," \
               f"camera: ({self.camera_for_sprites.position[0]:4.0f}, " \
               f"{self.camera_for_sprites.position[1]:4.0f})" \
               f"player: ({self.player_sprite.center_x}," \
               f"{self.player_sprite.center_y})" 
        arcade.draw_text(text, 10, 10, arcade.color.WHITE, 24)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        hit_list = self.physics_engine.update()

        for item in hit_list:
            # hit on item
            arcade.play_sound(self.laser_sound)
            self.score += 1

        # Scroll the screen to the player
        #self.scroll_to_player()

        # Scroll the window to the player.
        #
        # If CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        # Anything between 0 and 1 will have the camera move to the location with a smoother
        # pan.
        CAMERA_SPEED = 0.1 
        lower_left_corner = (self.player_sprite.center_x - self.width / 2,
                             self.player_sprite.center_y - self.height / 2)
        # move camera to sprint
        self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()