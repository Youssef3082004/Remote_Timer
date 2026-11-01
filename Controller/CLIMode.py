from helper.Colors import ACCENT, DIVIDER, WARNING, color_text
from argparse import ArgumentParser,RawTextHelpFormatter

class CLIMode:
    def __init__(self):
        self.parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
        self.parser.add_argument("--mode","-m",type=str,
            help=(
                "Select a menu option directly and skip the main menu prompt.\n\n"
                "Available modes:\n"
                "  1 = Keep the computer active and record time\n"
                "  2 = Start a timer and subtract elapsed time\n"
                "  3 = Keep the computer active without recording time\n"
                "  4 = Show records for every day\n"
                "  5 = Show records for a specific date\n"
                "  6 = Show total recorded time\n"
                "  7 = Close the program\n\n"
                "Example: python3 main.py -m 1 || timer -m 1 (if Installed in your os)"
            )
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
