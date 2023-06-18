import sys
import pygame


pygame.init()
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("Blue")
 #Set background color...
bg_color = (0,0,230)
while True:
    #Waits for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(bg_color)
    pygame.display.flip()