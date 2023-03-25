import pygame

pygame.init() #Initializes pygames

display_width = 800

display_length = 600

screen = pygame.display.set_mode((display_width, display_length)) #Display

pygame.display.set_caption("Bullons") #Window Name

background_color = (255, 255, 255) #White Background

on = True
 
while on:
    if pygame.event == pygame.QUIT:
        on = False

    screen.fill(background_color)
    
    pygame.display.update()    
    
pygame.quit()








