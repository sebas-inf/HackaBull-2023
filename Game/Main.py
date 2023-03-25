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

#path rectangles
path_rect_list = [
    pygame.Rect(0,400,300,50),
    pygame.Rect(250,150,50,250),
    pygame.Rect(250,100,300,50),
    pygame.Rect(550,100,50,200),
    pygame.Rect(400,300,200,50),
    pygame.Rect(400,350,50,100),
    pygame.Rect(450,400,250,50),
    pygame.Rect(650,450,50,150)
]

while True:
    if pygame.event == pygame.QUIT:
        pygame.quit()

    screen.blit(background_image, (0,0)) #Places the game background

    # draws the path
    for rect in path_rect_list:
        pygame.draw.rect(screen,pathColor,rect)

    pygame.display.flip() #Updates the game screen
    








