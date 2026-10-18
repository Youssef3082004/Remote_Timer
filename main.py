from data.jsondata import Json
from Controller.Cursor import Cursor
from Controller.Timer import Timer
from helper.Colors import ACCENT, DIVIDER, ERROR, SUCCESS, WARNING, color_text

options = [
    "Press '1' to keep the computer active and record the elapsed time.",
    "Press '2' to start a timer and subtract the elapsed time from your records.",
    "Press '3' to keep the computer active without recording time.",
    "Press '4' to show the recorded time for every day.",
    "Press '5' to show the recorded time for a specific date.",
    "Press '6' to show the total recorded time.",
    "Press '7' to close terminal",

]

try:
    menu = "\n".join(options)
    user_input = input(
        f"{color_text(menu, ACCENT)}\n{color_text('Select an option: ', WARNING)}"
    )
    print(color_text("*" * 50, DIVIDER))

    if user_input == "1":
        Cursor().keep_computer_active(record_elapsed_time=True)
    elif user_input == "2":
        Timer().track_elapsed_time(add_to_records=False)
    elif user_input == "3": 
        Cursor().keep_computer_active(record_elapsed_time=False)
    elif user_input == "4": 
        Json().display_records_by_date()
    elif user_input == "5": 
        day = input(color_text("Enter a date (DD/MM/YYYY): ", WARNING))
        Json().display_records_by_date(date_prefix=day)
    elif user_input == "6":
        total = Json().get_total_time(formatted=True)
        print(color_text(f"Total recorded time: {total}", SUCCESS))
    elif user_input == "7":
        print(color_text("Terminal is Closed!", ERROR))
    else: 
        message = "That option does not exist. Please select a number from 1 to 7."
        print(color_text(message, ERROR))

except KeyboardInterrupt:
    print(color_text("\nProgram stopped.", WARNING))
