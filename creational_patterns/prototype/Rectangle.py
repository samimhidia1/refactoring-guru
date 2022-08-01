"""
Concrete prototype. The cloning method creates a new object
in one go by calling the constructor of the current class and
passing the current object as the constructor's argument.
Performing all the actual copying in the constructor helps to
keep the result consistent: the constructor will not return a
result until the new object is fully built; thus, no object
can have a reference to a partially-built clone.
"""
from creational_patterns.prototype.Shape import Shape


class Rectangle(Shape):
    def __init__(self):
        self._width = None
        self._height = None

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    """
    A parent constructor call is needed to copy private
    fields defined in the parent class.
    """

    def __init__(self, source):
        super().__init__(source)
        self.width = source.width
        self.height = source.height

    def clone(self):
        return Rectangle(self)
