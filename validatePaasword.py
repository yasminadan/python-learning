password = "TECHNOguru"
input_password = input("Enter password: ")

while True:
 if input_password != password:
     print("try again")
 else:
    print("login successful")
 break

def validation():

loop = True
while loop:
     password = input("Enter your password: ")
 
     if len(password) < 8:
         print("your password should have more than 8 characters")
     elif not password.isdigit():
        print("your password should have atleast one digit")
     elif not password.isupper():
        print("your password should have a atleast a capital letter")
     else:
        print("login successful")
     break 
   return validation   