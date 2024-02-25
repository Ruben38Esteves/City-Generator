import pygame

pygame.init()

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Main Window")

def get_color(i, j):
    color = (255, (255 * i)//SCREEN_WIDTH, (255 * j)//SCREEN_HEIGHT)
    return color

def paint_screen():
    for i in range(0,SCREEN_WIDTH,64):
        for j in range(0,SCREEN_WIDTH,64):
            pygame.draw.rect(screen, get_color(i,j), pygame.Rect(i,j,64,64))

class tile:
    possibilities = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def update_possibilities(self, new_possibilities):
        self.possibilities = [x for x in self.possibilities if x in new_possibilities]




running = True
while running:
    screen.fill((0,0,0))

    paint_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()