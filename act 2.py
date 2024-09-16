import pygame
pygame.init()
screenwidth,screenheight = 500,500
screen = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("park")
image = pygame.transform.scale(pygame.image.load('blue-background-7470781_1280.jpg').convert(),(screenwidth, screenheight))
imagetiger = pygame.transform.scale(pygame.image.load('images.jpg').convert_alpha(),(200, 200))
tigerrectancle = imagetiger.get_rect(center = (screenwidth // 2,screenheight // 2 - 30))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
    screen.blit(image,(0,0))
    screen.blit(imagetiger,tigerrectancle)
  

    pygame.display.flip()
    clock.tick(30)
    
    pygame.display.quit()

if __name__ == '__main__':
 game_loop()


