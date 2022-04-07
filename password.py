username = input("What is your username? ")
password = input("Please create a password: ")
while len(password) < 8:
    password = input("please use a password 8 to 16 characters long: ")
    
def hasNumbers(string):
    return any(char.isdigit() for char in string)

while username in password:
    password = input("please use a password that is not your username ")
    for i in password:
        if hasNumbers(password) == False:
            password = input("password must contain a digit. ")      
        
print("password successfully created.")




















