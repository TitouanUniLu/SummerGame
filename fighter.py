from re import X
import pygame

class Fighter():
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp

    def draw(self, screen):
        sprite = pygame.image.load("feraligatr.png")
        screen.blit(sprite, (self.x, self.y))
        
    
    def move(self, clock):
        SPEED = 0.75
        GRAVITY = 1
        dx = 0
        fall_speed = 0.001
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            print("space")
        if key[pygame.K_q]:
            dx -= SPEED
        if key[pygame.K_d]:
            dx = SPEED
        if (self.x + dx > 10) and (self.x + dx < 900):
            self.x += dx
        
        '''while self.y > 10:
            self.y -= fall_speed'''


        pygame.display.update()