import pygame
import time

pygame.init()

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Main Window")

def create_matrix():
    new_matrix = []
    for y in range(0,15):
        new_line = []
        for x in range(0,15):
            new_tile = Tile(x,y)
            new_line.append(new_tile)
        new_matrix.append(new_line)
    return new_matrix

def colour_tile(tile_type):
    match tile_type:
        case 0:
            return (0,0,0)
        case _ :
            return (255,255,255)


class Tile:
    possibilities = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    tile_type = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x:" + str(self.x) + ", y:" + str(self.y)

    def update_possibilities(self, new_possibilities):
        self.possibilities = [x for x in self.possibilities if x in new_possibilities]

    def paint_on_screen(self):
        pygame.draw.rect(screen, colour_tile(self.tile_type), pygame.Rect(self.x * 64,self.y * 64,64,64))




running = True
map_grid = create_matrix()
while running:
    screen.fill((0,0,255))

    for y in map_grid:
        for x in y:
            print(x)
            x.paint_on_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    time.sleep(1)

pygame.quit()