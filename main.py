import sqlite3
import os
import sys
import colorama
from colorama import Fore
from colorama import init
import time
import keyboard
from datetime import datetime

# Connecting to sqlite
# connection object


option = None
currentMoney = None
#print(sys.stdin)


connection_obj = sqlite3.connect('db/database.db')


cursor_obj = connection_obj.cursor()



# Creating table
#table = """ CREATE TABLE account (Email,First_Name,Last_Name); """

cursor_obj.execute("""CREATE TABLE IF NOT EXISTS account (Email,First_Name,Last_Name);""")
cursor_obj.execute("""CREATE TABLE IF NOT EXISTS transactions (
reason VARCHAR(255) NOT NULL,
amount INT NOT NULL,
timestamp CHAR(25)
) """)




#cursor_obj.execute(table)
checkEmpty = None
print("Account table created")

def show_account():
    global checkAccount
    cursor_obj.execute("SELECT * FROM account")
    checkAccount = cursor_obj.fetchall()
    print(cursor_obj.fetchall())
def show_transactions():
    global currentMoney, checkEmpty
    print("Transaction List:")
    for row in cursor_obj.execute('SELECT * FROM transactions'):
        print(row)
    cursor_obj.execute("SELECT * FROM transactions")
    checkEmpty = cursor_obj.fetchall()
    if not checkEmpty:
        currentMoney = 0
    else:
        getMoney()
    return(currentMoney)
show_account()
#show_transactions()
def getMoney():
    global currentMoney
    currentMoney = 0
    for i in range(len(checkEmpty)):
        currentMoney += float(checkEmpty[i][1])
    return(currentMoney)

Balance = Fore.BLUE + "Balance"
Transactions = Fore.WHITE+"Transactions"
Settings = Fore.WHITE+"Settings"
Help = Fore.WHITE+"Help"
Exit = Fore.WHITE+"Exit"



if len(checkAccount) == 0:
        print("Welcome to SmartCashManage")
        print("You do not have an account yet...")
        fName = input("Please enter your first name: ")
        lName = input("Please enter your last name: ")
        email = input("Please enter your email address: ")      
        insertList = [email, fName, lName]
        cursor_obj.executemany("INSERT INTO account (Email,First_Name,Last_Name) values(?,?,?)", (insertList,))
        connection_obj.commit()
else:
        cursor_obj.execute("SELECT First_Name FROM account")
        name = cursor_obj.fetchall()
        print("""
    Welcome back to ManageCash, """ + name[0][0] + """!
    """)
        #sys.stdin = open("txt.txt","w")
        option = "b"
#cursor_obj.executemany("INSERT INTO account (Email,First_Name,Last_Name) values(?,?,?)", (['tax', '-1', '05-07-2009'],))
#connection_obj.commit()

def options():
    global Balance, Transactions, Settings, Help, Exit
    print("""
    """+Balance+"""
    """+Transactions+"""
    """+Settings+"""
    """+Help+"""
    """+Exit+"""
    """)
options()
init()
def down():
    global Balance, Transactions, Settings, Help, Exit, option
    if Balance == Fore.BLUE + "Balance":
        Balance = Fore.WHITE + "Balance"
        Transactions = Fore.BLUE + "Transactions"
        options()
        time.sleep(0.1)
        option = "t"
    elif Transactions == Fore.BLUE + "Transactions":
        Transactions = Fore.WHITE + "Transactions"
        Settings = Fore.BLUE + "Settings"
        options()
        time.sleep(0.1)
        option = "s"
    elif Settings == Fore.BLUE + "Settings":
        Settings = Fore.WHITE + "Settings"
        Help = Fore.BLUE + "Help"
        options()
        time.sleep(0.1)
        option = "h"
    elif Help == Fore.BLUE + "Help":
        Help = Fore.WHITE + "Help"
        Exit = Fore.BLUE + "Exit"
        options()
        time.sleep(0.1)
        option = "e"
    elif Exit == Fore.BLUE + "Exit":
        options()
    else:
        pass
    
        
def up():
    global Balance, Transactions, Settings, Help, Exit, option
    if Exit == Fore.BLUE + "Exit":
        Exit = Fore.WHITE + "Exit"
        Help = Fore.BLUE + "Help"
        options()
        time.sleep(0.1)
        option = "help"
    elif Help == Fore.BLUE + "Help":
        Help = Fore.WHITE + "Help"
        Settings = Fore.BLUE + "Settings"
        options()
        time.sleep(0.1)
        option = "s"
    elif Settings == Fore.BLUE + "Settings":
        Settings = Fore.WHITE + "Settings"
        Transactions = Fore.BLUE + "Transactions"
        options()
        time.sleep(0.1)
        option = "t"
    elif Transactions == Fore.BLUE + "Transactions":
        Transactions = Fore.WHITE + "Transactions"
        Balance = Fore.BLUE + "Balance"
        options()
        time.sleep(0.1)
        option = "b"
    elif Balance == Fore.BLUE + "Balance":
        options()
    else:
        pass
def addTransaction():
        #sys.stdin = <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>
        sacrificialLamb = input("Press Enter To Continue: ")
        secondSacrifice = input("")
        reason = input("Reason for transaction (E.g. Tax): ")
        amount = float(input("Amount of money: "))
        timestamp = datetime.now().strftime("%H:%M:%S")+" at " +datetime.now().strftime("%m/%d/%Y")
        transactionInsert = [reason, amount, timestamp]
        cursor_obj.executemany("INSERT INTO transactions (reason, amount, timestamp) values(?,?,?)", (transactionInsert,))
        connection_obj.commit()
        print("Transaction was successful!")
        print("Going home...")
        time.sleep(1)
        os.system('clear')
        
        
if len(checkAccount) != 0:
    option = "b"
while True:
    if len(checkAccount) != 0:
        if keyboard.is_pressed("down") == True:
            time.sleep(0.01)
            os.system('clear')
            down()
        if keyboard.is_pressed("up") == True:
            time.sleep(0.01)
            os.system('clear')
            up()
        if keyboard.is_pressed("shift") == True:
            if option == "b":
                print(f'You currently have ${show_transactions()}')

                time.sleep(0.1)
            if option == "s":
                print("No settings currently available")
                time.sleep(1)
                option == None
            if option == "h":
                print("""
Help:
Use arrow keys to change options
Press shift to select option
Contact trankyan171@gmail.com if you have any more queries
Manage Cash is basically an app to help with managing and
tracking the money that you have.""")
                time.sleep(0.1)
            if option == "t":
                time.sleep(0.01)
                os.system('clear')
                options()
                for row in cursor_obj.execute('SELECT * FROM transactions'):
                        print(row)
                addTransaction()
                #print(checkEmpty)
                options()
            if option == "e":
                os.system('clear')
                print("""
Thankyou for using PyBank!
                
                """)
                time.sleep(1)
                time.sleep(0.2)
                os.system('clear')
                print("""
Thankyou for using PyBank!
Exiting .   
                """)
                time.sleep(0.2)
                os.system('clear')
                print("""
Thankyou for using PyBank!
Exiting ..  
                """)
                time.sleep(0.2)
                os.system('clear')
                print("""
Thankyou for using PyBank!
Exiting ...
                """)
                time.sleep(1)
                exit()
    else:
        break
"""
cursor_obj.executemany("INSERT INTO account (Email,First_Name,Last_Name) values(?,?,?)", (['tax', '-1', '05-07-2009'],))
connection_obj.commit()
"""




connection_obj.close()


#sudo python3 -B main.py
