""" 
Function : 
    Reusable block of code

ex : 
    > 10 lines of code -> name
    
    after 20 lines
    
    call name

1. built-in functions - len(), type(), int(), str()
2. user-defined functions - user will create the function
3. lambda function - 1 line function

creating a function : 
    keyword - def
    Syntax : 
        def functionName():
            block of re-usable code

Using a function : 
    by calling the functionName we can use a function
    
Arguments in function : 
    if we are passing any data when calling a function is called as arguments
    
    syntax : 
        functionName(data)
        
Parameters in function : 
    used to accept/ store the arguments inside it 
    syntax : 
        def functionName(para,...):
        
default parameters :

name arguments : 

return values in function:
    to return value in a function we have to use "return" keyword inside it
    
    Syntax : 
        def functioName():
            ops
            return value

returning multiple values inside a function:
    syntax : 
        return value1, value2,...

*args, **kwargs
"""

def cal(operation, **numbers):
    result = 0
    print(numbers)
    if(operation == "add"):
        for i in numbers['numbers']:
            result += i

    return result

print(cal(operation = 'add',numbers = [1,2,3,4,5,6,7]))
# def sample(a,**b):
#     print(a, b)

# sample(a="2", b="5", c= 7)
# sample(2, 5, 7)

# def sample(a,b,*c):
#     print(a,b,c)
    
# sample(1,2,3,4,5,6)

# def sample():
#     return 1,2,3,4

# value1, value2, value3, *rest = sample()

# print(value1, rest)

# def addNumbers(n1 = 0, n2 = 0):
#     return n1+n2
    
# print(addNumbers(1) * 2)

# def printUser(first = "Guest",middle ="", last ="Guest"):
#     print(first, middle, last)
    

# printUser(last="Sharma",first="ravi")


# def printUser(first = "Guest",middle ="", last ="Guest"):
#     print(first, middle, last)
    

# # printUser("ravi","", "Sharma")
# printUser()

# def isPrimeNumber(number):
#     count = 0 #counts the zero

#     for i in range(1,number + 1):
#         if number%i == 0:
#             count += 1

#     if count == 2:
#         print(number,"is prime number")
#     else:
#         print(number,"is not a prime number")


# isPrimeNumber(3)
# isPrimeNumber(14)
# isPrimeNumber(6)
# isPrimeNumber(7)
# print("before function")

# def sample():
#     print("sample function")
    
# print("after function")

# sample()
