"""
The creator class declares the factory method that must
return an object of a product class. The creator's subclasses
usually provide the implementation of this method.
"""


class Dialog:
    """
    The creator may also provide some default implementation
    of the factory method.
    """

    def createButton(self):
        raise NotImplementedError()

    """
    Note that, despite its name, the creator's primary
    responsibility isn't creating products. It usually
    contains some core business logic that relies on product
    objects returned by the factory method. Subclasses can
    indirectly change that business logic by overriding the
    factory method and returning a different type of product
    from it.
    """

    def render(self):
        # Call the factory method to create a product object.
        okButton = self.createButton()
        # Now use the product.
        okButton.onClick(self.closeDialog)
        okButton.render()


"""
Concrete creators override the factory method to change the
resulting product's type.
"""


class WindowsDialog(Dialog):
    def createButton(self):
        return WindowsButton()


class WebDialog(Dialog):
    def createButton(self):
        return HTMLButton()


"""
The product interface declares the operations that all
concrete products must implement.
"""


class Button:
    def render(self):
        raise NotImplementedError()

    def onClick(self, f):
        raise NotImplementedError()


"""
Concrete products provide various implementations of the
product interface.
"""


class WindowsButton(Button):
    def render(self, a, b):
        # Render a button in Windows style.
        pass

    def onClick(self, f):
        # Bind a native OS click event.
        pass


class HTMLButton(Button):
    def render(self, a, b):
        # Return an HTML representation of a button.
        pass

    def onClick(self, f):
        # Bind a web browser click event.
        pass


class Application:
    def __init__(self):
        self.dialog = None

    """
    The application picks a creator's type depending on the
    current configuration or environment settings.
    """

    def initialize(self):
        config = self.readApplicationConfigFile()

        if config.OS == "Windows":
            self.dialog = WindowsDialog()
        elif config.OS == "Web":
            self.dialog = WebDialog()
        else:
            raise Exception("Error! Unknown operating system.")

    """
    The client code works with an instance of a concrete
    creator, albeit through its base interface. As long as
    the client keeps working with the creator via the base
    interface, you can pass it any creator's subclass.
    """

    def main(self):
        self.initialize()
        self.dialog.render()

    def readApplicationConfigFile(self):
        return None

    def closeDialog(self):
        pass


# The client code can work with any concrete creator class.
def clientCode(creator: Dialog):
    print("Client: I'm not aware of the creator's class,"
          "but it still works.\n" + creator.someOperation())


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    clientCode(ConcreteCreator1())
    print("")

    print("App: Launched with the ConcreteCreator2.")
    clientCode(ConcreteCreator2())

