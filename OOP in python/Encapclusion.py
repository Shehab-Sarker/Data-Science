#  Encapsulation
# 1. Encapsulation is the OOP principle of hiding internal object details and restricting direct
#  access to some parts of an object.
#  2. It helps protect data and makes the class more secure and manageable.
#  Using access modifiers:
#  1. public → accessible from anywhere (default in Python)
#  2. _protected → hint to treat as internal (not enforced)
#  3. __private → name mangled to restrict access from outside
#  Hiding private details inside a class.

class BankAccount:
    def __init__(self):
        self.__balance=100 #Private Variable
        
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            
    def get_balance(self):
        return self.__balance
    
acc=BankAccount()
acc.deposit(6000)
print(acc.get_balance())
# print(acc.__balance)
print()


class Bankaccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
        
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited: ${amount}")
        else:
            print("Invaild amount!")
            
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdaraw : {amount}")
        else:
            print("Insufficient balance.")
            
    def get_balance(self):
        return self.__balance
    
acc1=Bankaccount("Shehab",220000)
print(f"Owner : {acc1.owner}")
print(f"Initial Balance : {acc1.get_balance()}")
acc1.deposit(30000)
acc1.withdraw(50000)
print(f"Tolat Balance : {acc1.get_balance()}")
print()

#Example of a Protected Attribute
class Person:
    def __init__(self,name,age):
        self.name=name
        self._age=age
        
    def show_info(self):
        print(f"Name : {self.name}, age : {self._age}")
        
p=Person("Shehab","23")
p.show_info()

## Accessing the protected attribute (still possible)
print(f"Accessing Protected age: {p._age}")

#  1. _age is a protected attribute.
#  2. We can access it from outside the class, but it's considered bad practice unless you're in a subclass or need to for a good reason.

class Student(Person):
    def is_adult(self):
        return self._age>=18
    
s=Student("Ayan",18)
print(f"Is adulat? {s.is_adult()}")




        
        