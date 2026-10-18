from data.jsondata import Json
from Controller.Cursor import Cursor
from Controller.Timer import Timer
options = [
    "- Press '1' to move the cursor and track elapsed time.",
    "- Press '2' to track over time and deacreased from elapsed time.",
    "- Press '3' to move the cursor without tracking time.",
    "- Press '4' to view your total recorded time for each day.",
    "- Press '5' to view your total recorded time for specific day.",
    "- Press '6' to view your total recorded time",
]

try:
    user_input = input(f"{"\n".join(options)}\nChoose Mode: ")
    print("*" * 50)

    if user_input == "1":
        Cursor().move(time_count=True)
    elif user_input == "2":
        Timer().Calc(add=False)
    elif user_input == "3": 
        Cursor().move(time_count=False)
    elif user_input == "4": 
        Json().select_by_date()
    elif user_input == "5": 
        day = input("Write Date: ")
        Json().select_by_date(date=day)
    elif user_input == "6":
        Json().total_time(formated=True)
    else: 
        print("oops! You Choosed Mode not Exist")

except KeyboardInterrupt:
    print("Program Stopped!")
