import time
from data.jsondata import Json
from helper.Formating import Formating


class Timer:

    def track_elapsed_time(self, add_to_records: bool = True) -> None:
        start_time = time.monotonic()
        action = "add it to" if add_to_records else "subtract it from"
        print(f"Timer started. Press Ctrl+C to stop and {action} your records.")
        try:
            while True:
                time.sleep(1)

        except KeyboardInterrupt:
            elapsed = int(time.monotonic() - start_time)

            if add_to_records:
                Json().add_time(seconds=elapsed)
            else:
                Json().deduct_time(seconds=elapsed)

            print("\nTimer stopped.")
            Formating().format_duration(seconds=elapsed)
