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


class Circle(Shape):
    def __init__(self):
        self._radius = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    def __init__(self, source):
        super().__init__(source)
        self.radius = source.radius

    def clone(self):
        return Circle(self)
