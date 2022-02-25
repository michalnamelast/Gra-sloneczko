import pygame, random
from gra_sloneczko_sun import Sun

class Snieg(object):

    def __init__(self,gra):
        pygame.font.init
        self.gra = gra
        self.player = Sun(self)
        self.snieg_biel = pygame.image.load('C:/Users/mjaro/Desktop/projektypython/pygame_images/snieg_biel.png')
        self.snieg_nieb = pygame.image.load('C:/Users/mjaro/Desktop/projektypython/pygame_images/snieg_niebieski.png')
        self.snieg_maly = pygame.transform.smoothscale(self.snieg_biel,(20,20))
        self.snieg_duzy = pygame.transform.smoothscale(self.snieg_nieb,(25,22))
        self.kordy = []
        self.pkt = 0
    

        for i in range(100):
            x = random.randrange(1,1600, 1)
            y = random.randrange(1,600, 1)
            self.kordy.append([x,y])
        
       
    
    def sniezynka(self):
        self.player.sterowanie()
        self.player.szybkosc()
        for i in range(50):
            if i % 2 == 0:
                self.gra.screen.blit(self.snieg_duzy, (self.kordy[i]))
                self.kordy[i][1] += 0.5
            else:
                self.gra.screen.blit(self.snieg_maly, (self.kordy[i]))
                self.kordy[i][1] += 0.6
            if self.kordy[i][1] > 900:
                y = random.randrange(1,200,1)
                self.kordy[i][1] = y
                x = random.randrange(1,1600,1)
                self.kordy[i][0] = x
            if self.player.y + 120 > self.kordy[i][1] > self.player.y + 30 and self.player.x + 120 > self.kordy[i][0] > self.player.x + 40:
                y = random.randrange(1,200,1)
                self.kordy[i][1] = y
                x = random.randrange(1,1600,1)
                self.kordy[i][0] = x
                self.pkt += 1
        
        

    def licz(self):
        self.czcionka = pygame.font.SysFont("dejavusans", 20)
        self.punkty = str(self.pkt)
        self.text_render = self.czcionka.render(self.punkty, 1, (250, 250, 250))
        self.gra.screen.blit(self.text_render, (10,10))

        
                

                
                    
        
        

            
        
            
            
            
                
                
        
            

        
            
        

        






