'''
Class
      (1) What is class
      (2) ordinary vs static properties
      (3) Special methods
'''
print("==== What is class ====")
#  class - blueprint for object creation!
# Structure > state constructor method


class Person():
    # state
    message = "static state property"
    # constructor

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # method

    def introduce(self):
        print(f"{self.name} says:How do you do?")

    def say_age(self):
        print(f"{self.name} says:i am {self.age} old")

    @classmethod
    def explain(cls):
        print("static method property executed")


person1 = Person("Justin", 32)
person2 = Person("Kyle", 22)

# ordinary state
name = person1.name
print("person1:", name)

# rodinary method
person1.introduce()
person2.say_age()


print("==== ordinary vs static propertiesf ====")

new_message = Person.message
print(new_message)


# static methods

Person.explain()


print("==== Special methods ====")
# Python's most common special methods are below:
# __init__,__newt__,__str__,__call__,__getitem__,__eq__,


class Car():
    # state
    description = "This class makes cars"
    # constructor

    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name,
        self.year = year

    # method
    def start_engine(self):
        print(f"the {self.name} started engine!")

    def stop_engine(self):
        print(f"the {self.name} stopped engine!")

    def __str__(self):
        return f"the car.name:{self.name} was produced in {self.year} year!"

    def __call__(self, *args, **kwds):
        print("Object called as function")
        return True


my_car = Car("ferrari", 2002)
my_car.start_engine()
my_car.stop_engine()
print(my_car.name)
your_car = Car("Toyoto", 2003)
print(your_car)
response = your_car()
print("response:", response)
