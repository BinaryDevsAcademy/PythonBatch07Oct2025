""" 

    file handling : 
        used to store/ maintain data
        here we are having 3 default modes
            1. Write (w, w+) 
                - create new file if not exist or replace the old text with new one
            2. Append (a, a+)
                - create new file if not exist or adding the new text to the old one
            3. Read mode (r, r+)
                - used to read file content
        
        1. without 'with keyword'
            here we use both open and close function
            syntax : 
                variable = open(path, mode)
                variable.operation()
                variable.close()
        2. with 'with keyword'
"""


# import os

# os.remove('C:\\Users\\Dell\\Downloads\\GitRepos\\PythonBatch1\\CorePython\\Files\\File1.txt')

# file = open('C:\\Users\\Dell\\Downloads\\GitRepos\\PythonBatch1\\CorePython\\Files\\File1.txt', 'a')

# file.write("this is first line")

# file.close()

# with open('C:\\Users\\Dell\\Downloads\\GitRepos\\PythonBatch1\\CorePython\\Files\\File1.txt', 'r') as f:
#     data = f.readlines()
#     print(data)

def createStudentRecord():
    print("Enter student name : ")
    studentName = input()
    print("Enter student phone : ")
    studentPhone = int(input())
    print("Enter student email : ")
    studentEmail = input()
    print("Enter student Class : ")
    studentClass = input()
    
    return {
        'name' : studentName,
        'phone' : studentPhone,
        'email' : studentEmail,
        'class' : studentClass
    }


def saveStudentData(studentInfo):
    with open('C:\\Users\\Dell\\Downloads\\GitRepos\\PythonBatch1\\CorePython\\Files\\File1.txt', 'a') as file:
        file.write(f"{studentInfo['name']} : {studentInfo}")
        print("student record saved")

studentRecord = createStudentRecord()

saveStudentData(studentRecord)

# create a app for contact management 