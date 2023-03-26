import pygame
from math import sqrt
from Node import Node
class Bulloon:
    def __init__(self, level, x, y, vx, vy):
        self.__health = level
        self.__speed = level * 2
        self.x = x
        self.y = y
        self.__vx = vx
        self.__vy = vy

        if self.__health == 1: # set image as redbull
            self.image = pygame.image.load("Game/art/redbull.png")
            self.__width, self.__height = self.image.get_size()

        if self.__health == 2:
            self.image = pygame.image.load("Game/art/bluebull.png")
            self.__width, self.__height = self.image.get_size()

        if self.__health == 3:
            self.image = pygame.image.load("Game/art/greenbull.png")
            self.__width, self.__height = self.image.get_size()
        
        if self.__health == 3:
            self.image = pygame.image.load("Game/art/goldbull.png")
            self.__width, self.__height = self.image.get_size()

        self.radius = (self.__width + self.__height) // 2 # set radius to be used in distance calculations

    def draw(self, surface):
        surface.blit(self.image, (self.x - self.__width // 2, self.y - self.__height // 2))
    
    def update(self, nodes):
        self.x += self.__vx * self.__speed
        self.y += self.__vy * self.__speed
        for node in nodes:
            if sqrt(pow((node.x - self.x),2) + pow((node.y - self.y),2)) <= 6:
                self.__vx = node.dx
                self.__vy = node.dy
                if node.dx == 0:
                    self.x = node.x
                elif node.dy == 0:
                    self.y = node.y
    
    def take_damage(self, bulloons, damage):
        self.__health = max(0, self.__health - damage)
        if self.__health == 0:
            self.delete(bulloons)

    def delete(self, bulloons):
        bulloons.remove(self)

    def check_reached_end(self, bulloons): #returns health (the damage amount) if the bulloon reached the end, otherwise it returns 0 to indicate it has not reached the end
        if (self.x  == 675 and self.y >= (600 + self.__height)):
            bulloons.remove(self)
            return self.__health
        else:
            return 0