"""step1. creat a class Car"""
class Car:
    """A safer model of a car using encapsulation."""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        # 1. privatize the odometer_reading
        self._odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    # 2. Getter: provide a public, read-only method to get odometer information.
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self._odometer_reading} miles on it.")

    # 3. Setter: Provide a safety method to update the mileage.
    def update_odometer(self,mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts tp roll the odometer back
        :param mileage:
        :return:
        """
        if mileage >= self._odometer_reading:
            self._odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    # 4. a method rely on private attribute.
    def drive(self,miles):
        """
        Simulate driving, increasing the odometer reading.
        Reject negative miles.
        :param miles:
        :return:
        """
        if miles>0:
            self._odometer_reading += miles
            print(f"The car has driven {miles} miles.")
        else:
            print("You can't drive negative miles!")

"""step2. interact with class after encapsulation"""
my_secure_car = Car("subaru","outback",2025)
print(my_secure_car.get_descriptive_name())

# normal interact
my_secure_car.read_odometer()
my_secure_car.drive(100)
my_secure_car.read_odometer()

#try unsafe operation
print("--- Attempting unsafe operations ---")
# Try to set a smaller value via Setter setup
my_secure_car.update_odometer(50)
my_secure_car.read_odometer() #The mileage is still 100.
# Caution: That is the function setting the if-else function. Not the capsulation has the function that reject the updating!

# Attempt to change the private attribute. Caution! This is a unrecommended habit although it is possible in Python!
my_secure_car._odometer_reading = -500
my_secure_car.read_odometer()
#!!! we need to obey the agreement, refuse to do that !!!
