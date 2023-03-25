import pygame

pygame.init() #Initializes pygames

#Display section
display_width = 800
display_length = 600
screen = pygame.display.set_mode((display_width, display_length)) #Display
pygame.display.set_caption("Bullons") #Window Name
background_image = pygame.image.load("Game\\art\\grass.png") #Map background

#Colors
pathColor = (204,171,120)
pathOutlineColor = (190,145,103)

 
while True:
    if pygame.event == pygame.QUIT:
        pygame.quit()

    screen.blit(background_image, (0,0)) #Places the game background
    
    pygame.display.flip() #Updates the game screen
    








