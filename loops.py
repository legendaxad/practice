'''
      LOOP operators
      (1) For
      (2) Break / else
      (3) While
'''


print("====== for Operators ======")

# text = "MIT"

# numbs = [10, 7, 3, 4]
# car_obj = dict(brand="Ferrari", year=2025)
# range_obj = range(5)

# for letter in text:
#     print(letter)
# print("====")
# for number in numbs:
#     print(number)
# print("====")
# for x in range_obj:
#     print(x)

# for key in car_obj:
#     print(car_obj.get(key))
# print("======")

# for x in range(1, 20, 5):
#     print(f"the x: {x}")


print("====== Break / else ======")

# for x in range(1, 20, 5):
#     print(f"the x: {x}")
#     if x > 11:
#         print("reached break")
#         break
# else:
#     print("looped success")


print("====== While Operator ======")

# numb = 40
# while numb > 0:
#     numb -= 10
#     print(f"The number equal : {numb}")


count = 0
while True:
    count += 1
    x = int(input("Find the number: "))

    if x == 41:
        print(f"you fund the number in {count} steps")
        break
    else:
        print("Whrong")
