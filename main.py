import pygame
import time
import random

pygame.init()

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Main Window")


possible_connections = [
    #1
    {
        "up": [10,11,14],
        "down" : [2,16],
        "left" : [1,8],
        "right" : [1,7]
    },
    #2
    {
        "up": [1,16],
        "down" : [10,12,15],
        "left" : [2,6],
        "right" : [2,5]
    },
    #3
    {
        "up": [3,7],
        "down" : [3,5],
        "left" : [4,16],
        "right" : [9,11,12]
    },
    #4
    {
        "up": [4,8],
        "down" : [4,6],
        "left" : [9,11,12],
        "right" : [3,16]
    },
    #5
    {
        "up": [3,7],
        "down" : [10,12,15],
        "left" : [2,6],
        "right" : [9,14,15]
    },
    #6
    {
        "up": [4,8],
        "down" : [10,12,15],
        "left" : [9,11,12],
        "right" : [2,5]
    },
    #7
    {
        "up": [10,11,14],
        "down" : [3,5],
        "left" : [1,8],
        "right" : [9,14,15]
    },
    #8
    {
        "up": [10,11,14],
        "down" : [4,6],
        "left" : [9,11,12],
        "right" : [1,7]
    },
    #9
    {
        "up": [9,12,13,15],
        "down" : [9,11,13,14],
        "left" : [3,5,7,9,11,12],
        "right" : [4,6,8,9,14,15]
    },
    #10
    {
        "up": [2,5,6,10,11,14],
        "down" : [1,7,8,10,12,15],
        "left" : [10,13,14,15],
        "right" : [10,11,12,13]
    },
    #11
    {
        "up": [9,12,13,15],
        "down" : [1,7,8,10,12,15],
        "left" : [10,13,14,15],
        "right" : [4,6,8,9,14,15]
    },
    #12
    {
        "up": [2,5,6,10,11,14],
        "down" : [9,11,13,14],
        "left" : [10,13,14,15],
        "right" : [4,6,8,9,14,15]
    },
    #13
    {
        "up": [9,12,15],
        "down" : [9,11,14],
        "left" : [10,14,15],
        "right" : [10,11,12]
    },
    #14
    {
        "up": [9,12,15],
        "down" : [1,7,8,10,12,15],
        "left" : [3,5,7,9,11,12],
        "right" : [10,11,12,13]
    },
    #15
    {
        "up": [2,5,6,10,11,14],
        "down" : [9,11,13,14],
        "left" : [3,5,7,9,11,12],
        "right" : [10,11,12,13]
    },
    #16
    {
        "up": [1],
        "down" : [2],
        "left" : [4],
        "right" : [3]
    }
]

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


class Tile:
    possibilities = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    tile_type = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x:" + str(self.x) + ", y:" + str(self.y)

    def update_possibilities(self, new_possibilities):
        save_for_debug = self.possibilities
        self.possibilities = [x for x in self.possibilities if x in new_possibilities]
        if len(self.possibilities) == 1:
            self.collapse()
        if len(self.possibilities) == 0:
            self.possibilities = new_possibilities
            """
            print(self)
            print(save_for_debug)
            print(new_possibilities)
            pygame.quit()
            """

    def paint_on_screen(self):
        if self.tile_type >= 1 :
            print("should paint a tile")
            screen.blit(get_tile_image(self.tile_type),(self.x *64,self.y * 64))
        else:
            pygame.draw.rect(screen, colour_tile(self.tile_type), pygame.Rect(self.x * 64,self.y * 64,64,64))

    def collapse(self):
        print(self.possibilities)
        if len(self.possibilities) > 0:
            self.tile_type = random.choice(self.possibilities)
            print("x:" + str(self.x) + ", y:" + str(self.y) + "    became: " + str(self.tile_type))
            if self.x > 0 :
                if map_grid[self.y][self.x - 1].tile_type == 0:
                    map_grid[self.y][self.x - 1].update_possibilities(possible_connections[self.tile_type - 1]["left"])
            if self.x < 14 :
                if map_grid[self.y][self.x + 1].tile_type == 0:
                    map_grid[self.y][self.x + 1].update_possibilities(possible_connections[self.tile_type - 1]["right"])
            if self.y > 0:
                if map_grid[self.y - 1][self.x].tile_type == 0:
                    map_grid[self.y - 1][self.x].update_possibilities(possible_connections[self.tile_type - 1]["up"])
            if self.y < 14:
                if map_grid[self.y + 1][self.x - 1].tile_type == 0:
                    map_grid[self.y + 1][self.x].update_possibilities(possible_connections[self.tile_type - 1]["down"])

def check_complete():
    for y in map_grid:
        for x in y:
            if x.tile_type == 0:
                return False
    return True

def collapse_random():
    rand_x = random.randrange(0,15)
    rand_y = random.randrange(0,15)
    map_grid[rand_y][rand_x].collapse()

def collapse_min_options():
    chosen = [-1,-1,99]
    for y in map_grid:
        for current_tile in y:
            if current_tile.tile_type == 0:
                if len(current_tile.possibilities) < chosen[2]:
                    chosen[2] = len(current_tile.possibilities)
                    chosen[0] = current_tile.x
                    chosen[1] = current_tile.y
    print("collapsed: (" + str(chosen[0]) + ", " + str(chosen[1]) + ")")
    map_grid[chosen[1]][chosen[0]].collapse()


running = True
map_grid = create_matrix()

collapse_random()

image1 = pygame.image.load('tile_1.png')
image2 = pygame.image.load('tile_2.png')
image3 = pygame.image.load('tile_3.png')
image4 = pygame.image.load('tile_4.png')
image5 = pygame.image.load('tile_5.png')
image6 = pygame.image.load('tile_6.png')
image7 = pygame.image.load('tile_7.png')
image8 = pygame.image.load('tile_8.png')
image9 = pygame.image.load('tile_9.png')
image10 = pygame.image.load('tile_10.png')
image11 = pygame.image.load('tile_11.png')
image12 = pygame.image.load('tile_12.png')
image13 = pygame.image.load('tile_13.png')
image14 = pygame.image.load('tile_14.png')
image15 = pygame.image.load('tile_15.png')
image16 = pygame.image.load('tile_16.png')

while running:
    screen.fill((0,0,255))

    for y in map_grid:
        for x in y:
            x.paint_on_screen()

    if not check_complete():
        collapse_min_options()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    time.sleep(0.2)

pygame.quit()