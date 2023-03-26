import pygame
from Node import Node
from Bulloon import Bulloon
from Bullet import Bullet
from KeyboardT import KeyboardT
from math import sqrt

pygame.init() #Initializes pygames



#Display section
display_width = 800
display_length = 600
screen = pygame.display.set_mode((display_width, display_length)) #Display
pygame.display.set_caption("Bulloons") #Window Name
icon = pygame.image.load("Game/art/Hackabull.PNG")
pygame.display.set_icon(icon)#Favicon
background_image = pygame.image.load("Game/art/grass.png") #Map background

#clock to set framerate later
clock = pygame.time.Clock()
framerate = 60

#Font
font = pygame.font.SysFont("Arial", 50)

#Colors
pathColor = (204,171,120)
pathOutlineColor = (190,145,103)

#Nodes
nodes = [
    Node(278, 425, 0, -1),
    Node(278, 125, 1, 0),
    Node(578, 125, 0, 1),
    Node(578, 325, -1, 0),
    Node(428, 325, 0, 1),
    Node(428, 425, 1, 0),
    Node(678, 425, 0, 1)
]

# Bulloons
spawnX = -40
spawnY = 425
bulloons = [
    Bulloon(1,spawnX,spawnY, 1, 0),
    Bulloon(2,spawnX,spawnY, 1, 0),
    Bulloon(3,spawnX,spawnY, 1, 0),
    Bulloon(2,spawnX,spawnY, 1, 0)
]
# towers
towers = []
# bullets
bullets = []
#Path rectangles
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


#Path outline rectangles
path_rectoutline_list = [
    pygame.Rect(0,400,310,60),
    pygame.Rect(250,150,60,260),
    pygame.Rect(250,100,310,60),
    pygame.Rect(550,100,60,210),
    pygame.Rect(400,300,210,60),
    pygame.Rect(400,350,60,110),
    pygame.Rect(450,400,260,60),
    pygame.Rect(650,450,60,160)
]

# flag variables
lose_condition = False
win_condition = False

#Displays losing message
def lost():
    button_width = 200
    button_height = 100
    button_surface = pygame.Surface((button_width, button_height))
    button_surface.fill((122,45,48))
    text = font.render("You Lost", True, (255,255,255))
    text_rect = text.get_rect(center = (button_width // 2, button_height // 2))
    button_surface.blit(text, text_rect)

#Displays winning message
def won():
    button_width = 200
    button_height = 100
    button_surface = pygame.Surface((button_width, button_height))
    button_surface.fill((65,135,145))
    text = font.render("You Won", True, (255,255,255))
    text_rect = text.get_rect(center = (button_width // 2, button_height // 2))
    button_surface.blit(text, text_rect)

#Runs the game itself
def play():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    towers.append(KeyboardT(1, 100, 5))
                
        screen.blit(background_image, (0,0)) #Places the game background
        
        if lose_condition:
            lost()
        if win_condition:
            won()
    
        #Draws the outline of the path
        for outline in path_rectoutline_list:
            pygame.draw.rect(screen, pathOutlineColor, outline)

        # draws the path
        for rect in path_rect_list:
            pygame.draw.rect(screen,pathColor,rect)

        #update bulloons
        for bulloon in bulloons:
            bulloon.update(nodes)
            bulloon.check_reached_end(bulloons)
            bulloon.draw(screen)

        for bullet in bullets:
            bullet.update()
            if bullet.check_hit(bulloons):
                bullet.delete(bullets)
            bullet.check_off_screen(display_width, display_length, bullets)
            bullet.draw(screen)
        
        for tower in towers:
            if tower.placeMode:
                tempx, tempy = pygame.mouse.get_pos()
                tower.move(tempx,tempy)
                if pygame.mouse.get_pressed()[0]:
                    tower.placeMode = False

            if not tower.canShoot:
                delay = 1000 / tower.fireRate
                tower.time = pygame.time.get_ticks()
                elapsed_time = pygame.time.get_ticks() - delay
                if elapsed_time >= delay:
                    tower.canShoot = True
            for bulloon in bulloons:
                if sqrt(pow((tower.x - bulloon.x),2) + pow((tower.y - bulloon.y),2)) <= tower.damageRange and not tower.placeMode:
                    bullets.append(tower.shoot(bulloon.x, bulloon.y, pygame.time.get_ticks()))
            tower.draw(screen, tower.placeMode)

        pygame.display.flip() #Updates the game screen
        clock.tick(framerate) #sets max fps to the framerate 

#Starting menu
def menu():
    button_width = 200
    button_height = 100
    button_surface = pygame.Surface((button_width, button_height))
    button_surface.fill((65,135,145))
    button_rect = button_surface.get_rect(center = (button_width // 2, button_height // 2))
    text = font.render("Start", True, (255,255,255))
    text_rect = text.get_rect(center = (button_width // 2, button_height // 2))
    button_surface.blit(text, text_rect)
    button_rect.x = display_width // 2 - button_width // 2
    button_rect.y = display_length // 2 - button_height // 2
    

    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # check for button click
                if button_rect.collidepoint(event.pos):
                    play()

        screen.fill((255,255,255)) # draw background color for menu
        screen.blit(button_surface, button_rect) # draw play button

        pygame.display.flip() #Updates the game screen


menu()