# KeyboardT.py
import pygame
from Bullet import Bullet
from math import sqrt
class KeyboardT:
    def __init__(self, damage, damageRange, fireRate):
        self.__damage = damage
        self.damageRange = damageRange
        self.fireRate = fireRate
        self.canShoot = True
        self.x, self.y = 0,0
        self.time = 0
        self.placeMode = True
        self.image = pygame.image.load("Game/art/keyboardTower.png")
        self.__width, self.__height = self.image.get_size()
        self.radius = (self.__width + self.__height // 2)
        ## damage of tower, range of tower, size of tower

    def draw(self, surface, highlight):
        if highlight:
            radius = self.damageRange
            circle = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
            pygame.draw.circle(circle, (179, 176, 159, 200), (self.x - self.__width // 2, self.y - self.__height // 2), radius)
        surface.blit(self.image, (self.x - self.__width // 2, self.y - self.__height // 2))

    def move(self, x, y):
        self.x = x
        self.y = y

    def shoot(self, targetx, targety, time):
        # Calculate the direction from the player to the bulloon
        direction_x = targetx - self.x
        direction_y = targety - self.y
        
        # set time
        self.time = time

        # Normalize the direction vector
        direction_length = sqrt(direction_x ** 2 + direction_y ** 2)
        if direction_length != 0:
            direction_x /= direction_length
            direction_y /= direction_length
        
        # Calculate the position of the bullet
        bullet_radius = 4
        bullet_x = self.x + direction_x * (self.radius + bullet_radius)
        bullet_y = self.y + direction_y * (self.radius + bullet_radius)
        
        # Create the bullet
        bullet = Bullet(bullet_x, bullet_y, direction_x, direction_y, bullet_radius, self.__damage)

        self.canShoot = False
        return bullet
    