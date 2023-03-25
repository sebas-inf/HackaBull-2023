import pygame

pygame.init() #Initializes pygames

display_width = 800

display_length = 600

screen = pygame.display.set_mode((display_width, display_length)) #Display

pygame.display.set_caption("Bullons") #Window Name

background_image = pygame.image.load("grass.png") #Map backgroun

on = True #Flag to run program
 
while on:
    if pygame.event == pygame.QUIT:
        on = False

    screen.blit(background_image, (0,0)) #Places the game background
    
    pygame.display.flip() #Updates the game screen
    
pygame.quit()








