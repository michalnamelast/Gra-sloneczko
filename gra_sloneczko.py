
from threading import Timer
import pygame, time
from gra_sloneczko_sun import Sun 
from gra_sloneczko_tlo import Tlo
from gra_sloneczko_snieg import Snieg
from gra_sloneczko_przeszkoda import Przeszkoda




class Gra(object):

  def __init__(self):
    # Importuje 
    self.player = Sun(self)
    self.tlo = Tlo(self)
    self.snieg = Snieg(self)
    self.przeszkoda = Przeszkoda(self)
   
    # Okno gry 
    pygame.init()
    self.screen = pygame.display.set_mode((1180, 720))
  


    # petla gry
    running = True
    while running:
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
          running = False

      self.screen.fill((self.tlo.kolor1, self.tlo.kolor2, self.tlo.kolor3))
      self.drawing()
      self.sterowanie()
      pygame.display.flip()
      
      
        

  def sterowanie(self):
    self.player.szybkosc()
    self.player.sterowanie()
    self.player.strona()
    self.tlo.jasnosc()
    self.tlo.moc()
    self.przeszkoda.fizyka()
    
    

  def drawing(self):
    self.snieg.licz()
    self.snieg.sniezynka()
    self.player.drawing()
    self.przeszkoda.draw()
    self.przeszkoda.tabela()
    
    
    

if __name__ == '__main__':
  Gra()
