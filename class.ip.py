'''
      Class deep diving
      (1) Inheritance
      (2) Polymorphism
'''
print("===== Inheritance =====")
#  Parent > Child
# Parent provides only public & protected property to children


class Animal():
    description = "The class is parent for animals"

    def __init__(self, voice):
        self._status = "Animal is alive"
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice:{self.voice}")


class Dog(Animal):
    #     state

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says : {self.sound}-{self.sound}")

    def protect(self):
        print("Yes , I can protect you ")

    def make_voice(self):
        print(f"the {self.name} can make sound:{self.sound}")


class Cat(Animal):
    #     state

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says : {self.sound}-{self.sound}")

    def play(self):
        print("Yes , I can play with you ")


class Fish(Animal):
    #     state

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says : {self.sound}-{self.sound}")

    def swim(self):
        print("Yes , I can swim with you ")


dog = Dog("alex", "wofw", True)
cat = Cat("Tom", "meow", True)
fish = Fish("Nemo", "zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("-----")
dog.make_voice()
cat.make_voice()
fish.make_voice()


print("+++")

print(Animal.description)
print(Dog.description)
print("dog.status:", dog._status)


print("==== Polymorphism =====")

dog.make_voice()
cat.make_voice()
fish.make_voice()


print("-----")


# fish>Fish>Animal>object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)

result = a and b and c
print("The result:", result)


# Fish > Animal > object

data = issubclass(Fish, Animal)
data1 = issubclass(Animal, object)
print("data:", data, data1)
