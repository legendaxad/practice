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
