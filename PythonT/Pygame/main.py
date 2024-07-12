import pygame
from sys import exit

#initialise 
pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Borets')
clock = pygame.time.Clock()

mouse_pos = pygame.mouse.get_pos()

surface = pygame.Surface((100,200))
surface.fill('green')

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Add mechanics
    screen.blit(surface,(0,0))
    # at the end update everything
    pygame.display.update()
    clock.tick(60)