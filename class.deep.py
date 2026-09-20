'''
      Class deep diving
      (1) Inheritance
      (2) Polymorphism
      (3) Encapsulation
'''
print("===== Encapsulation =====")


'''
C++,Java=>public private protected
PHP Typescipt>public private protected
Python > name __name(private) _name(protected)
'''


class Account():
    # state
    description = "The class makes bank accounts"

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("$deposit$", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("$withdraw$", amount)
        self.__amount -= amount

    @property  # getter
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("change_ownership", new_owner)
        self.__owner = new_owner

    def change_owner(self, new_owner):
        print("change_ownership", new_owner)
        self.__owner = new_owner


my_account = Account("Kyle", 1000)
my_account.get_balance()
my_account.deposit(2)
my_account.get_balance()
my_account.withdraw(1003)
my_account.get_balance()
my_account.owner = "Alex"
my_account.get_balance()

try:
    result = my_account.__amount
    print(result)
except Exception as err:
    print(err)


owner_name = my_account.holder  # state
print(owner_name)
# getter and setter
my_account.holder = "Nortoy"
my_account.get_balance()
