"""Shapes."""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """General shape class."""

    def __init__(self, color: str):
        """Shape constructor."""
        self.color = color

    def set_color(self, color: str):
        """Set the color of the shape."""
        self.color = color

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self.color

    @abstractmethod
    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        print("Implement area")
        pass


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Circle constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        super().__init__(color)
        self.radius = radius

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return f"Circle (r: {self.radius}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        area = float(pi * self.radius ** 2)
        return area


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Square constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        super().__init__(color)
        self.side = side

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Square (a: {self.side}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        area = float(self.side * self.side)
        return area


class Rectangle(Shape):
    """Rectangle is a subclass of Shape."""

    def __init__(self, color: str, width: float, height: float):
        """Initialize Rectangle."""
        super().__init__(color)
        self.width = width
        self.height = height

    def __repr__(self):
        """Return representation of the rectangle."""
        return f"Rectangle (l: {self.width}, w: {self.height}, color: {self.color})"

    def get_area(self) -> float:
        """Calculate the area of the rectangle."""
        return float(self.width * self.height)


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Paint constructor."""
        self.shapes = []

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        self.shapes.append(shape)

    def get_shapes(self) -> list:
        """Return all the shapes."""
        return self.shapes

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        total_area = 0
        for shape in self.shapes:
            total_area += shape.get_area()
        return total_area

    def get_circles(self) -> list:
        """Return only circles."""
        circles_list = []
        for shape in self.shapes:
            if isinstance(shape, Circle):
                circles_list.append(shape)
        return circles_list

    def get_squares(self) -> list:
        """Return only squares."""
        squares_list = []
        for shape in self.shapes:
            if isinstance(shape, Square):
                squares_list.append(shape)
        return squares_list

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        rectangles_list = []
        for shape in self.shapes:
            if isinstance(shape, Rectangle):
                rectangles_list.append(shape)
        return rectangles_list


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    paint.add_shape(circle)
    paint.add_shape(square)
    print(paint.calculate_total_area())
    print(paint.get_circles())
