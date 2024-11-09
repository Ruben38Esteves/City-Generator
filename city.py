from tile import Tile
from stack import Stack 
import random

class City:
    def __init__(self):
        # create 2d array
        self.matrix = []
        for y in range(0,15):
            new_line = []
            for x in range(0,15):
                new_tile = Tile(x,y)
                new_line.append(new_tile)
            self.matrix.append(new_line)

        # inform tiles of their neighboors
        for y in range(0,15):
            for x in range(0,15):
                current_tile : Tile = self.matrix[y][x]
                if x > 0:
                    current_tile.add_neighboor("left", self.matrix[y][x-1])
                if x < 14:
                    current_tile.add_neighboor("right", self.matrix[y][x+1])
                if y > 0:
                    current_tile.add_neighboor("up", self.matrix[y-1][x])
                if y < 14:
                    current_tile.add_neighboor("down", self.matrix[y+1][x])

    def get_lowest_entropy(self):
        lowest_entropy = 99
        lowest_entropy_tiles = []
        for row in self.matrix:
            for tile in row:
                entropy = tile.entropy
                if entropy < lowest_entropy and entropy != 0:
                    lowest_entropy = entropy
                    lowest_entropy_tiles = [tile]
                elif entropy == lowest_entropy:
                    lowest_entropy_tiles += [tile]
        print(lowest_entropy)
        return lowest_entropy_tiles
    
    def wave_function_collapse(self):
        lowest_entropy_tiles = self.get_lowest_entropy()
        if len(lowest_entropy_tiles) == 0:
            return True
        current_tile = random.choice(lowest_entropy_tiles)

        current_tile.collapse()

        stack = Stack()
        stack.push(current_tile)
        print(stack.stack, " is the content of the stack")

        while(stack.not_empty()):
            current_tile : Tile = stack.pop()
            for direction in current_tile.neighboors.keys():
                neighboor : Tile = current_tile.neighboors[direction]
                if neighboor.tile_type == 0:
                    inverse_direction = ""
                    match(direction):
                        case "left":
                            inverse_direction = "right"
                        case "right":
                            inverse_direction = "left"
                        case "up":
                            inverse_direction = "down"
                        case "down":
                            inverse_direction = "up"
                    updated = neighboor.update_possibilities(current_tile.possibilities, inverse_direction)
                    if updated:
                        stack.push(neighboor)
        return False