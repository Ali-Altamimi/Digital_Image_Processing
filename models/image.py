import utilities.io as io
import matplotlib.pyplot as plt
# import numpy as np
from scipy import ndimage


class Image:
    def __init__(self, name:str, dimensions:list=None, path:str=None, matrix:list=None, dtype=None):
        self.name = name
        self.path = path
        self.dimensions = dimensions
        self.size = dimensions[0]* dimensions[1]
        self.dtype = dtype
        if(matrix == None):
            if(path == None):
                self.matrix = None
            else:
                self.matrix = io.read(path, dimensions)
        else:
            self.matrix = matrix
    @classmethod
    def exist(cls, name:str, matrix:list):
        return cls(name, dimensions=[len(matrix[0]), len(matrix[1])], matrix=matrix)
    
    def display(self, cmap='gray'):
        plt.figure()
        rotated_img = ndimage.rotate(self.matrix[::-1], -90)
        plt.imshow(rotated_img, cmap)
        plt.title(self.name)
        # plt.xticks(rotation=90)

        plt.show()


    def write(self):
        io.write(self)

