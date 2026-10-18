import time
from data.jsondata import Json
from helper.Formating import Formating


class Timer:

    def Calc(self, add: bool = True):
        start_time = time.monotonic()
        print(f"{'Increase' if add else 'Decrease'} Timer Started. Press Ctrl+C to stop.")
        try:
            while True:
                time.sleep(1)

        except KeyboardInterrupt:
            elapsed = int(time.monotonic() - start_time)

            if add:
                Json().add(seconds=elapsed)
            else:
                Json().decrease(seconds=elapsed)

            print("\nTimer stopped.")
            Formating().format(seconds_input=elapsed)