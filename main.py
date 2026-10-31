#!/usr/bin/env bash

from data.jsondata import Json
from helper.Cursor import Cursor
from helper.Timer import Timer
from helper.Colors import ERROR, SUCCESS, WARNING, color_text
from Controller.CLIMode import CLIMode


mode = CLIMode().get_mode()

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
