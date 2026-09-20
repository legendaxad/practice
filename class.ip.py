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
