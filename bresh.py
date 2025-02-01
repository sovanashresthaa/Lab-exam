import pygame,sys
pygame.init()

screen = pygame.display.set_mode((800, 600))

def draw_line_DDA(x1, y1, x2, y2):
    
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    lx, ly = (1 if x2 > x1 else -1), (1 if y2 > y1 else -1)
    x, y = x1, y1

    if dx > dy:
        p = 2 * dy - dx
        for _ in range(dx + 1):
            screen.set_at((x, y), 'WHITE')
            x += lx
            if p >= 0:
                y += ly
                p -= 2 * dx
            p += 2 * dy
    else:
        p = 2 * dx - dy
        for _ in range(dy + 1):
            screen.set_at((x, y), 'WHITE')
            y += ly
            if p >= 0:
                x += lx
                p -= 2 * dy
            p += 2 * dx

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')
    draw_line_DDA(200, 50, 400, 300)
    pygame.display.flip()
