import mysql.connector
import random

connection = mysql.connector.connect(user = "root", database = "elite_102", password = "Aqua321!!")

cursor = connection.cursor()


def account_password_verification():
    attempts = 3 
    user_input_num = input("Enter your account number: ")
    user_input_pin = input("Enter your account pin: ")

    while (attempts > 0):
        get_account_pin = (f"SELECT pin FROM bank_accounts WHERE account_num = {user_input_num}")

        cursor.execute(get_account_pin)
        account_pin = cursor.fetchone()[0]

        print(f"account_pin is {account_pin}")

        while (account_pin != user_input_pin):
            print("Your account information doesn't match up. ")
            print(f"You have {attempts} attempts left")
            account_num = input("Enter your account number: ")
            user_input_pin = input("Enter your account pin: ")
            attempts -= 1 

            if(attempts < 0):
                print("You have reached the max number of attempts. Account cannot be accessed")
                return ""
        return user_input_num

# fine tune to say something when they input something other than int, do for other functions too
# Checking account balance: Functionality to allow users to view the current balance of their account.
def check_balance(user_account_num):
    current_balance = (f"SELECT balance FROM bank_accounts WHERE account_num = {user_account_num}")
    cursor.execute(current_balance)
    cur_balance = int(cursor.fetchone()[0])
    print (f"Balance: {cur_balance}")

    
# Depositing funds: Enabling users to add money to their account.
def deposit_funds(user_account_num):
    add = int(input("Amount of money to be deposited: "))
    original_balance = (f"SELECT balance FROM bank_accounts WHERE account_num = {user_account_num}")
    cursor.execute(original_balance)
    og_balance = int(cursor.fetchone()[0])

    deposit_fund = (f"UPDATE bank_accounts SET balance = {og_balance + add} WHERE account_num = {user_account_num}");  
    cursor.execute(deposit_fund)

    # prints out new balance 
    new_balance = (f"SELECT balance FROM bank_accounts WHERE account_num = {user_account_num}")
    cursor.execute(new_balance)
    new = int(cursor.fetchone()[0])
    print(f"Current balance: {new}")



# Withdrawing funds: Allowing users to remove money from their account.
def withdraw_funds(user_account_num):
    subtract = int(input("Amount of money to be withdrawn: "))
    original_balance = (f"SELECT balance FROM bank_accounts WHERE account_num = {user_account_num}")
    cursor.execute(original_balance)
    og_balance = int(cursor.fetchone()[0])
# will adding the values work
    withdraw_fund = (f"UPDATE bank_accounts SET balance =  {og_balance - subtract} WHERE account_num = {user_account_num}")
    cursor.execute(withdraw_fund)

    new_balance = (f"SELECT balance FROM bank_accounts WHERE account_num = {user_account_num}")
    cursor.execute(new_balance)
    new = int(cursor.fetchone()[0])
    print(f"Current balance: {new}")



# Creating a new account: The a1bility for new users to register an account within the app.
def create_account():
    name = input("Enter your name: ")
    account_num = random.randint(1000,9000)
    pin = input("Create a pin: ")
    confirmation_pin = input("Confirm the pin: ")

    while not(confirmation_pin == pin):
        print("Your confirmation pin does not match up with your original pin. Try again")
        confirmation_pin = input("Confirm the pin: ")
    
    inputting_new_account = (f"INSERT INTO bank_accounts (account_num, pin, name, balance) VALUES ({account_num}, {pin}, {name}, 0)")
    # cursor.execute(inputting_new_account) 
    account_verified = account_num
    return (f"Account number {account_num} has been created. ")

# Deleting an account: Functionality for users to remove their account, should they choose to.
def close_account(user_account_num):
    # is not None to check if account_password_verification returned an actual acocunt number

    if(user_account_num != ""): 
        deleting_account = (f"DELETE FROM bank_accounts WHERE account_num = {user_account_num}")
        cursor.execute(deleting_account)
        print(f"Successfully deleted account number {user_account_num}")
        return 
    return ("Account cannot be deleted.")

# Modifying account details: Allowing users to change their account information, such as email, password, or personal details.
def modify_account(user_account_num): 
    if(user_account_num != ""):
        new_pin = input("Enter your new pin: ")
        confirm_new_pin = input("Confirm your new pin: ")
        while not(confirm_new_pin == new_pin):
            print("Your confirmation pin does not match up with your original pin. Try again")
            confirm_new_pin = input("Confirm the pin: ")
        modifying_account = (f"UPDATE bank_accounts SET pin = {new_pin} WHERE account_num = {user_account_num}")
        cursor.execute(modifying_account)
        print(f"The pin for account number {user_account_num} has successfully been changed. ")
    else: 
        print ("Account cannot be modified. ")
    
def home_page(user_account_num): 
    print("1. Check balance \n2. Deposit money \n3. Withdraw money \n4. Modify account \n5. Close account \n6. Create account")
    user_choice = int(input("Select an action"))

    while(user_choice < 1 and user_choice > 6):
        print("Enter a valid choice")
        print("1. Check balance \n2. Deposit money \n3. Withdraw money \n4. Modify account \n5. Close account \n6. Create account")
        user_choice = int(input("Select an action: "))

    if(user_choice == 1):
        check_balance(user_account_num)
    elif(user_choice == 2):
        deposit_funds(user_account_num)
    elif(user_choice == 3):
        withdraw_funds(user_account_num)
    elif(user_choice == 4):
        modify_account(user_account_num)
    elif(user_choice == 5):
        close_account(user_account_num)
    elif(user_choice == 6):
        create_account()
    return_to_home()


def return_to_home():
    returning = input("Return to home page? Yes or No")
    if(returning.lower() == ("yes")):
        home_page(account_verified)

#running the program 
print("Welcome to the banking app! ")
account_verified = account_password_verification()
print(f"account_verified is {account_verified}")


if (account_verified != ""):
    home_page(account_verified)


cursor.close()

connection.close()


        
# SELECT * FROM table_name WHERE condition
# SELECT pin FROM bank_accounts WHERE account_num = desired account



#if (returning_member.equalsIgnoreCase("yes")):
#    account_number = input("Enter your account number: ")
#    account_pin = input("Enter your account PIN: ")
    # make sure the pins and the account numbers match up to what is in the dictionary 
#elif (returning_member.equalsIgnoreCase("no")):
    # account_number = random number 
#    account_pin = input("Create your account PIN")
#    pin_confirmation = input("Confirm your account PIN")
#    while(!account_pin.equals(pin_confirmation)):
#          print("Your PIN codes do not match up. Enter it again.")
#          pin_confirmation = input("Confirm your account PIN")
#    add (account_number, account_pin) to table