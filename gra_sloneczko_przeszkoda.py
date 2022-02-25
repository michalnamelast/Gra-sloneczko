import pygame, random
from numpy import gradient
from gra_sloneczko_sun import Sun



class Przeszkoda(object):

    def __init__(self, gra):
        self.sun = Sun(self)
        self.gra = gra
        self.x = random.randrange(1200)
        self.y = 100
        self.speed = 1
        self.ilosc = 10
        

        if self.y < 1000:
            self.y += self.speed
            self.y = -100
            self.x = random.randrange(1200)

    def fizyka(self):
        self.speed = self.ilosc / 10
        print(self.ilosc, self.speed)


    def draw(self):
        pygame.draw.rect(self.gra.screen, (255,0,0), pygame.Rect(self.x, self.y, 30, 60))
        self.y += self.speed
        if self.y >= 1000:
            self.x = random.randrange(1200)
            self.y = -100
            self.ilosc += 1
    
    def tabela(self):
        self.czcionka = pygame.font.SysFont("dejavusans", 30)
        self.punkty = str(self.ilosc - 10)
        self.text_render = self.czcionka.render(self.punkty, 1, (250, 0, 100))
        self.gra.screen.blit(self.text_render, (1120,10))
        
