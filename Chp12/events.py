import pygame
import sys 
# initializing imported module
pygame.init()
  
# displaying a window of height
# 500 and width 400
pygame.display.set_mode((1000, 700))
pygame.display.flip() 
while True:
    for event in pygame.event.get():
        if event.type == pygame.K_q:
            sys.exit()
            