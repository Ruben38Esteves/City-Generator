from city import City
import random
import pygame
import time

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Main Window")

def colour_tile(tile_type):
    match tile_type:
        case 0:
            return (100,100,100)
        case 1:
            return (255,255,255)
        case 2:
            return (0,100,0)
        case 3:
            return (0,0,100)
        case 4:
            return (100,100,0)
        case 5:
            return (100,0,100)
        case 6:
            return (0,100,100)
        case 7:
            return (100,255,100)
        case 8:
            return (200,0,0)
        case 9:
            return (0,200,0)
        case 10:
            return (0,0,200)
        case 11:
            return (200,200,0)
        case 12:
            return (200,0,200)
        case 13:
            return (0,200,200)
        case 14:
            return (200,200,200)
        case 15:
            return (255,0,0)
        case 16:
            return (0,0,255)
        case _ :
            return (255,255,255)

def get_tile_image(tile_type):
    match tile_type:
        case 1:
            return image1
        case 2:
            return image2
        case 3:
            return image3
        case 4:
            return image4
        case 5:
            return image5
        case 6:
            return image6
        case 7:
            return image7
        case 8:
            return image8
        case 9:
            return image9
        case 10:
            return image10
        case 11:
            return image11
        case 12:
            return image12
        case 13:
            return image13
        case 14:
            return image14
        case 15:
            return image15
        case 16:
            return image16
        case 17:
            return image17
        case 18:
            return image18
        case 19:
            return image19
        case 20:
            return image20

def paint_on_screen(tile):
        if tile.tile_type >= 1 :
            screen.blit(get_tile_image(tile.tile_type),(tile.x *64,tile.y * 64))
        else:
            text = my_font.render(str(tile.entropy), False, (255, 255, 255))
            screen.blit(text, (tile.x *64,tile.y * 64))


running = True
city = City()

image1 =  pygame.image.load('tiles/tile_1.png')
image2 =  pygame.image.load('tiles/tile_2.png')
image3 =  pygame.image.load('tiles/tile_3.png')
image4 =  pygame.image.load('tiles/tile_4.png')
image5 =  pygame.image.load('tiles/tile_5.png')
image6 =  pygame.image.load('tiles/tile_6.png')
image7 =  pygame.image.load('tiles/tile_7.png')
image8 =  pygame.image.load('tiles/tile_8.png')
image9 =  pygame.image.load('tiles/tile_9.png')
image10 = pygame.image.load('tiles/tile_10.png')
image11 = pygame.image.load('tiles/tile_11.png')
image12 = pygame.image.load('tiles/tile_12.png')
image13 = pygame.image.load('tiles/tile_13.png')
image14 = pygame.image.load('tiles/tile_14.png')
image15 = pygame.image.load('tiles/tile_15.png')
image16 = pygame.image.load('tiles/tile_16.png')
image17 = pygame.image.load('tiles/tile_17.png')
image18 = pygame.image.load('tiles/tile_18.png')
image19 = pygame.image.load('tiles/tile_19.png')
image20 = pygame.image.load('tiles/tile_20.png')

def check_complete():
    for y in city.matrix:
        for x in y:
            if x.tile_type == 0:
                return False
    return True

while running:
    screen.fill((0,0,0))

    for y in city.matrix:
        for x in y:
            paint_on_screen(x)

    finished = False
    if not finished:
        finished = city.wave_function_collapse()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    pygame.display.update()
    #4time.sleep(0.2)
pygame.quit()