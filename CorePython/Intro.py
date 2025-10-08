""" 
    What is python
    History of Python
    Software Requirements of python
    Indentation
    Data Types
    Print()
    type()
    String - intro
    comments
"""

# print('That\'s a point...')
# print("That's a point...")
# print('"How are you?", she asked him')
# print('''print('That\'s a point...')
#       print("That's a point...")
#       print('"How are you?", she asked him') ''')
# print(True)

# type() is used to check the type of the value
# print(type(1))
# print(type(1.4))
# print(type("1"))
# print(type(True))

""" 
    data temp - variable - container that holds the data - stores inside RAM
    Rules : 
        1. to identify variables we use names
        2. names can't be keywords -> if want to use always make any one of the character to uppercase
        3. Can't use special characters except _
        4. can't start variable name with numbers 
            ex : 2a X  -----   a2
        
    Best practice : 
        1. give meaningful names --> studentName or studentPhoneNumber
        
        2. Always follow case notations ---> digitalbrollystudentname
        snake case notation : digital_brolly_student_name
        camel case notation : digitalBrollyStudentName
        Pascal Case notation ; DigitalBrollyStudentName
        
    python dynmically typed lang ---> assigns data type automatically based on the data stored in variable
    
    operation : process --> tools (operators)
    
    operators : 
        1. assignment (=)
        used to assign value -> variable
        --> it always assigns the righside value to the left side
        shorthand : (+=, -=, *=, /=, %=, //=, **=)
            combines the arth ops and assign
        --------------------------
        2. arth (+, - , /, *, %, //, **)
        used to perform maths ops
        --> It always follow BODMAS Rules
        -------------------------
        3. logical (and, or, not)
            used to combine multiple boolean values into a single value
            
            and : 
            input1 input2   output
            true    true    true
            true    false   false
            false   true    false
            false   false   false
            
            or : 
            input1 input2   output
            true    true    true
            true    false   true
            false   true    true
            false   false   false
            
            not :
            input   output
            true    false
            false   input
            
            conditions combine
        --------------------------------
        4. bitwise (&, |, ~, ^, >>, <<)
            used to perform bit by bit operations
            bit - one of the binary number (0,1)
            
            number system : 
                1. binary - 0, 1
                2. octal - 0 - 7
                3. decimal - 0- 9
                4, hexa decimal -- 0-9 A - F
                
            we apply it on decimals but at the backgrounds the sytem performs the operation on the binary numbers
            
            2 ) 25 (12
                24
                --
                1
                
            2 ) 12 (6
                12
                --
                0
            
            2) 6 ( 3
                6
             -----
              0
            
            2) 3 (1
                2
             --- 
              1
            
            2) 1 (0
                0
             ---- 
              1
            
            25 - 11001
            
            
            5 & 8
            
            0   1   0   1
            1   0   0   0
            ---------------
            0   0   0   0
            
            5 | 8
            
            0   1   0   1
            1   0   0   0
            -------------
            1   1   0   1
        ---------------------------------
        5. comparison/ relational (>, <, >=, <=, ==, !=)
            used to compare data and will provide the boolean as a result
        ----------------------------------
        6. increment/ decrement
        7. membership
        8. identity operator
"""

print(5 & 8)
print(5 | 8)

# studentName1 = "ravi"
# studentName2 = "ravi"

# studentClass1 = "A"
# StudentClass2 = "A"

# print(studentName1 == studentName2 and studentClass1 == StudentClass2)

# #person1 is not person2
# print(not(studentName1 == studentName2 and studentClass1 == StudentClass2))


# print(5 != 5)
# print(5 > 8)
# print(5 < 8)
# print(5 >= 8)
# print(5 <= 8)
# print(5 == 5)

# value1 = 5
# value2 = 6

# print(value1)

# value1 += value2 # value1 = value1 + value2

# print(value1)


# result = 12

# print(result)
# print(12 + 4) 
# print(6 * 6)

# print(12 + 5)
# print(12 - 5)
# print(12 * 5)
# print(12 / 5)
# print(12 % 5)
# print(12 // 5)
# print(12 ** 5)

# print(5 * 4 + 4 / 6) #34, 31, 

# """ 
#     20 + 0.666
# """
