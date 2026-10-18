
class Formating:
    def format(self,seconds_input:int,print_statement:bool = True):
        hours, remainder = divmod(seconds_input, 3600)                        
        minutes, seconds = divmod(remainder, 60) 

        if print_statement:                       
            print(f"Your Total recorded time =  {hours:02d}:{minutes:02d}:{seconds:02d}")

        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        