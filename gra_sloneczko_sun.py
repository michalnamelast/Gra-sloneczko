import pygame
import time 

class Sun(object):

    def __init__(self, gra):
        self.gra = gra  
        self.sun_img = pygame.image.load('C:/Users/mjaro/Desktop/projektypython/pygame_images/sun1.png')
        
        self.x  = 300
        self.y = 300
        self.speed = 1
        # czas
        self.clock1 = pygame.time.Clock()
        self.clock2 = pygame.time.Clock()
        self.delta1 = 0.0
        self.delta2 = 0.0


    def strona(self):
        self.delta1 += self.clock1.tick() / 1000.0
        while self.delta1 > 1/11:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_l]:
                self.sun_img = pygame.transform.flip(self.sun_img, True, False)
            if pressed[pygame.K_k]:
                self.sun_img = pygame.transform.flip(self.sun_img, False, True)
            self.delta1 = 0
            


    def szybkosc(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_i]:
            self.speed = 1
        if pressed[pygame.K_o]:
            self.speed = 2
        if pressed[pygame.K_p]:
            self.speed = 3
        
        
    def sterowanie(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w] and self.y > -351:
            self.y += -self.speed
        if pressed[pygame.K_s] and self.y < 990:
            self.y +=  self.speed
        if pressed[pygame.K_d] and self.x < 1347:
            self.x +=  self.speed
        if pressed[pygame.K_a] and self.x > -351:
            self.x += -self.speed
       

    def drawing(self):
        self.gra.screen.blit(self.sun_img, (self.x, self.y))
        # print(f'X: {self.x}  Y: {self.y}')
        print(self.sun_img.get_rect().width)
        print(self.sun_img.get_width())


        
        