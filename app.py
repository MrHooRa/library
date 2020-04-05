# DATABASE connector
import mysql.connector
import os

# To color shell text
import colorama
colorama.init()

config = {
    'app':{
        'NAME':"Python library",
        'VERSION':'0.1'
    },
    'DATABASE':{
        'hostname':'localhost',
        'username':'root',
        'password':'',
        'dbName':'python-library'
    },
    # Regular color!
    'color':{
        'rest': '\033[0m',
        'red': '\033[0;31m',
        'green': '\033[0;32m',
        'black': '\033[0;30m',
        'blue': '\033[0;34m',
        'cyan': '\033[0;36m',
        'purple': '\033[0;35m',
        'yellow': '\033[0;33m'
    },
    'tempUser':{
        'username':'admin',
        'password':'123',
        'userID': '1'
    }
}

# Do NOT EDIT THIS SECTION !!
mydb = mysql.connector.connect(
  host=config['DATABASE']['hostname'],
  user=config['DATABASE']['username'],
  passwd=config['DATABASE']['password'],
  database=config['DATABASE']['dbName']
)
# # # # # # # # # # # # # # # #

# AND THIS ONE!
mycursor = mydb.cursor()
# # # # # # # # # # # # #

# Color
def color(text, color = ''):
    col = config['color']['rest'] if color == '' else config['color']['red'] if color == 'red' else config['color']['green'] if color == 'green' else config['color']['black'] if color == 'black' else config['color']['blue'] if color == 'blue' else config['color']['cyan'] if color == 'cyan' else config['color']['purple'] if color == 'purple' else config['color']['yellow'] if color == 'yellow' else config['color']['rest']
    return col+""+text+""+config['color']['rest']

# Login with username and password
def Login(username, password):
    if username is not None:
        if password is not None:
            
            # Get username and password
            if username == config['tempUser']['username']:
                if password == config['tempUser']['password']:
                    return True

# Control Panel, Should isLogin = True
def cpanel(userID, username, isLogin = False):
    if isLogin is True:
        text = '''
            | - - - - - - - - - - - - - - - - - |
            |                                   |
                        Welcome {}                  
            |                                   |
            | - - - - - - - - - - - - - - - - - |
            '''.format(username)
        print(
            color(
                text, 'cyan'
                )
            )
                    
        # varibal loginOption to store login user option
        print(color("Select the option you want: ", "rest") + color("[1] New book [2] Books list [3] logout and exit", 'yellow'))
        loginOption = input()
                    
        if loginOption == "1" or loginOption == "new book":
            os.system('cls')
            text = '''
            | - - - - - - - - - - - - - - - - - |
            |                                   |
                        Add new book                  
            |                                   |
            | - - - - - - - - - - - - - - - - - |
            '''
            print(
                color(
                    text,'cyan'
                )
            )
            
            
            # Get Book title 
            print(color("Title: ", 'cyan'))
            bookTitle = input()
            print(color("Description: ", 'cyan'))
            bookDescription = input()
            
            
            if insertBook(userID, bookTitle, bookDescription, isLogin):
                os.system('cls')
                print(
                    color(
                        "New book recorded successfully!",'green'
                    )
                )
            else:
                os.system('cls')
                print(
                    color(
                        "Error when record new book, try again!",'red'
                    )
                )
            cpanel(userID, username, True)
            
        # Books list
        if loginOption == "2" or loginOption == "books list":
            booksList(userID, username, True)
            
            
        # Exit and logout
        elif loginOption == "3" or loginOption == "logout":
            os.system('cls')
            print(color(
                    "Logout from {}".format(config['app']['NAME']),
                    'red'
                    )
                  )
            main()
        else:
            os.system('cls')
            print(
                color(
                    "Error",
                    'red'
                )
            )
            cpanel(userID, username, True)


# user should have isLogin = True
def insertBook(userID, bookTitle, bookDescription, isLogin = False):
    if isLogin is True:
        if userID.isdigit():
            sqlInsertBook = "INSERT INTO books (userID, title, description) VALUES (%s, %s, %s)"
            val = (int(userID), bookTitle, bookDescription)
            mycursor.execute(sqlInsertBook, val)
            mydb.commit()
            return True

def booksList(userID = 0, username = 'user', isLogin = False):
    mycursor.execute("SELECT * FROM books")
    myresult = mycursor.fetchall()
    
    n = 0
    for result in myresult:
        n += 1
    #    Use join sql
        text = '''
        # [{0}]
            Title: {1}
            Description: {2}
            Author: {3}
        #
        '''.format(result[0], result[2], result[3], result[1])
       
        print(
            color(
                text,
                "green"
            )
        ) 

    print(
        color(
            "\t |=> Found {0} book(s)".format(n),
            'purple'
        )
    )

    if(isLogin == True):
        print("\n" +
            color(
                "Press enter to continue...",
                "purple"
            )
        )
        input()
        os.system('cls')
        cpanel(userID, username, True)

    else:
        print("\n" +
            color(
                "Press enter to continue...",
                "purple"
            )
        )
        input()
        os.system('cls')
        main()

def register(username, password, fullName):
    username = username if username is not None else False
    password = password if password is not None else False
    fullName = fullName if fullName is not None else False

    if username != False or password != False or fullName != False:
        os.system('cls')
        print(
            color(
                "New account",
                "green"
            )
        )
        main()
    else:
        os.system('cls')
        print(
            color(
                "Something wrong!, try again",
                "red"
            )
        )
        main()
        
def main():

    text = '''
        | ## ## ## ## ## ## ## ## ## ## ## ## ## ## |
        |                                           |
        |           Online python library           |
        |           - - - - - - - - - - -           |
        |                                           |
        | ## ## ## ## ## ## ## ## ## ## ## ## ## ## |
    '''
    print(color(text, "cyan"))
    print(color("Select the option you want: ", "rest") + color("[1] login [2] register [3] books list [4] exit (enter)", 'yellow'))
    
    # varibal option to store user option
    option = input()


    if option != "":

        # If user select option (1 or login)
        if option == "login" or option == '1':

            # Get username, password
            print(color("Username: ", 'cyan'))
            username = input()
            print(color("Pasword: ", 'cyan'))
            password = input()
            
            # Call class Login(username, password)
            if Login(username, password):
                os.system('cls')
                cpanel(config['tempUser']['userID'], username, True)
            else:
                os.system('cls')
                print(
                    color(
                        "\tUsername or password incorrect!",
                        "red"
                    )
                )
                main()
                
        # If user select option (2 or register)
        elif option == "register" or option == '2':
            
            # Ask user Username, password, Full name
            print(color("Username: ", 'cyan'))
            username = input()
            
            print(color("Pasword: ", 'cyan'))
            password = input()
            
            print(color("Full name: ", 'cyan'))
            fullName = input()
            
            register(username, password, fullName)

        # If user select option (3 or books list)
        elif option == "books list" or option == '3':
            booksList()
        
        # If user select option (3 or exit or anything!)
        else: 
            os.system('cls')
            print(color(
                    "Thanks for using {}".format(config['app']['NAME']),
                    'blue'
                    )
                  )
            exit()

    # If user does NOT select specific option, call main class again!
    else:
        os.system('cls')
        main()
    
os.system('cls')
main()
