import FileHandling as fh

# fh.checkIfPhoneNumberExist(1234567890,fh.getAllContacts())

print(fh.getAllContacts())


print("Enter contact number")
number = int(input())

print("Enter name for the contact number : ")
contactName = input()

fh.addContactToFile({
    "name" : contactName,
    "number" : number
})

print(fh.getAllContacts())