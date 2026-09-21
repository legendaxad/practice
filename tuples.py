'''
      Tuple
      (1) what is tiple : tuple vs list
      (2) unpacking argiments
      (3) zip
'''

print("===== Whta is tuple : tuple vs list =====")

# Java/php/nodejs array => Python list,array

# list
# numbs = [1, 4, 2, 6, 3, 3]
# car_dic = {"brand": "Ferrari", "year": "2002"}
# print(numbs)
# # Contructor
# letters = list("Hello World!")
# person_dic = dict(name="Kyle", age=22)
# print(letters)

# fruits = ["apple", "lemon", "banana", "melon"]
# print(fruits)
# fruits[0] = "kiwi"
# print(fruits)


# animal = ("dog", "cat", "fish", "lion")
# tuple_obj = ("Mit", 100, True, None)
# print(animal[2])


#  Try avoid this

# people = "Andrew", "John"
# animal = "Dog",

# print(type(animal))

print("===== unpacking argiments =====")

groups = ["MIT", "FLEX", "DEVEX", "MG"]

# (x, y, *z) = groups
# print(f"x:{x},y:{y},z {z}")


#  *args > tuple

def calculate(*args):
    print(f"args:{args}")
    total = 1
    for x in args:
        total *= x
    print(f"the type(args):{type(args)}")
    print(f"Total value :{total}")
    return total


calculate(1, 4, 2)

# **kwargs >dictionary


def introduce(**kwargs):
    print(f"the type(**kwargs) {type(kwargs)}")
    print(f"Hi , I am {kwargs["name"]} and my age is {kwargs["age"]}")

# call


introduce(name="Justin", age=23)
introduce(name="Kyle", age=22, single="True")
