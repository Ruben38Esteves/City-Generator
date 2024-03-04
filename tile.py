class Tile:
    possibilities = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    tile_type : int = 0
    updated = False

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x:" + str(self.x) + ", y:" + str(self.y)

    def update_possibilities(self, new_possibilities):
        self.updated = True
        save_for_debug = self.possibilities
        self.possibilities = [x for x in self.possibilities if x in new_possibilities]
        #self.update_possible_neighboors()
        if len(self.possibilities) == 1:
            self.collapse()
        elif len(self.possibilities) == 0:
            print(save_for_debug)
            print(new_possibilities)
        """
        if len(self.possibilities) == 0:
            self.possibilities =  save_for_debug
            print("conflicts")
            
            print(self)
            print(save_for_debug)
            print(new_possibilities)
            pygame.quit()
            """

    def paint_on_screen(self):
        if self.tile_type >= 1 :
            screen.blit(get_tile_image(self.tile_type),(self.x *64,self.y * 64))
        else:
            text = my_font.render(str(len(self.possibilities)), False, (255, 255, 255))
            screen.blit(text, (self.x *64,self.y * 64))
            #pygame.draw.rect(screen, colour_tile(self.tile_type), pygame.Rect(self.x * 64,self.y * 64,64,64))

    def update_possible_neighboors(self):
        if self.x > 0 :
            if map_grid[self.y][self.x - 1].tile_type == 0: #and map_grid[self.y + 1][self.x - 1].updated == False:
                map_grid[self.y][self.x - 1].update_possibilities(possible_connections[self.tile_type - 1]["left"])
        if self.x < 14 :
            if map_grid[self.y][self.x + 1].tile_type == 0: #and map_grid[self.y + 1][self.x - 1].updated == False:
                map_grid[self.y][self.x + 1].update_possibilities(possible_connections[self.tile_type - 1]["right"])
        if self.y > 0:
            if map_grid[self.y - 1][self.x].tile_type == 0: #and map_grid[self.y + 1][self.x - 1].updated == False:
                map_grid[self.y - 1][self.x].update_possibilities(possible_connections[self.tile_type - 1]["up"])
        if self.y < 14:
            if map_grid[self.y + 1][self.x - 1].tile_type == 0: #and map_grid[self.y + 1][self.x - 1].updated == False:
                map_grid[self.y + 1][self.x].update_possibilities(possible_connections[self.tile_type - 1]["down"])


    def collapse(self):
        if len(self.possibilities) > 0:
            self.tile_type = random.choice(self.possibilities)
            #print("x:" + str(self.x) + ", y:" + str(self.y) + "    became: " + str(self.tile_type))
            #update_map(self.x, self.y)~
            self.update_possible_neighboors()