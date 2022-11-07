
import pygame
from pygame.locals import *
 
pygame.init()
clock = pygame.time.Clock()
size = 1920, 1080
BLACK = 0, 0, 0
speed = 10
screen = pygame.display.set_mode(size,0,32)
pygame.display.set_caption('GAME')
IsaacPosX, IsaacPosY = 960, 540
TearPosX, TearPosY = 960, 540
 
IsaacSprite=pygame.image.load('nino.png')
TearSprite=pygame.image.load('tacos.png')
loop = True
while loop:
    # this adds the sprite at every frame rate
    screen.fill(BLACK)
    screen.blit(IsaacSprite,(IsaacPosX,IsaacPosY))
 
    for event in pygame.event.get():
        # this is to close the window
        if event.type==QUIT:
            loop = False
            #sys.exit() # this will close the kernel too
            # in development mode leave the comment above
    # this is the list with the keys being pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        IsaacPosX -= speed
    if keys[pygame.K_d]:
        IsaacPosX += speed
    if keys[pygame.K_z]:
        IsaacPosY -= speed
    if keys[pygame.K_s]:
        IsaacPosY += speed

    if keys[pygame.K_LEFT]:
        TearPosX = IsaacPosX
        TearPosY = IsaacPosY
        screen.blit(TearSprite,(TearPosX,TearPosY))
        #for i in range(5):
        #    TearPosX -= speed

    if keys[pygame.K_RIGHT]:
        TearPosX = IsaacPosX
        TearPosY = IsaacPosY
        screen.blit(TearSprite,(TearPosX,TearPosY))
    if keys[pygame.K_UP]:
        TearPosX = IsaacPosX
        TearPosY = IsaacPosY
        screen.blit(TearSprite,(TearPosX,TearPosY)) 
    if keys[pygame.K_DOWN]:
        TearPosX = IsaacPosX
        TearPosY = IsaacPosY
        screen.blit(TearSprite,(TearPosX,TearPosY))

    # we update the screen at every frame
    pygame.display.flip()
    # if we put the frame rate at 60 the sprite will move slower
    clock.tick(120)
 
pygame.quit()
