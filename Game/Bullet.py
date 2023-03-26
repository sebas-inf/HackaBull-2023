import pygame
from math import sqrt
class Bullet:
    def __init__(self, x, y, dx, dy, radius, damage):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.speed = 1
        self.radius = radius
        self.damage = damage

    def update(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed
    
    def draw(self, surface):
        pygame.draw.circle(surface, (62, 60, 66), (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(surface, (179, 176, 159), (int(self.x), int(self.y)), self.radius - 2)
        
    def delete(self, bullets):
        # delete self from bullets list
        bullets.remove(self)
        
    def check_hit(self, bulloons):
        for bulloon in bulloons:
            distance = sqrt(pow((bulloon.x - self.x),2) + pow((bulloon.y - self.y),2))
            if distance <= bulloon.radius + self.radius:
                bulloon.take_damage(bulloons, self.damage)
                return True
    
    def check_off_screen(self, width, height, bullets):
        # check if bullet is off screen, ifso delete it
        if self.x < -self.radius or self.x > width + self.radius or self.y < -self.radius or self.y > height + self.radius:
            self.delete(bullets)