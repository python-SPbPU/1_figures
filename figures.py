class Rectangle:
    def __init__(self, width, height, x=0, y=0):
        self._width = width
        self._height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        """Sets a new width for the rectangle"""
        self._width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        """Sets a new height for the rectangle"""
        self._height = value

    def area(self):
        return self.width * self.height

    def perimetr(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return (f"Прямоугольник с координатами ({self.x},{self.y}), "
                f"сторонами {self.width} и {self.height}, "
                f"площадью {self.area()} и периметром {self.perimetr()}")



class Square(Rectangle):
    def __init__(self, side, x=0, y=0):
        super().__init__(side, side, x, y)

    @property
    def width(self):
        """Returns the length for the side of the square"""
        return self._width

    @width.setter
    def width(self, value):
        """Sets a new lenght for the side of the square"""
        self._width = self._height = value

    @property
    def height(self):
        """Returns the length for the side of the square"""
        return self._height

    @height.setter
    def height(self, value):
        """Sets a new lenght for the side of the square"""
        self._width = self._height = value

    def __repr__(self):
        return (f"Квадрат с координатами ({self.x}, {self.y}), "
                f"стороной {self.width}, площадью {self.area()} и периметром {self.perimetr()}")

def resize_shape(shapes: list[Rectangle]):
    """Doubles the width of each shape in the list.
    :param shapes: list[Rectangle] - A list of objects inheriting from the Rectangle class,
                                        which may include both rectangles and squares.
    :return: None - The function modifies the width of the shapes in the provided list in place."""
    for shape in shapes:
        shape.width *= 2

if __name__ == '__main__':
    """Entry point of the program.

    Creates a list of shapes and doubles the width of each shape using the 
    resize_shape function. Then prints the characteristics 
    of each shape in the list to the console."""
    figures = [Rectangle(2, 3), Square(2, 1, 1)]
    resize_shape(figures)
    for figure in figures:
        print(figure)





