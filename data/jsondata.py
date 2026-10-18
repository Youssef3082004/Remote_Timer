import json
import datetime
from Model.Day import Day
from helper.Formating import Formating

class Json:

    def load(self) -> list[Day]:
        try:
            with open("time.json", "r") as file:
                return [Day(**record) for record in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save(self, content: list[Day]):
        with open("time.json", "w") as file:
            json.dump([record.model_dump() for record in content],file,indent=2)

    def add(self, seconds: int):
        content = self.load()
        today = datetime.datetime.now().strftime("%d/%m/%Y")

        for record in content:
            if record.date == today:
                record.seconds += seconds
                break
        else:
            content.append(Day(date=today, seconds=seconds))

        self.save(content)


    def decrease(self, seconds: int):
        content = self.load()

        if seconds <= 0: return
        content.sort(key=lambda day: datetime.datetime.strptime(day.date, "%d/%m/%Y"),reverse=True)

        for day in content:
            if seconds <= 0:
                break

            deducted = min(day.seconds, seconds)
            day.seconds -= deducted
            seconds -= deducted
        self.save(content)


    def total_time(self,formated:bool = False) -> int | str:
        total = sum(day.seconds for day in self.load())
        
        return Formating().format(total) if formated else total
             

    def select_by_date(self, date: str = None) -> None:
        for day in self.load():
            if date is None:
                print(f"{day.date} : {day.Format}")
            elif day.date.startswith(date):
                print(f"{day.date} : {day.Format}")