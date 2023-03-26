import pygame
from math import sqrt
class Bullet:
    def __init__(self, x, y, dx, dy, radius, damage):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.speed = 3
        self.radius = radius
        self.damage = damage

    def update(self):
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed
    
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), self.radius)
        
    def delete(self, bullets):
        # delete self from bullets list
        bullets.remove(self)
        
    def check_hit(self, bulloons):
        for bulloon in bulloons:
            distance = sqrt((bulloon.x - self.x) ** 2 + (bulloon.y - self.y) ** 2)
            if distance <= bulloon.radius + self.radius:
                bulloon.take_damage(bulloons, self.damage)
                return True