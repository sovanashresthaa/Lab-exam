import pygame,sys
pygame.init()

screen = pygame.display.set_mode((800, 600))

def draw_ellipse(xc, yc, rx, ry):
    x, y = 0, ry
    rx2, ry2 = rx**2, ry**2
    two_rx2, two_ry2 = 2 * rx2, 2 * ry2
    px, py = 0, two_rx2 * y

    # Region 1
    p = ry2 - (rx2 * ry) + (0.25 * rx2)
    while px < py:
        for dx, dy in [(x, y), (-x, y), (x, -y), (-x, -y)]:
            screen.set_at((xc + dx, yc + dy), 'WHITE')
        x += 1
        px += two_ry2
        if p < 0:
            p += ry2 + px
        else:
            y -= 1
            py -= two_rx2
            p += ry2 + px - py

    # Region 2
    p = ry2 * (x + 0.5)**2 + rx2 * (y - 1)**2 - rx2 * ry2
    while y >= 0:
        for dx, dy in [(x, y), (-x, y), (x, -y), (-x, -y)]:
            screen.set_at((xc + dx, yc + dy), 'WHITE')
        y -= 1
        py -= two_rx2
        if p > 0:
            p += rx2 - py
        else:
            x += 1
            px += two_ry2
            p += rx2 - py + px

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')
    draw_ellipse(200, 200, 100, 50)

    pygame.display.flip()
