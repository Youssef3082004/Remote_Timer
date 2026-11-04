from colorama import Fore, Style, init


init()

INFO = Fore.CYAN
SUCCESS = Fore.GREEN
WARNING = Fore.YELLOW
ERROR = Fore.RED
ACCENT = Fore.MAGENTA
DIVIDER = Fore.BLUE


def color_text(text: str, color: str) -> str:
    return f"{color}{text}{Style.RESET_ALL}"
