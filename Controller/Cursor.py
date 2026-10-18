import pyautogui
import time     
from data.jsondata import Json
from helper.Formating import Formating
class Cursor:

    def move(self):
        print("Mouse mover started. Press Ctrl+C to stop.")                                                                                     
        start_time = time.monotonic()                                       
        try:                                                                
            while True:                                                     
                # Get current mouse position                                
                x, y = pyautogui.position()                                 

                # Move cursor 100 pixels to the right                       
                pyautogui.moveTo(x + 100, y + 100, duration=0.5)            
                time.sleep(1)                                               

                # Return cursor to original position                        
                pyautogui.moveTo(x, y, duration=0.5)                        

                # Wait 60 seconds                                           
                time.sleep(60)                                              

        except KeyboardInterrupt:                                           
            print("\nMouse mover stopped.")                                 

        finally:                                                            
            elapsed = int(time.monotonic() - start_time)                    
            Json().add(seconds=elapsed)  
            Formating().format(seconds_input=elapsed)                                   
                                                                        