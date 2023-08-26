import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sound Example"

COIN_RADIUS = 15
PLAYER_SPEED = 5
TOTAL_COINS = 10

class MyGame(arcade.Window):
  def __init__(self):
    super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    self.player_x = SCREEN_WIDTH // 2
    self.player_y = 100
    self.coins = []
    self.coin_sound = arcade.load_sound("coin_sound.wav")

    for _ in range(TOTAL_COINS):
      coin = [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)]
      self.coins.append(coin)

  def on_draw(self):
    arcade.start_render()
    for coin in self.coins:
      arcade.draw_circle_filled(coin[0], coin[1], COIN_RADIUS, arcade.color.YELLOW)

    arcade.draw_circle_filled(self.player_x, self.player_y, 30, arcade.color.BLUE)

  def on_key_press(self, key, modifiers):
    if key == arcade.key.LEFT:
      self.player_x -= PLAYER_SPEED
    elif key == arcade.key.RIGHT:
      self.player_x += PLAYER_SPEED
    if key == arcade.key.UP:
      self.player_y += PLAYER_SPEED
    elif key == arcade.key.DOWN:
      self.player_y -= PLAYER_SPEED

  def update(self, delta_time):
    for coin in self.coins:
      # Check if the player collects a coin
      distance = ((self.player_x - coin[0]) ** 2 + (self.player_y - coin[1]) ** 2) ** 0.5
      if distance < 45: # 45 is the sum of the player and coin radii
        coin[0] = random.randint(0, SCREEN_WIDTH)
        coin[1] = random.randint(0, SCREEN_HEIGHT)
        arcade.play_sound(self.coin_sound)

def main():
  game = MyGame()
  arcade.run()

if __name__ == "__main__":
  main()
