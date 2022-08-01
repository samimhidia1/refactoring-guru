"""
Using the Builder pattern makes sense only when your products
are quite complex and require extensive configuration. The
following two products are related, although they don't have
a common interface.
"""
class Car:
    # A car can have a GPS, trip computer and some number of
    # seats. Different models of cars (sports car, SUV,
    # cabriolet) might have different features installed or
    # enabled.
    pass

class Manual:
    # Each car should have a user manual that corresponds to
    # the car's configuration and describes all its features.
    def __int__(self):




"""
The builder interface specifies methods for creating the
different parts of the product objects.
"""
class Builder:
    def reset(self):
        pass

    def setSeats(self, seats):
        pass

    def setEngine(self, engine):
        pass

    def setTripComputer(self, tripComputer):
        pass

    def setGPS(self, gps):
        pass

"""
The concrete builder classes follow the builder interface and
provide specific implementations of the building steps. Your
program may have several variations of builders, each
implemented differently.
"""
class CarBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.car = Car()

    # All production steps work with the same product instance.
    def setSeats(self, seats):
        # Set the number of seats in the car.
        pass

    def setEngine(self, engine):
        # Install a given engine.
        pass

    def setTripComputer(self, tripComputer):
        # Install a trip computer.
        pass

    def setGPS(self, gps):
        # Install a global positioning system.
        pass

    # Concrete builders are supposed to provide their own
    # methods for retrieving results. That's because various
    # types of builders may create entirely different products
    # that don't all follow the same interface. Therefore such
    # methods can't be declared in the builder interface (at
    # least not in a statically-typed programming language).
    #
    # Usually, after returning the end result to the client, a
    # builder instance is expected to be ready to start
    # producing another product. That's why it's a usual
    # practice to call the reset method at the end of the
    # `getProduct` method body. However, this behavior isn't
    # mandatory, and you can make your builder wait for an
    # explicit reset call from the client code before disposing
    # of the previous result.
    def getProduct(self):
        product = self.car
        self.reset()
        return product

"""
Unlike other creational patterns, builder lets you construct
products that don't follow the common interface.
"""
class CarManualBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.manual = Manual()

    def setSeats(self, seats):
        # Document car seat features.
        pass

    def setEngine(self, engine):
        # Add engine instructions.
        pass

    def setTripComputer(self, tripComputer):
        # Add trip computer instructions.
        pass

    def setGPS(self, gps):
        # Add GPS instructions.
        pass

    def getProduct(self):
        # Return the manual and reset the builder.
        pass

"""
The director is only responsible for executing the building
steps in a particular sequence. It's helpful when producing
products according to a specific order or configuration.
Strictly speaking, the director class is optional, since the
client can control builders directly.
"""
class Director:
    def __init__(self):
        self.builder = None

    # The director works with any builder instance that the
    # client code passes to it. This way, the client code may
    # alter the final type of the newly assembled product.
    def setBuilder(self, builder):
        self.builder = builder

    # The director can construct several product variations
    # using the same building steps.
    def constructSportsCar(self, builder):
        builder.reset()
        builder.setSeats(2)
        builder.setEngine(SportEngine())
        builder.setTripComputer(True)
        builder.setGPS(True)

    def constructSUV(self, builder):
        # ...

"""
The client code creates a builder object, passes it to the
director and then initiates the construction process. The end
result is retrieved from the builder object.
"""
class Application:
    def makeCar(self):
        director = Director()

        builder = CarBuilder()
        director.constructSportsCar(builder)
        car = builder.getProduct()

        builder = CarManualBuilder()
        director.constructSportsCar(builder)

        # The final product is often retrieved from a builder
        # object since the director isn't aware of and not
        # dependent on concrete builders and products.
        manual = builder.getProduct()