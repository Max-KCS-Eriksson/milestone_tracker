import datetime


class Milestone:
    def __init__(self, event: str, year: int, month: int, date: int):
        try:
            _ = datetime.date(year, month, date)
        except ValueError as e:
            raise e
        else:
            self.event = event
            self.year = year
            self.month = month
            self.date = date

    def days_since(self):
        """Return number of days since milestone happened"""
        return (
            datetime.date.today() - datetime.date(self.year, self.month, self.date)
        ).days
