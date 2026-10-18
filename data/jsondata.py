import json
import datetime
from Model.Day import Day
from helper.Colors import INFO, color_text
from helper.Formating import Formating

class Json:

    def load_records(self) -> list[Day]:
        try:
            with open("time.json", "r") as file:
                return [Day(**record) for record in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_records(self, records: list[Day]) -> None:
        with open("time.json", "w") as file:
            json.dump([record.model_dump() for record in records], file, indent=2)

    def add_time(self, seconds: int) -> None:
        records = self.load_records()
        today = datetime.datetime.now().strftime("%d/%m/%Y")

        for record in records:
            if record.date == today:
                record.seconds += seconds
                break
        else:
            records.append(Day(date=today, seconds=seconds))

        self.save_records(records)


    def deduct_time(self, seconds: int) -> None:
        records = self.load_records()

        if seconds <= 0:
            return
        records.sort(key=lambda day: datetime.datetime.strptime(day.date, "%d/%m/%Y"),reverse=True,)

        for day in records:
            if seconds <= 0:
                break

            deducted = min(day.seconds, seconds)
            day.seconds -= deducted
            seconds -= deducted
        self.save_records(records)


    def get_total_time(self, formatted: bool = False) -> int | str:
        total = sum(day.seconds for day in self.load_records())

        return Formating().format_duration(total, print_result=False) if formatted else total

    def display_records_by_date(self, date_prefix: str | None = None) -> None:
        for day in self.load_records():
            if date_prefix is None or day.date.startswith(date_prefix):
                print(color_text(f"{day.date} = {day.formatted_duration}", INFO))
