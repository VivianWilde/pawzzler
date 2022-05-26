#!/usr/bin/env ipython3

VIEW_WIDTH = 45
VIEW_HEIGHT = 32

class Location:
    def __init__(self, name, texture="void", width=VIEW_WIDTH, height=VIEW_HEIGHT,  start=(0, 0)):#Shoudn't start be None
        self.name=name
        self.character_location = start
        self.mapdict = {}
        self.WIDTH = width
        self.HEIGHT = height
        self.texture = texture

    def add_character(self, x, y):
        self.character_location = (x, y)

    def remove_character(self):
        self.character_location = None

    def add(self, item, x, y):
        self.create_item(item, (x, y))

    def create_item(self, item, pos):
        self.mapdict[pos] = item

    def unblocked(self, pos):
        return pos in self.mapdict

    def in_range(self, pos):
        return 0 <= pos[0] <= self.WIDTH and 0 <= pos[1] <= self.HEIGHT

    def movable(self, direction):
        pos = self.to_absolute(direction)
        return self.unblocked(pos) and self.in_range(pos)

    def update(self, direction):
        self.character_location = self.to_absolute(direction) ## Please use these instead of the other two

    def try_interact(self):
        for cell in self.adjacents():
            if not self.unblocked(cell):
                self.mapdict[cell].interact()

    def adjacents(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        return map(self.to_absolute, directions)

    def objects_in_view(self):
        result = {}
        for key, value in sorted(self.mapdict.items(), key=lambda item: item[0] + self.WIDTH * item[1]):
            if value not in result.values():
                result[key] = value

    #fix this up so that objects spanning multiple blocks are only returned once
    #range query on objects


    # def get_view_bounds(self):
    #     left_range = VIEW_WIDTH//2
    #     right_range = VIEW_WIDTH - left_range - 1
    #     x_start = self.character_location[0] - left_range

    @staticmethod
    def vec_add(a, b):
        map(lambda i: a[i] + b[i], range(len(a)))

    @staticmethod
    def vec_sub(a, b):
        map(lambda i: a[i] - b[i], range(len(a)))

    def to_absolute(self, pos):
        return self.vec_add(pos, self.character_location)

    def to_relative(self, pos):
        return self.vec_sub(pos, self.character_location)

