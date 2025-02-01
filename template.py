import pygame,sys
pygame.init()

screen = pygame.display.set_mode((800, 600))

#define function here

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('BLACK')
    #call the function here
    pygame.display.flip()
