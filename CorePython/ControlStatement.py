"""
    Control Statement :
    Statement : 
        A line
    
    1. Conditional Statements
        a. if
            if condition:
                block of statements
        b. if else
            if condition:
                block of statements
            else:
                block of statements
        c. if elif
            if condition:
                block of statements
            elif condition:
                block of statements
            .
            .
            .
            else:
                block of statements
        d. match
            syntax : 
                match data:
                    case value1:
                        block of case
                    case value2:
                        block of case
                    .
                    .
                    case _:
                        block of case
                        
        e. nested conditional Statements
        
        Advantages : 
        1. Executes set of statments only when the condition is true
        2. provides control over the statements
        
    2. Loops/ Iteration Statements
        to iterate a set of statements finite or infinite number of times
        for : range
            syntax : 
                for variable in range():
                    block of code
        while : infinite
            syntax : 
                init
                while condition:
                    block of while loop
                    update
                
    Assignment : 
    1. write a program to print 4 table upto 20
    2. write a program to print tables from 1 to user choice upto 10
    3. find the even and odd number of the given number
    4. check if given number is prime number or not
    5. find the factorial of a number ex : 5! = 5 x 4 x 3 x 2 x 1 = 120
    6. find the prime number within a range of user choice
    7. write a program to print a table of user choice but only print the even numbers
"""

# variable = 1
# #loop has to run only when the variable value is either less than 10 or equal to 10. if it higher than 10 loop has to stop.
# while variable <= 10:
#     print("statment",variable)
#     variable += 11


# for variable in range(1 , 11):
#     print(f"2 X {variable} = {variable * 2}")

# outer loop
# for variable1 in range(1, 5):
#     # inner loop
#     for variable2 in range(1, 5):
#         print(variable1, variable2)

# value = 1

# match value:
#     case 1:
#         print("case 1")
#     case 2:
#         print("case 2")
#     case _:
#         print("valid value")
    



""" 
    # currency covertor // 1. simple if 2. if elif
    1. USD to INR
    2. Pounds to INR
    3. ....
    option : x
    Enter amount in INR : xxxx
    
    Total Value in ____ is xxxx
    
    # weigth convertor from lbs to kgs and vice versa
    # distance convertor - miles to km and km to miles
"""





# print("Currency Convertor")
# print("1. USD TO INR")
# print("2. EUROS TO INR")
# print("3. DIRHAM TO INR")
# print()
# option = int(input("Please select an option : "))

# currencyValue = 0

# if option == 1:
#     print("Option 1 selected")
#     print("Currency Converstion (USD TO INR)")
#     currencyValue = 80
# elif option == 2:
#     print("Option 2 Selected")
#     print("Currency Converstion (EUROS TO INR)")
#     currencyValue = 85
# elif option == 3:
#     print("option 3 selected")
#     print("Currency Converstion (USD TO INR)")
#     currencyValue = 100
# else:
#     print("please select a valid option")
    

# if currencyValue:
#     inrCurrency = int(input("Enter amount in INR : "))
#     print(f"Total amount {inrCurrency} in USD : {currencyValue * inrCurrency}")
    


#check if a person is a eligible to vote || if his age >= 18
# truthy and falsy : 

# age = input("Enter your age : ")

# age = int(age)

# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# if age >= 18:
#     print("You are eligible to vote")
# if age < 18:
#     print("You are not eligible to vote")

# if "a":
#     print("if block statement")
#     print("if block statement")
#     print("if block statement")
#     print("if block statement")
#     print("if block statement")


# age = input("Enter your age : ")

# print("You are eligible to vote")

# print("You are not eligible to vote")

# value = input("Enter a number : ")
# print("You entered a value of ",value)
# print(5, 65)

# print(f"You entered a value of {value}")
# print("You entered value of "+value)