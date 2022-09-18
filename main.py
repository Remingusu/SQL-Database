from Data.database_handler import DatabaseHandler

database_handler = DatabaseHandler("database.db")


def register():
    print("---Register---")
    username = input("Username : ")
    password = input("Password : ")
    age = int(input("Age : "))
    database_handler.create_person(username, password, age)
    menu_connected(username)


def login():
    print("---Login---")
    username = input("Username : ")
    password = input("Password : ")
    if database_handler.user_exists_with(username) and password == database_handler.password_for(username):
        print("Login !")
        menu_connected(username)
    else:
        print("Username / password mismatch")


def user_list():
    username = database_handler.user_list()
    for i in username:
        print(i["Username"])


def change_password(username: str):
    new_password = input("Enter your new password : ")
    new_password_confirmation = input("Confirm your new password : ")
    if new_password == new_password_confirmation:
        database_handler.change_password(username, new_password)
        print("Your password has been changed !")
    else:
        print("Password mismatch !")


def description(username: str):
    description = database_handler.description(username)
    description = description["Description"]
    if description is None or description == "":
        print("You don't have a description")
    else:
        print(f"Your description is : {description}")


def change_description(username: str):
    description = database_handler.description(username)
    description = description["Description"]
    if description is None or description == "":
        print("You don't have a description")
    else:
        print(f"Your description is : {description}")
    new_description = input("Enter your description : ")
    database_handler.change_description(username, new_description)
    print("Your description has been changed !")


def menu_connected(username: str):
    while True:
        print("Welcome to IDK ! (connected)")
        print("Choose an option")
        print("1. Logout")
        print("2. Change Password")
        print("3. User list")
        print("4. See your description")
        print("5. Change your description")
        choix = int(input())
        if choix == 1:
            return
        if choix == 2:
            change_password(username)
        if choix == 3:
            user_list()
        if choix == 4:
            description(username)
        if choix == 5:
            change_description(username)


def menu_not_connected():
    while True:
        print("Welcome to IDK (not connected)")
        print("Choose an option")
        print("1. Login")
        print("2. Register")
        print("3. User list")
        choix = int(input())
        if choix == 1:
            login()
        if choix == 2:
            register()
        if choix == 3:
            user_list()


menu_not_connected()
