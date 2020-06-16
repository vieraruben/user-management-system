from resources.helpers import * 
from classes.UserDB import UserDB
from classes.Switch import Switch

if __name__=="__main__": 
    # Variables
    user_db = UserDB()
    user_db.load_user_data() # Load data from json file
    switch = Switch(user_db)
    q = ""

    while q != 'q':
        choice_messages()
        choice = input("")
        clear()
        switch.check(choice)