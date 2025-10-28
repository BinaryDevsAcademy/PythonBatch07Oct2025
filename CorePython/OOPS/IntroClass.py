class Student:    
    def __init__(self, 
                 name = "John", 
                 age = 10):
        print("student object created",name)
        self.name = name
        self.age = age
    
    # def showDetails(self):
    #     return f"name = {self.name} and age = {self.age}"
    
    def showDetails(self,age = 10):
        return f"name = {self.name} and age = {age}"

student1 = Student("Priya")
student2 = Student("Raj")
student3 = Student("Raghu")
student4 = Student("Iris")

# student1.name="Priya"
student1.name = "Henry"


message1 = student1.showDetails()
message2 = student2.showDetails()
message3 = student3.showDetails()
message4 = student4.showDetails()

print(message1)
print(message2)
print(message3)
print(message4)