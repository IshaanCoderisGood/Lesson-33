import pygame
pygame.init()
size = pygame.display.set_mode((1920, 1080))
no = False
while not no:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
pygame.display.flip()