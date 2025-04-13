import arcade
import time


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Attributes to store where our ball is
        self.ball_x = 50
        self.ball_y = 50

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        #arcade.start_render()
        self.clear() 

        arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.AUBURN)
        # you will see this is also 1/60 second
        print("on_draw time is: ", time.time() )

    # better use on_update according to doc
    # https://api.arcade.academy/en/latest/api/window.html?highlight=on_draw#arcade-window
    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball_x += 1
        self.ball_y += 1
        # you will see this is also 1/60 second
        #print("update time is: ", time.time() )
        # you will see this is 1/60 second
        #print("time is: ", delta_time)


def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()