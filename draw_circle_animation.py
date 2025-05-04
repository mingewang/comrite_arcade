import arcade

class MyGame(arcade.Window):

  def __init__(self, width, height, title):

    # Call the parent class's init function
    super().__init__(width, height, title)
    # Set the background color
    arcade.set_background_color(arcade.color.ASH_GREY)
    self.ball_x = 50
    self.ball_y = 100

  def on_draw(self):
    """ Called whenever we need to draw the window. """
    self.clear()
    arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.AUBURN)
    arcade.draw_text("Hello, world!", 300, 300, arcade.color.WHITE, font_size=20, anchor_x="center")

  def update(self, delta_time):
    self.ball_x += 2 
    self.ball_y += 2 
              

def main():
  window = MyGame(640, 480, "Hello World")
  arcade.run()

if __name__ == "__main__":
  main()
