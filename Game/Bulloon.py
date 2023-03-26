import pygame
from math import sqrt

class Bulloon:
    def __init__(self, level, x, y, vx, vy):
        self.__health = level
        self.__speed = level * 2
        self.__x = x
        self.__y = y
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

        #self.__radius = (self.__width + self.__height) // 2 # set radius to be used in distance calculations

    def draw(self, surface):
        surface.blit(self.image, (self.__x - self.__width // 2, self.__y - self.__height // 2))
    
    def update(self, nodes):
        self.__x += self.__vx * self.__speed
        self.__y += self.__vy * self.__speed
        for node in nodes:
            if sqrt(pow((node.x - self.__x),2) + pow((node.y - self.__y),2)) <= 6:
                self.__vx = node.dx
                self.__vy = node.dy
                if node.dx == 0:
                    self.x = node.x
                elif node.dy == 0:
                    self.y = node.y
    
    def take_damage(self, bulloons, damage):
        self.health = max(0, self.health - damage)
        if self.health == 0:
            self.delete(bulloons)

    def delete(self, bulloons):
        bulloons.remove(self)

    def check_reached_end(self, bulloons): #returns health (the damage amount) if the bulloon reached the end, otherwise it returns 0 to indicate it has not reached the end
        if (self.x  == 675 and self.y >= (600 + self.__height)):
            return self.__health
        else:
            return 0