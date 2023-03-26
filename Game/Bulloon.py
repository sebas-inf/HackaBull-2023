import pygame
from math import sqrt

class Bulloon:
    def __init__(self, health, x, y, vx, vy):
        self.__health = health
        self.__speed = health * 2
        self.__x = x
        self.__y = y
        self.__vx = vx
        self.__vy = vy

        if health == 1: # set image as redbull
            self.image = pygame.image.load("Game/art/redbull.png")
            self.__width, self.__height = self.image.get_size()

        if health == 2:
            pass

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
            
    def delete(self, bulloons):
        bulloons.remove(self)