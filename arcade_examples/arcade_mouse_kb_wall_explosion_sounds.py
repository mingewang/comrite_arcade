import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
        self.explosion_sound = arcade.load_sound(":resources:sounds/explosion2.wav")
        self.explosion_sound_player = None

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius, self.
                                  color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        hit_wall = False

        if self.position_x < self.radius:
            self.position_x = self.radius
            hit_wall = True 

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            hit_wall = True 

        if self.position_y < self.radius:
            self.position_y = self.radius
            hit_wall = True 

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            hit_wall = True 

        if hit_wall:
            # the following works
            #arcade.play_sound(self.explosion_sound)
            # better this
            # https://learn.arcade.academy/en/latest/chapters/20_sounds/sounds.html
            if not self.explosion_sound_player or not self.explosion_sound_player.playing:
                self.explosion_sound_player = arcade.play_sound(self.explosion_sound)

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)
        self.laser_sound = arcade.load_sound("laser.wav")
        self.background_music = arcade.load_sound(":resources:music/1918.mp3")
        arcade.play_sound(self.background_music, volume=0.5, looping=True)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            arcade.play_sound(self.laser_sound)


    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.ball.position_x = x
        self.ball.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button pressed at", x, y)

def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()