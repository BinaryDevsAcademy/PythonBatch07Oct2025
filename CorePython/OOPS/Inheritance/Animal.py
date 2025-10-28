class Animal:
    name = "animal name"
    def __init__(self, name = "animal"):
        print("Animal class constructor")
        self.name = name
    def sleep(self):
        print("animal sleeps")
        
    def eat(self):
        print("animal eats")
        
    def speak(self):
        print("animal speaks",self.name)
        


class Dog(Animal):
    def speak(self):
        print(super().name)
        super().speak() #call parent class speak method
        print("speaks BOW BOW")

dog1 = Dog()

dog1.speak()
dog1.sleep()
dog1.eat()


# class Cat(Animal):
#     def speak(self):
#         print("speaks meow meow")
    
# cat1 = Cat()

# cat1.sleep()
# cat1.eat()
# cat1.speak()

# class WildAnimals:
#     def hunt(self):
#         print("hunting...")
    
#     def nature(self):
#         print("voilent")

# class Fish:
#     def swim(self):
#         print("swimming")
        
#     def sleep(self):
#         print("fish sleeping")

# class Shark(WildAnimals, Fish, Animal):
#     pass

# shark1 = Shark()
# shark1.eat()
# shark1.sleep()
# shark1.hunt()
# shark1.swim()

        