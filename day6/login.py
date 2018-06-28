###########################
users = {
    "root": {
        "password": "vishwa"
    }
}

# #####################
def validate(form):
    if len(form) > 0:
        return False
    return True

# ##################################
def loginauth(username, password):
    if username in users:
        if password == users[username]["password"]:
            print("Login successful")
            return True
    return False
def register():
    while True:
        username = input("New username: ")
        if not len(username) > 0:
            print("Username can't be blank")
            continue
        elif username in users:     
            print("username is alrady present")
            continue
        else:
            break
    while True:
        password = input("New password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        else:
            break
    print("Creating account...")
    users[username] = {}
    users[username]["password"] = password
    print("Account has been created")
##########################
def login():
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("Username can't be blank")
        else:
            break
    while True:
        password = input("Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
        else:
            break

    if loginauth(username, password):
         print("welcome to the py word")
    else:
         print("Invalid username or password")
    ########################################
print("Options: register press 1| login press 2 | exit press 3")
while True:
    option = input("karo input ")
    if option == "2":
        login()
    elif option == "1":
        register()
    elif option == "3":
        break
    else:
        print(option + " is not an option")
