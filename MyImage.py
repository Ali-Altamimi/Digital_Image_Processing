import my_io


class MyImage:

    def __init__(self, name, dimensions, path=None):
        self.name = name
        self.path = path
        self.dimensions = dimensions
        self.size = dimensions[0]* dimensions[1]
        if(path == None):
            self.matrix = 0
        else:
            self.matrix = my_io.read(path, dimensions)

