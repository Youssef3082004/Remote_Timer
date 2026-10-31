from helper.Colors import ACCENT, DIVIDER, WARNING, color_text
from argparse import ArgumentParser

class CLIMode:
    def __init__(self):
        self.parser = ArgumentParser()
        self.parser.add_argument("--mode","-m",type=str,
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

        self.options = [
            "Press '1' to keep the computer active and record the elapsed time.",
            "Press '2' to start a timer and subtract the elapsed time from your records.",
            "Press '3' to keep the computer active without recording time.",
            "Press '4' to show the recorded time for every day.",
            "Press '5' to show the recorded time for a specific date.",
            "Press '6' to show the total recorded time.",
            "Press '7' to close terminal.",
        ]

    def get_mode(self):
        args = self.parser.parse_args().mode
        if args is not None: return args
    
        menu = "\n".join(self.options)
        option = input(f"{color_text(menu, ACCENT)}\n{color_text('Select an option: ', WARNING)}".strip())
        print(color_text("*" * 50, DIVIDER))
        return option
