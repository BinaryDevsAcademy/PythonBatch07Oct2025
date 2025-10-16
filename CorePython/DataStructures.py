""" 
    Data Structures : 
        Arrangement of data.
    
        DSA : 
            insertion
            deletion
            selection
            sorting
        10 rounds - 9+ LPA
    
        python - data structures --> built-in 
        
        common - collections
        
        list - allows duplicate values, mutable(it can change) - []
        tuple - allows duplicate values, immutable (it can't be change) - ()
        set - doesn't allow duplicates, mutable - {}
        dict - stores data in key,pair value - {}
"""

#index 0 - 4
list1 = [1,2,3,4,5,-1,0,1]

print(len(list1)) 

#index values 0 - n-1

#insert : used to insert values in a list based on index : insert at the end of the list
list1.insert(4,6)

print(list1)

#append : inser the values at the end of the list
list1.append(7)

#sort : sorts the entire list
list1.sort()

#remove : removes the value from the list
list1.remove(4)

# list1.clear()

print(list1)

#index : gives the index value of the desired value
print(list1.index(5))

print(list1)

""" 
    membership : ('in' and 'not in')
    identity : (is and is not) -- check the memory references
"""

list2 = [1,2,3,4,5,6]

value = 14


for i in range(len(list2)):
    if(list2[i]  == value):
        print("value present inside the list")
        break

if(value in list2):
    print("value is present in the list2")

if(value not in list2):
    print("value is not present inside the list")
    
list3 = [1,2,3,4,5] #104

list4 = [1,2,3,4,5] #105

print(list3, list4)

if(list3 is list4):
    print("Both (3,4) shares same memory location")

if(list2 is list4):
    print('both shares the same memory location')

if(list2 is not list4):
    print("both are not sharing the same memory location")
    
if(list3 == list4):
    print("both lists are having same values")
    
    
stringList = ["cricket", "football", "tennis","Pubg"]

games = ".".join(stringList)

print(stringList)
print(games)

for i in range(len(stringList)):
    print(stringList[i])
    
for i in stringList:
    print(i)

numberList1 = [1,2,3,4,5,6]


# number 2 = 1,4,9,16,25,36

numberList2 = []

for i in numberList1:
    numberList2.append(i ** 2)
    
print(numberList2)

#list comp
numberList3 = [i ** 2 for i in numberList1]

print(numberList3)

#deep copy
numberList4 = [i for i in numberList1]

#unpacking : making the list values as seperate values

#rest of the values -> *variable
value1, value2, value3, *restValues = numberList1

print(value1,value2, value3, restValues)

numberList5 = [*numberList1]

print(numberList5)


tupleData1 = (1,2,3,4,5,-1,0,1)
print(tupleData1)
print(len(tupleData1))
print(tupleData1.count(3))
print(tupleData1.index(1))

for i in tupleData1:
    print(i)
    
numberList6 = [*tupleData1]
print(numberList6)

value1, value2, *restValues = tupleData1

print(value1,value2,restValues)


#variable = dataType(data)

tupleData2 = tuple(numberList2)
print(tupleData2)


setData1 = {1,3,2,4,5,6}
print(setData1.pop())
print(setData1.pop())
# print(setData1.clear())
setData1.add(7)
setData1.remove(5)

#data --> hashing algo --> value?

print(setData1)

value1, value2, *restValues = setData1
print(value1, value2, restValues)

setData2 = {i ** 2 for i in setData1}
print(setData2)

# Subsets are not allowed in sets
# setData3 = {1,22, setData2}

# print(setData3)

tupleData3 = (1,2,tupleData2)

print(tupleData3)

list5 = [1,2,3,list1]

value1, value2,_,[value5, value6, *restValues] = list5
print(list5)

print(value1, value2, value5, value6, restValues)

setData3 = {1,2,3,4,5,6}
setData4 = {4,5,6,7,8,9}

""" 
    common data - 4,5,6
    union - combines two sets and generated 1 set
    intersection - takes only the common data
    difference - consider the values which are not present in another set
    sym_differe - considers the values in both the sets but not the common values
    sym_diff_update
    intersection_update
"""
print(setData3.union(setData4))
print(setData3.intersection(setData4))
print(setData3.difference(setData4))
print(setData3.symmetric_difference(setData4))
print(setData3.symmetric_difference_update(setData4))
print(setData3)
print(setData3.intersection_update(setData4))
print(setData3) # 7,8,9
print(setData3.issuperset(setData4))

setData5 = {8,10,11,12,13}
print(setData5.isdisjoint(setData4))

# setData4.remove(5)
setData4.discard(5)
print(setData4)


""" 
    Dist : key pair values
    
    key -> value - hash
    
    Rules : 
        1. key should be unique -> strings, number
        2. values can be duplicate
"""

student1 = {"name" : "Ravi", 1 : 34}
name = "Rahul"
age = 27

# student2 = dict(name=name)
print(student1)
# print(student2)

student = {
    "name" : "Rahul",
    "age" : age,
    "section" : "A"
}

print(student["name"])
student["name"] = "Gandhi"

print(student)

student["school"] = "Kinder Garden"
print(student)

student["School"] = "Kinder Garden"
print(student)

#setdefault - insert the value or set the default value while inserting into dist
student.setdefault("phone", 8907654321)
print(student)

#popitem - removes the last item from the dist

#pop - removes the item based on the key
student.pop("School")
print(student)

#update - updates dist if the key exist or else insert into the dist
student.update({"email" : "rahul@gmail.com"})

print(student)

#keys - return the list of keys in a dist
print(student.keys())

#values - return the list of values in a dist
print(student.values())

#items - return the list of keys and values in a dist
print(student.items())

for i in student:
    print(student[i])
    
for i,j in student.items():
    print(i,j)

student.clear()
print(student)

