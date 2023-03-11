import arcade
import animate
from constants import SCREEN_WIDTH

class Zombie(animate.Animate):
    def __init__(self, image, health, row, center_y):
        super().__init__(image, scale=0.09)
        self.health = health
        self.row = row
        self.set_position(SCREEN_WIDTH, center_y)
        self.change_x = 0.2
    
    def update(self):
        self.center_x -= self.change_x
        if self.health <= 0:
            self.kill()

class OrdinaryZombie(Zombie):
    def __init__(self, center_y, row):
        super().__init__('zombies/zom1.png', 12, row, center_y)
        self.append_texture(arcade.load_texture(f'zombies/zom1.png'))
        self.append_texture(arcade.load_texture(f'zombies/zom2.png'))