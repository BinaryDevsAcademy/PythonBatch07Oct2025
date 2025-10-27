import ast

def checkIfPhoneNumberExist(number, contactList):
    for contact in contactList:
        contact_dict = ast.literal_eval(contact)
        if contact_dict['number'] == number:
            return True
    
    return False
    
def addContactToFile(contact):
    file = file = open('C:\\Users\\Dell\\Downloads\\GitRepos\\PythonBatch1\\Projects\\file\\Contacts.txt', 'a+')
    
    contactList = getAllContacts()
    contact["id"] = len(contactList) + 1
    if len(contactList) == 0:
        # print(contact)
        file.write(f"{contact}")
    else:
        # print(contact)
        if checkIfPhoneNumberExist(contact["number"], contactList):
            print("Phone number already existed")
        else:
            file.write(f"{contact}")
            file.write("\n")
    print("contact saved successfully")
    file.close()
    

def getAllContacts():
    file = open('C:\\Users\\Dell\\Downloads\\GitRepos\\PythonBatch1\\Projects\\file\\Contacts.txt', 'r')
    contacts = file.readlines()
    file.close()
    return contacts