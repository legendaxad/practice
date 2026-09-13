'''
      Functions
      (1) DEFINE vs CALL
      (2) Parameter vs Argument
      (3) Keyword vs default arguments
      (4) Scope
'''

print("=====DEFINE(parameter) & CALL(argumeter) =====")
# funtion> reusable blovk of code
# Instead of block {} in Java but in Python uses indentation!

# Define - parameter


def greet(a):
    print(f"how do you do? {a}")


def greeting(b):
    print(f"greeting is executed")
    return f"Hi {b}"


# CALL - argument
result1 = greet("Kyle")
result2 = greeting("Abbos")
print(result1)
print(result2)
