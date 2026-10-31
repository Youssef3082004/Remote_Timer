#!/usr/bin/env bash

from data.jsondata import Json
from Controller.Cursor import Cursor
from Controller.Timer import Timer
from helper.Colors import ACCENT, DIVIDER, ERROR, SUCCESS, WARNING, color_text
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--mode","-m",type=str,
    help=(
        "Select a menu option directly and skip the main menu prompt. "
        "Available modes: 1=keep the computer active and record time, "
        "2=start a timer and subtract elapsed time, "
        "3=keep the computer active without recording time, "
        "4=show records for every day, 5=show records for a specific date, "
        "6=show total recorded time, 7=close the program. "
        "Example: main.py -m 1"
    ),
)
args = parser.parse_args()

options = [
    "Press '1' to keep the computer active and record the elapsed time.",
    "Press '2' to start a timer and subtract the elapsed time from your records.",
    "Press '3' to keep the computer active without recording time.",
    "Press '4' to show the recorded time for every day.",
    "Press '5' to show the recorded time for a specific date.",
    "Press '6' to show the total recorded time.",
    "Press '7' to close terminal.",
]

def get_mode(cli_mode):
    if cli_mode is not None:
        return cli_mode

    menu = "\n".join(options)
    option = input(f"{color_text(menu, ACCENT)}\n{color_text('Select an option: ', WARNING)}".strip())
    print(color_text("*" * 50, DIVIDER))
    return option

mode = get_mode(args.mode)

try:
    if mode =="1":
        Cursor().keep_computer_active(record_elapsed_time=True)
    elif mode =="2":
        Timer().track_elapsed_time(add_to_records=False)
    elif mode =="3": 
        Cursor().keep_computer_active(record_elapsed_time=False)
    elif mode =="1": 
        Json().display_records_by_date()
    elif mode =="5": 
        day = input(color_text("Enter a date (DD/MM/YYYY): ", WARNING))
        Json().display_records_by_date(date_prefix=day)
    elif mode=="6":
        total = Json().get_total_time(formatted=True)
        print(color_text(f"Total Recorded Time = {total}", SUCCESS))
    elif mode =="7":
        print(color_text("Terminal is Closed!", ERROR))
    else: 
        message = "That option does not exist. Please select a number from 1 to 7."
        print(color_text(message, ERROR))

except KeyboardInterrupt:
    print(color_text("\nProgram stopped.", WARNING))
