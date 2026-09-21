
'''
      Operators and COnditions
      (1) Operators
      (2) Conditions
      (3) Logical Operators
'''

# print("++++Operators++++")

# +,-,<,<=,>,>=,*,/,//,%,+=,**,-=,==,is

# a = 19
# b = 5

# result = a//b
# left = a % b
# print(f"the result:{result} and left:{left}")


# print(b**3)
# print("="*5)

c = dict(name="Kyle", age=23)
d = dict(name="Kyle", age=23)
e = c
# print("c==d", c == d)  # only value
# print(id(c), id(d), id(e))


# print(c is d)
# print(c is e)


print("++++Conditions++++")

x = 44
if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")

print("------")
age = 19
# person = None
# if age > 16:
#     person = "Adult"
# else:
#     person = "Child"

# print("person:", person)


# ternary

# person = "Adult " if age > 18 else "minor"
# print("person:", person)


is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:
    print("Welcome here, Do you want to be student?")
elif is_admin:
    print("Welcome here, Do you want to be admin?")
elif is_guest and is_parent:
    print("Welcome here, Do you want to go waiting room?")
else:
    print("Other cases")
