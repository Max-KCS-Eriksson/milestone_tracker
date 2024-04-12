import datetime


class Milestone:
    def __init__(self, event: str, year: int, month: int, day: int):
        try:
            _ = datetime.date(year, month, day)
        except ValueError as e:
            raise e
        else:
            self.event = event
            self.year = year
            self.month = month
            self.day = day

    def days_since(self):
        """Return number of days since milestone happened"""
        return (
            datetime.date.today() - datetime.date(self.year, self.month, self.day)
        ).days

    def months_since(self):
        """Return number of months since milestone happened"""
        today = datetime.date.today()
        num_of_months = (today.year - self.year) * 12 + today.month - self.month
        if today.day < self.day:
            num_of_months -= 1

        return num_of_months
