from data.jsondata import Json
from Controller.Cursor import Cursor

user_input = input("- press '1' if you want to move cursor\n- press '2' to show all remaining time\nyour input: ")
print("*" * 50)

if user_input == "1":
    Cursor().move()
elif user_input == "2": 
    Json().select_by_date()
else: 
    print("oops! Please Choose '1' or '2'")