from pydantic import BaseModel
from helper.Formating import Formating

class Day(BaseModel):
    date: str
    seconds: int

    @property
    def formatted_duration(self) -> str:
        return Formating().format_duration(seconds=self.seconds, print_result=False)
