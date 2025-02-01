import pygame,sys
pygame.init()
screen=pygame.display.set_mode((800,600))

def draw_circle(xc, yc, r):
    x, y, d = 0, r, 1 - r
    while x <= y:
        for dx, dy in [(x, y), (y, x), (-y, x), (-x, y), (-x, -y), (-y, -x), (y, -x), (x, -y)]:
            screen.set_at((xc + dx, yc + dy), 'WHITE')
        x += 1
        d = d + 2 * x + 1 if d < 0 else d + 2 * x - 2 * y + 1
        if d >= 0: 
            y -= 1



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
    screen.fill('black')
    draw_circle(200, 200, 100)
    pygame.display.flip()

