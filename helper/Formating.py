from helper.Colors import SUCCESS, color_text


class Formating:

    def format_duration(self, seconds: int, print_result: bool = True) -> str:
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        formatted_duration = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        if print_result:
            print(color_text(f"Recorded time: {formatted_duration}", SUCCESS))

        return formatted_duration
