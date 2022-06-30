import pygame
from fighter import Fighter

pygame.init()
SCREEN_W = 1000
SCREEN_H = 600

clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Fighting game")

bg_img = pygame.image.load("background.png")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon) 

background_top = screen.get_height() - bg_img.get_height()
background_left = screen.get_width()/2 - bg_img.get_width()/2
  


fighter_1 =  Fighter(500, 100, 50)
print(fighter_1.y)

run = True
while run:   
    pygame.display.flip()
    screen.blit(bg_img, (background_left, background_top))
    fighter_1.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    fighter_1.move(clock)
    clock.tick()
    #print(clock.get_fps())

    

pygame.quit()