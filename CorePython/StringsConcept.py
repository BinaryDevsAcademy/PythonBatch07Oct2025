""" 
    String : collection of characters(numbers, alphabets, spcl character)
    
    indivi: single family     name - vaikuntapuram - 
    apart : multiple families name - vaikuntapuram - index number (0, size - 1)
    
    
"""

value = 1

name = "Tony Stark" #index values(0 - 9)

#indexing

#accessing single character in string -- syntax : variableName[index]
print(name[0])
print(name[1])

#accessing multiple characters in a string -- syntax : variableName[starting : ending (n-1)]
print(name[0 : 6])

#reverse indexing - negative indexing -- right to left -- syntax : variableName[-starting] //1
print(name[-1])

#accessing multiple characters in reverse indexing -- syntax : variableName[starting : ending]
print(name[-5 : ])

#reversing a string variableName[start(empty) : ending(empty) : step(-1)] // slicing
print(name[ :: -1 ])


# string methods

#format : used to replace placeholder values 
#syntax : string.format("values")
print("name : {}".format("dinesh"))

#join : onhold until we complete list


#replace - used to replace a certain word inside a string
#syntax : string.replace(oldString, newString, count(optional))
#count - mentions how many words that it needs to replace (default it replaces all the words)
sentance = "hello boy. how are you My boy?"
print(sentance.replace("boy", "man",1))

#capitalize : converst the 1st character of a string to uppercase
print(sentance.capitalize())

#lower : converts all the characters into lower case
print(sentance.lower())

#upper : converts all the characeters into uppercase
print(sentance.upper())

#title : converst the first character of the each word in a string to uppercase
print(sentance.title())

#find : used to find a character in a string if the character exists --> returns the index : -1
#syntax :       find('character', startingIndex, endingIndex)
print(sentance.find("o", 6))

#index : used to find a character in a string if the character exists --> returns the index : error
print(sentance.index('boy'))

#rfind : to find the character in a string from backwards --> return the index : error
print(sentance.rfind("z"))

numberedString = '123' 



#zfill: is used to pad 0's to a string -- > date = 08 - 2 digits - 1
print(numberedString.zfill(7))

#isdigit : checks if the string is having numeric values or not
print(numberedString.isdigit())

str1 = "abc123"

print(str1.isalnum())

print(str1.isalpha())

print(str1.isdecimal())

print(str1.isidentifier())

print(str1.islower())

print(str1.isupper())

print(sentance.count("o"))
