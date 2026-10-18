import time
from data.jsondata import Json
from helper.Colors import INFO, WARNING, color_text
from helper.Formating import Formating

class Cursor:

    def keep_computer_active(self, record_elapsed_time: bool = True) -> None:
        import pyautogui

        print(color_text("Mouse mover started. Press Ctrl+C to stop.", INFO))
        start_time = time.monotonic()
        try:
            while True:
                # Get the current mouse position.
                x, y = pyautogui.position()

                # Move the cursor away from and back to its original position.
                pyautogui.moveTo(x + 100, y + 100, duration=1)
                time.sleep(1)
                pyautogui.moveTo(x, y, duration=1)

                # Repeat every eight minutes.
                time.sleep(60 * 8)
        except KeyboardInterrupt:
            print(color_text("\nMouse mover stopped.", WARNING))
        finally:
            if record_elapsed_time:
                elapsed = int(time.monotonic() - start_time)
                Json().add_time(seconds=elapsed)
                Formating().format_duration(seconds=elapsed)
