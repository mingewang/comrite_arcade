import arcade

#laser_sound = arcade.load_sound("laser.wav")
#arcade.play_sound(laser_sound)


arcade.open_window(300, 300, "Sound Demo")
laser_sound = arcade.load_sound("laser.wav")
arcade.play_sound(laser_sound)
arcade.run()