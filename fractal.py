import pygame, sys, math, random

def color_pixel(surface, color, pos):
    surface.fill(color, (pos, (1, 1)))

def mandlebrot(Zo,c):
    global max_iter, scale,rfac,bfac,gfac
    z = Zo
    iter=0
    while abs(z)<=5 and iter<max_iter:
        z = z**2+c
        iter+=1
    if iter == max_iter:
        color_pixel(screen, (0,0,0), (screen_width/2+Zo.real*scale, screen_height/2-Zo.imag*scale))
    else:
        rshade = iter*rfac
        if rshade>=255:
            rshade = 255

        bshade = iter*bfac
        if bshade>=255:
            bshade = 255

        gshade = iter*gfac
        if gshade>=255:
            gshade = 255
        color_pixel(screen, (rshade,gshade,bshade,),(screen_width/2+Zo.real*scale, screen_height/2-Zo.imag*scale))



pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 750

screen = pygame.display.set_mode ((screen_width, screen_height))
pygame.display.set_caption('Mandlebrot')

white = (211,81,0)
bg_color = (248,161,69)
black = (21, 21, 21)
lblack = (15, 15, 15)
mid = (240, 121, 0)
ghost_line = (0,0,0)


scale = 75
max_iter = 80

rfac,gfac,bfac = 8,4,12
ct=0
x=0;y=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
    x+=random.uniform(-1, 2)*0.02
    y+=random.uniform(-1, 2)*0.02
    c= complex(x,y)
    for i in range(-200,200):
        for k in range(-200,200):
            Zo = complex(i/75,k/75)
            mandlebrot(Zo,c)

    print("framee")

    pygame.display.flip()
    clock.tick(10)
    