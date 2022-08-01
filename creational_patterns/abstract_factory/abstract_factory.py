"""
The abstract factory interface declares a set of methods that
return different abstract products. These products are called
a family and are related by a high-level theme or concept.
Products of one family are usually able to collaborate among
themselves. A family of products may have several variants,
but the products of one variant are incompatible with the
products of another variant.
"""


class GUIFactory:
    def createButton(self):
        pass

    def createCheckbox(self):
        pass


"""
Concrete factories produce a family of products that belong
to a single variant. The factory guarantees that the
resulting products are compatible. Signatures of the concrete
factory's methods return an abstract product, while inside
the method a concrete product is instantiated.
"""


class WinFactory(GUIFactory):
    def createButton(self):
        return WinButton()

    def createCheckbox(self):
        return WinCheckbox()


"""
Each concrete factory has a corresponding product variant.
"""


class MacFactory(GUIFactory):
    def createButton(self):
        return MacButton()

    def createCheckbox(self):
        return MacCheckbox()


"""
Each distinct product of a product family should have a base
interface. All variants of the product must implement this
interface.
"""


class Button:
    def paint(self):
        pass


"""
Concrete products are created by corresponding concrete
factories.
"""


class WinButton(Button):
    def paint(self):
        # Render a button in Windows style.
        pass


class MacButton(Button):
    def paint(self):
        # Render a button in macOS style.
        pass


"""
Here's the base interface of another product. All products
can interact with each other, but proper interaction is
possible only between products of the same concrete variant.
"""


class Checkbox:
    def paint(self):
        pass


class WinCheckbox(Checkbox):
    def paint(self):
        # Render a checkbox in Windows style.
        pass


class MacCheckbox(Checkbox):
    def paint(self):
        # Render a checkbox in macOS style.
        pass


"""
The client code works with factories and products only
through abstract types: GUIFactory, Button and Checkbox. This
lets you pass any factory or product subclass to the client
code without breaking it.
"""


class Application:
    def __init__(self, factory):
        self.factory = factory
        self.button = None

    def createUI(self):
        self.button = self.factory.createButton()

    def paint(self):
        self.button.paint()


"""
The application picks the factory type depending on the
current configuration or environment settings and creates it
at runtime (usually at the initialization stage).
"""


class ApplicationConfigurator:
    def main(self):
        config = readApplicationConfigFile()

        if config.OS == "Windows":
            factory = WinFactory()
        elif config.OS == "Mac":
            factory = MacFactory()
        else:
            raise Exception("Error! Unknown operating system.")

        app = Application(factory)
