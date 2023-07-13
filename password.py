import random
import string
user = input("Do you want to create a new password? ")

if user.lower() == "y" or user.lower() == "yes":

    character = list(string.punctuation + string.digits + string.ascii_letters)
    
    a = random.sample(character, 10)
    
    password = "".join(a)
    
    print(f"Your new password is {password}")

    save = input("Do you want to save your password? ")
    if save.lower() == "y" or save.lower() == "yes":
        with open('notes.txt', 'w') as file:
            file.write(password)
            print("Password has been saved to notes,txt file")
    else:
        quit
else:
    quit

