from connections import possible_connections
import random

class Tile:
    tile_type : int = 0
    updated = False

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.possibilities = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.entropy = len(self.possibilities)

        self.possible_connections = {
            "left":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
            "right":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
            "up":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
            "down":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        }
        self.neighboors = {}

    def __str__(self):
        return "x:" + str(self.x) + ", y:" + str(self.y)
    
    def __repr__(self):
        return f"Tile(x={self.x}, y={self.y})"
    
    def add_neighboor(self,direction,tile):
        self.neighboors[direction] = tile

    def update_possibilities(self, neighboor_possibilities, direction):

        old_entropy = len(self.possibilities)
        new_possibilities = []
        for a in self.possibilities:
            can_connect = False
            for b in neighboor_possibilities:
                if b in possible_connections[a][direction]:
                    can_connect = True
            if can_connect:
                new_possibilities += [a]
                can_connect = False
        
        self.possibilities = new_possibilities
        self.entropy = len(self.possibilities)

        updated = old_entropy != self.entropy
        return updated



    def update_possibilities_2(self, new_possibilities):
        print("update_possibilities")
        old_entropy = self.entropy
        self.possibilities = [x for x in self.possibilities if x in new_possibilities]
        self.entropy = len(self.possibilities)

        new_left = []
        new_right = []
        new_up = []
        new_down = []
        for x in self.possibilities.copy():
            new_left += [i for i in possible_connections[x]["left"] if i not in new_left]
            new_right += [i for i in possible_connections[x]["right"] if i not in new_right]
            new_up += [i for i in possible_connections[x]["up"] if i not in new_up]
            new_down += [i for i in possible_connections[x]["down"] if i not in new_down]

        self.possible_connections["left"] = new_left.copy()
        self.possible_connections["right"] = new_right.copy()
        self.possible_connections["up"] = new_up.copy()
        self.possible_connections["down"] = new_down.copy()

        updated = old_entropy != self.entropy
        return updated

    def update_neighboors(self):
        for direction in self.neighboors.keys():
            neighboor : Tile = self.neighboors[direction]
            if neighboor.tile_type != 0:
                neighboor.update_possibilities(self.possible_connections[direction])

    def collapse(self):
        print("collapsing: ",self)
        if len(self.possibilities) > 0:
            self.tile_type = random.choice(self.possibilities)
            self.possibilities = [self.tile_type]
            self.entropy = 0
            # self.possible_connections["left"] = possible_connections[self.tile_type]["left"]
            # self.possible_connections["right"] = possible_connections[self.tile_type]["right"]
            # self.possible_connections["up"] = possible_connections[self.tile_type]["up"]
            # self.possible_connections["down"] = possible_connections[self.tile_type]["down"]
            # self.update_neighboors()