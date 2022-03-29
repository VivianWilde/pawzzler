#!/usr/bin/env ipython3
import numpy as np


class Location:
    """Matrix of cells. Possibly sparse, but we don't care about that here."""

    def __init__(self, width, height, args):
        self.map = np.zeros((height, width), dtype=object)
        self.height = height
        self.width = width
        self.loc = (0, 0)  # x,y
        self.view_range = (magic(frontend), magic(frontend))

    @property
    def row_range(self):
        return self.view_range[1]

    def col_range(self):
        return self.view_range[0]

    @property
    def center(self):
        return center(self.map)

    def field_in_view(self, idx, converter):
        "Given an index (0 for x, 1 for y) and a converter (to translate to indices), return the lower and upper bounds on the number of FIELDs player should see, as matrix coordinates."
        x = converter(self.map, self.loc[idx])
        return max(0, x - self.view_range[idx] / 2), min(
            self.map.shape[idx ^ 1], x + self.view_range[idx] / 2
        )

    @property
    def rows_in_view(self):
        """Highest and lowest rows in view"""
        return self.field_in_view(1, to_row)

    @property
    def cols_in_view(self):
        """Left- and rightmost cols in view"""
        return self.field_in_view(0, to_col)

    def view(self):
        """Return the slice of the map which should be visible to the player, given that they are at CURRENT_LOC. CURRENT_LOC is also the center of this new matrix"""
        return self.map[
            self.rows_in_view[0] : self.rows_in_view[1],
            self.cols_in_view[0] : self.cols_in_view[1],
        ]

    def get(self, x, y):
        return get(self.map, x, y)

    def set(self, x, y, val):
        return set(self.map, x, y, val)


def center(m):
    """Return center of the matrix in x,y format."""
    return m.shape[1] // 2, m.shape[0] // 2


def get(m, x, y):
    indices = to_indices(m, x, y)
    return m[indices[0]][indices[1]]


def set(m, x, y, val):
    indices = to_indices(m, x, y)
    m[indices[0]][indices[1]] = val


def to_col(m, x):
    return center(m)[0] - x


def to_row(m, y):
    return center(m)[1] - y


def to_x(m, c):
    return c - center(m)[1]


def to_y(m, r):
    return r - center(m)[0]


def to_indices(m, x, y):
    """Translate coords relative to the center into coordinate of the matrix. Eg: in a 3x3 array, (0,0) translates to (1,1)"""
    return to_row(m, y), to_col(m, x)


def to_coords(m, r, c):
    """Inverse of to_indices. Translate matrix index coordinates into x,y coordinates, treating the center of the matrix as the origin."""
    return to_x(m, c), to_y(m, r)


def magic(*args):
    return 42


def frontend(*args):
    return "1/0 is infinity!"
