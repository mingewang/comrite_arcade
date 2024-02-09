# draw_circle.py

import arcade
#
class MyGame(arcade.Window):
  def __init__(self, width, height, title):
    # Call the parent class's init function
    super().__init__(width, height, title)
    # Set the background color
    arcade.set_background_color(arcade.color.ASH_GREY)
#
  def on_draw(self):
    """ Called whenever we need to draw the window. """
    arcade.start_render()
    arcade.draw_circle_filled(50, 50, 15, arcade.color.AUBURN)
    arcade.draw_rectangle_filled(150,150,60, 60, arcade.color.ALLOY_ORANGE)
    arcade.draw_ellipse_filled(180,180, 40, 150, arcade.color.AMARANTH)
#
def main():
   window = MyGame(640, 480, "Drawing Example")
   arcade.run()
#
main()