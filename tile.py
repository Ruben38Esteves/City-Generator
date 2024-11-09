from connections import possible_connections, weights
import random

class Tile:
    tile_type : int = 0
    updated = False

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.possibilities = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.entropy = len(self.possibilities)
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

    def update_neighboors(self):
        for direction in self.neighboors.keys():
            neighboor : Tile = self.neighboors[direction]
            if neighboor.tile_type != 0:
                neighboor.update_possibilities(self.possible_connections[direction])

    def collapse(self):
        if len(self.possibilities) > 0:
            possibilities_weights = [weights[x] for x in self.possibilities]
            self.tile_type = random.choices(self.possibilities,weights=possibilities_weights, k=1)[0]
            self.possibilities = [self.tile_type]
            self.entropy = 0