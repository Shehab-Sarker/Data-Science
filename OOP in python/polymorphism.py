#  Polymorphism
# 1. Polymorphism means "many forms" — in OOP, it refers to the ability to use the same
#  method name in different classes but with different behavior.
#  2. It allows you to call the same method on different objects and get different results
#  depending on the object type

class Cat:
    def speak(self):
        print("Meow")
        
class Dog:
    def speak(self):
        print("Bark")
        
def animal_sound(animal):
    animal.speak()
    
c=Cat()
d=Dog()

animal_sound(c)
animal_sound(d)
print()

#  Special Example of Polymorphism
#  1. Even though all objects use the same method name (pay), they behave differently — this is polymorphism.
#  2. You can easily add more payment types (e.g., CryptoPayment) without changing the function

class Payment:
    def pay(self,amout):
        pass
    
class CashPayment(Payment):
    def pay(self,amount):
        print(f"Paid ${amount} in cash.")
        
class CreditcardPayment(Payment):
    def pay(self,amount):
        print(f"Paid ${amount} using credit card.")
        
class MobliePayment(Payment):
    def pay(self,amount):
        print(f"Paid ${amount} using via mobile wallet.")
        
def process_payment(payment_method,amount):
    payment_method.pay(amount)
    
cash=CashPayment()
card=CreditcardPayment()
moblie=MobliePayment()

process_payment(cash,4000)
process_payment(card,6000)
process_payment(moblie,8000)