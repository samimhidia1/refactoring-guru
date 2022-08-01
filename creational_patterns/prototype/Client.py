from creational_patterns.prototype.Circle import Circle
from creational_patterns.prototype.Rectangle import Rectangle


class Application:
    def __init__(self):
        self._shapes = []

        circle = Circle()
        circle.x = 10
        circle.y = 10
        circle.radius = 20
        self._shapes.append(circle)

        another_circle = circle.clone()
        self._shapes.append(another_circle)
        # The `anotherCircle` variable contains an exact copy
        # of the `circle` object.

        rectangle = Rectangle()
        rectangle.width = 10
        rectangle.height = 20
        self._shapes.append(rectangle)

    def business_logic(self):
        # Prototype rocks because it lets you produce a copy of
        # an object without knowing anything about its type.
        shapes_copy = []

        # For instance, we don't know the exact elements in the
        # shapes array. All we know is that they are all
        # shapes. But thanks to polymorphism, when we call the
        # `clone` method on a shape the program checks its real
        # class and runs the appropriate clone method defined
        # in that class. That's why we get proper clones
        # instead of a set of simple Shape objects.
        for s in self._shapes:
            shapes_copy.append(s.clone())

        # The `shapesCopy` array contains exact copies of the
        # `shape` array's children.


if __name__ == "__main__":
    # The client code.
    shapes = [
        Circle(10, 10, 20),
        Rectangle(10, 20, 30, 40),
        Circle(100, 100, 50),
    ]

    shapes_copy = []

    for shape in shapes:
        shapes_copy.append(shape.clone())

    for i in range(len(shapes)):
        if shapes[i] is shapes_copy[i]:
            print(f"Shape {i}: Both objects are the same instance")
        else:
            if shapes[i] == shapes_copy[i]:
                print(f"Shape {i}: Both objects are copies")
            else:
                print(f"Shape {i}: Objects are different")
