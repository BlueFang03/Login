
New_user = input("Please Create a Username: ")
New_Password = input("Please Create a Password: ")

def Signin():
    attempts = 0
    while attempts < 3:
        check_user = input("Enter your username: ")
        check_pass = input("Enter your Password: ")
        if check_user == New_user and check_pass == New_Password:
            print("Successful")
            return x
        elif check_user != New_user:
            attempts+=1
            print("Wrong Username")
        elif check_pass != New_Password:
            attempts += 1
            print("Wrong Password")
        elif check_user != New_user & check_pass != New_Password:
            attempts+=1
            print("Wrong Username and Password")


def password_strength(ps):
    ps_strenght = False
    while ps_strenght:
        if filter(lambda i: i != i.isnumeric(), ps):
            print("Password is not strong enough")
            New_Password
        elif len(ps) < 5:
            print("Password is not strong enough")
            New_Password
        return New_Password
        ps_strenght = True


password_strength(New_Password)
Signin()



