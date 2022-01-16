contactList = []


def printContact(contacts):
    for contact in contacts:
        print("Name: {} \nContact No: {}".format(contact[0], contact[1]))


def createContact():
    name = input("Enter Name:   ")
    mobNo = input("Enter Contact Number:   ")
    contactList.append((name, mobNo))


def displayContact(view_input):
    if view_input == 'a':
        contactList.sort()
        printContact(contactList)
    else:
        result = []
        for contact in contactList:
            if contact[0].find(view_input) == -1:
                print("No such Contact Details exist with given name, please enter a valid name \n")
            else:
                result.append(contact)
        printContact(result)


def updateContact():
    update_input = input("Enter 'en' to Edit contact name, Enter 'ec' to edit contact number \n"
                         "Enter 'ed' to Delete contact:  ")
    query = input("Enter Contact Name to update/delete: ")
    found = False
    for index,contact in enumerate(contactList):
        if contact[0] == query:
            found = True
            if update_input == 'en':
                contactList.append((input("Enter updated Name: "), contact[1]))
                contactList.pop(index)
            elif update_input == 'ec':
                contactList.append((contact[0], input("Enter updated Contact Number: ")))
                contactList.pop(index)
            elif update_input == 'ed':
                contactList.pop(index)
            else:
                print("Enter a valid choice")
    if not found:
        print("No Contact Details exists with given name, Enter a valid name to update/delete")


def menu():
    user_input = input("Enter 's' to save contact, 'v' to view contact, 'u' to update contact, \n"
                       "Enter 'q' to quit:   ")

    while user_input != 'q':
        if user_input == 's':
            createContact()
        elif user_input == 'v':
            view_input = input("Enter 'name' to search, \n"
                               "or enter 'a' to view all saved contact:  ")
            displayContact(view_input)
        elif user_input == 'u':
            updateContact()

        else:
            print("Enter a valid choice")

        user_input = input("\nEnter 's' to save contact, 'v' to view contact, 'u' to update contact, \n"
                           "Enter 'q' to quit:   ")


menu()

