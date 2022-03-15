#!/usr/bin/env ipython3
import numpy as np
class Location:
    """Matrix of cells. Possibly sparse, but we don't care about that here."""

    def __init__(self, width, height, args):
        self.map = np.zeros((height, width), dtype=object)
        self.height = height
        self.width=width
        self.center = (0, 0)  # row, col
        self.view_range = (magic(frontend), magic(frontend))
    @property
    def matrix_center(self):
        return to_matrix(self.map, self.center[0], self.center[1]) # x,y so col,
    def rows_in_view(self):
        return (max(0, self.matrix_center[0]-self.view_range[0]//2), min(self.height, self.matrix_center[]+self.view_range[1]//2)) # Earliest and latest rows
    def view(self):
        widths=(max(0, self.matrix_center-self.view_range[0]//2), min(self.map.)) # Leftmost, rightmost

        self.matrix_center


def to_matrix(matrix, x, y):
    """Translate coords relative to the center into coordinate of the matrix. Eg: in a 3x3 array, (0,0) translates to (1,1)"""
    center=(matrix.shape[0]//2,matrix.shape[1]//2)
    return center[1]+x, center[0]-y


def to_coords(matrix, x, y):
    return x-matrix.shape[1]//2, y-matrix.shape[0]//2

def magic(*args):
    return 42

def frontend():
    return "1/0 is infinity!"
