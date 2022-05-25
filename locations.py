#!/usr/bin/env ipython3
class Location:
    def __init__(self, width=100, height=100, texture="void", start=(0, 0)):
        self.loc = start
        self.mapdict = {}
        self.WIDTH = width
        self.HEIGHT = height
        self.texture = texture

    def add_character(self, x, y):
        self.loc = (x, y)

    def remove_character(self):
        self.loc = None

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
        self.loc = self.to_absolute(direction)

    def try_interact(self):
        for cell in self.adjacents():
            if not self.unblocked(cell):
                self.mapdict[cell].interact()

    def adjacents(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        return map(self.to_absolute, directions)

    @staticmethod
    def vec_add(a, b):
        map(lambda i: a[i] + b[i], range(len(a)))

    @staticmethod
    def vec_sub(a, b):
        map(lambda i: a[i] - b[i], range(len(a)))

    def to_absolute(self, pos):
        return self.vec_add(pos, self.loc)

    def to_relative(self, pos):
        return self.vec_sub(pos, self.loc)
