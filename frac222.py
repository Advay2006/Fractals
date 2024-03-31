import pygame, sys, math

def color_pixel(surface, color, pos):
    surface.fill(color, (pos, (1, 1)))

def mandlebrot(c,n):
    global max_iter, scale,rfac,bfac,gfac
    z = Zo
    iter=0
    while abs(z)<=2 and iter<max_iter:
        z = z**n + c
        iter+=1
    if iter == max_iter:
        color_pixel(screen, (0,0,0), (screen_width/2+c.real*scale, screen_height/2-c.imag*scale))
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
        color_pixel(screen, (rshade,bshade,gshade),(screen_width/2+c.real*scale, screen_height/2-c.imag*scale))



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

#FIDDLE ARRROUUNNNDDD############
Zo = 0
scale = 90
max_iter = 80
expo = 0
#################################


rfac,bfac,gfac = 10,5,5
no=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
    
    for i in range(-200,200):
        for k in range(-100,100):
            c = complex(i/100,k/100)
            mandlebrot(c,expo)
    expo+=0.1
    no+=1
    #pygame.image.save(screen,"C:/Users/Ritul/Documents/Advay/Python/FRACTALImage{}.jpeg".format(no))


    print("framee")

    pygame.display.flip()
    
    clock.tick(5)
