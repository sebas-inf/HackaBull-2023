import pygame
from math import sqrt

class Bulloon:
    def __init__(self, health):
        self.__health = health
        self.__speed = health * 2