'''
      Objects :
      (1) What is object?
      (2) Iterable objects & Range
      (3) Dictionary
      (4) Error handling system
'''
import array
import math
# print("==== What is object ====")
# An object has state and method properties
# Everything is object in Python

# print(type("Hello world"))
# print(type(99))
# print(type(True))
# print(type(array))
# print(type(math))

# Paradigm>Functional Programming & OOP
# OOP 4 Concepts => Abstraction,Encapsulation,Inheritance,Polimorphism
# result1 = math.ceil(97.2)
# print(result1)
# result2 = math.ceil(98.2)
# print(result2)


print("==== Error handling system ====")


car_dic = dict(name="Tayota", year=2026, electric=True)


try:
    print("passed here")
    a = car_dic.speed()
    result = car_dic["aa"]
    print("result", result)


except Exception as err:
    print("error:", err)

else:
    print("executed without errors")
finally:
    print("Final closing logec")
