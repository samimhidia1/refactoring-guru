"""
Concrete prototype. The cloning method creates a new object
in one go by calling the constructor of the current class and
passing the current object as the constructor's argument.
Performing all the actual copying in the constructor helps to
keep the result consistent: the constructor will not return a
result until the new object is fully built; thus, no object
can have a reference to a partially-built clone.
"""

class Shape:
    def __init__(self):
        self._x = None
        self._y = None
        self._color = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    """
    The prototype constructor. A fresh object is initialized
    with values from the existing object.
    """

    def __init__(self, source):
        self.x = source.x
        self.y = source.y
        self.color = source.color

    """
    The clone operation returns one of the Shape subclasses.
    """

    def clone(self):
        pass
