import pygame,sys,math
pygame.init()

screen = pygame.display.set_mode((800, 600))

def draw_line_DDA (x1, y1, x2, y2):
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    steps = max(dx, dy)
    x_inc, y_inc = dx / steps, dy / steps
    x, y = x1, y1
    for _ in range(steps + 1):
        screen.set_at((round(x), round(y)), 'white')
        x, y = x + x_inc, y + y_inc



def translate_line (x3, y3, x4, y4,tx,ty) :
    x3=x3+tx
    x4=x4+tx
    y3=y3+ty
    y4=y4+ty
    draw_line_DDA(x3,y3,x4,y4)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')
    draw_line_DDA(200, 50, 400, 300)
    translate_line(200, 50, 400, 300,200,20)
    pygame.display.flip()
