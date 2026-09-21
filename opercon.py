
'''
      Operators and COnditions
      (1) Operators
      (2) Conditions
      (3) Logical Operators
'''

print("++++Operators++++")

# +,-,<,<=,>,>=,*,/,//,%,+=,**,-=,==,is

# a = 19
# b = 5

# result = a//b
# left = a % b
# print(f"the result:{result} and left:{left}")


# print(b**3)
print("="*5)

c = dict(name="Kyle", age=23)
d = dict(name="Kyle", age=23)
e = c
# print("c==d", c == d)  # only value
print(id(c), id(d), id(e))


print(c is d)
print(c is e)
