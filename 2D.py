import pygame,sys,math
pygame.init()

screen = pygame.display.set_mode((800, 600))

def draw_line_Bresh(x1, y1, x2, y2):
    
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


def translate_line (x3, y3, x4, y4,tx,ty) :
    x3=x3+tx
    x4=x4+tx
    y3=y3+ty
    y4=y4+ty
    draw_line_Bresh(x3,y3,x4,y4)

def scale_line (x3, y3, x4, y4,sx,sy) :
    x3=x3*sx
    x4=x4*sx
    y3=y3*sy
    y4=y4*sy
    draw_line_Bresh(x3,y3,x4,y4)

def rotate_line (x3, y3, x4, y4,A) :
    Th=math.radians(A)

    nx3=x3*math.cos(Th)-y3*math.sin(Th)
    nx4=x4*math.cos(Th)-y4*math.sin(Th)
    ny3=y3*math.cos(Th)+x3*math.sin(Th)
    ny4=y4*math.cos(Th)+x4*math.sin(Th)

    draw_line_Bresh(round(nx3),round(ny3),round(nx4),round(ny4))





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')
    draw_line_Bresh(200, 50, 400, 300)
    translate_line(200, 50, 400, 300,200,20)
    rotate_line (200, 50, 400, 300,18)
    scale_line (200, 50, 400, 300,2,2)
    pygame.display.flip()
