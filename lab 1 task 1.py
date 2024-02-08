def welcome_guest(name):
    # Check if the first letter of the name is a vowel
    if name and name[0].lower() in 'aeiou':
        return "Welcome!"
    else:
        return "Khushamdeed!"


guest_name = input("Enter guest's name: ")
greeting = welcome_guest(guest_name)
print(greeting)
