from pydantic import BaseModel
from helper.Formating import Formating

class Day(BaseModel):
    date: str
    seconds: int

    @property
    def Format(self):
        return Formating().format(seconds_input=self.seconds,print_statement=False)