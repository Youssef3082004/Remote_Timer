from data.jsondata import Json
from Controller.Cursor import Cursor
from Controller.Timer import Timer

options = [
    "press '1' to Keep the computer active and record the elapsed time.",
    "press '2' to Start a timer and subtract the elapsed time from your records.",
    "press '3' to Keep the computer active without recording time.",
    "press '4' to Show the recorded time for every day.",
    "press '5' to Show the recorded time for a specific date.",
    "press '6' to Show the total recorded time.",
]

try:
    menu = "\n".join(options)
    user_input = input(f"{menu}\nSelect an option: ")
    print("*" * 50)

    if user_input == "1":
        Cursor().keep_computer_active(record_elapsed_time=True)
    elif user_input == "2":
        Timer().track_elapsed_time(add_to_records=False)
    elif user_input == "3": 
        Cursor().keep_computer_active(record_elapsed_time=False)
    elif user_input == "4": 
        Json().display_records_by_date()
    elif user_input == "5": 
        day = input("Enter a date (DD/MM/YYYY): ")
        Json().display_records_by_date(date_prefix=day)
    elif user_input == "6":
        print(f"Total Recorded Time = {Json().get_total_time(formatted=True)}")
    else: 
        print("That option does not exist. Please select a number from 1 to 6.")

except KeyboardInterrupt:
    print("\nProgram Stopped.")
