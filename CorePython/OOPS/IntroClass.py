class Student:    
    def __init__(self, 
                 name = "John", 
                 age = 10):
        print("student object created",name)
        self.name = name

student1 = Student("Priya")
student2 = Student()
student3 = Student()
student4 = Student()

# student1.name="Priya"
student1.name = "Henry"

print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
