import pygame
from gra_sloneczko_sun import Sun


class Tlo(object):

    def __init__(self, gra):
        self.gra = gra
        self.player = Sun(self)
        self.kolor1 = 0
        self.kolor2 = 0
        self.kolor3 = 245
        



    def jasnosc(self):
        self.player.sterowanie()
        self.player.szybkosc()
        pressed = pygame.key.get_pressed()
        if ((pressed[pygame.K_w] and 10 <= self.kolor3 < 250) and (-350 < self.player.y < -50 )):
            self.kolor3 += -self.player.speed
        if ((pressed[pygame.K_s] and 4 <= self.kolor3 < 244) and (-350 < self.player.y < -50)):
            self.kolor3 += self.player.speed
        if ((pressed[pygame.K_w] and 4 <= self.kolor3 < 244) and (992 > self.player.y > 580)):
            self.kolor3 += self.player.speed
        if ((pressed[pygame.K_s] and 10 <= self.kolor3 < 250) and (992 > self.player.y > 580)):
            self.kolor3 += -self.player.speed
        if ((pressed[pygame.K_a] and 10 <= self.kolor3< 250) and (-350 < self.player.x < -30 )):
            self.kolor3 += -self.player.speed
        if ((pressed[pygame.K_d] and 4 <= self.kolor3 < 244) and (-350 < self.player.x < -30)):
            self.kolor3 += self.player.speed
        if ((pressed[pygame.K_a] and 4 <= self.kolor3 < 244) and (1300 > self.player.x > 1020)):
            self.kolor3 += self.player.speed
        if ((pressed[pygame.K_d] and 10 <= self.kolor3 < 250) and (1300 > self.player.x > 1020)):
            self.kolor3 += -self.player.speed

    def moc(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_m] and self.kolor1 < 255 and self.kolor2 < 255:
            self.kolor1 += 1
            self.kolor2 += 1
        elif self.kolor1 > 0 and self.kolor2 > 0:
            self.kolor1 += -1
            self.kolor2 += -1
        

            

