import pygame
from pygame.locals import*
pygame.init()


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


fpsClock = pygame.timeClock()
fps= 60

width, height = 540, 480
screen = pygame.display.set_mode((width,height))

while True:
    screen.fill((0,0,0))
  
    for event in pygame.event.get():
        if event.type ==QUIT:
          pygame.quit()
          sys.exit()
    pegame.display.flip()
    fpsClock.tick(fps)
    
