import datetime

from milestones.milestone import Milestone


def input_int(prompt):
    value = input(prompt)
    try:
        return int(value)
    except ValueError:
        print("Input error: enter integer")
        input_int(prompt)


def input_milestone_details():
    print("Enter milestone details")
    return {
        "event": input("event: "),
        "year": input_int("year: "),
        "month": input_int("month: "),
        "date": input_int("date: "),
    }


def list_milestones(milestones: dict):
    for milestone, date in milestones.items():
        print(f"{milestone}: {datetime.date(*date.values())}")


def print_time_passed_since(milestone: Milestone):
    print(f"{milestone.days_since()} days since {milestone.event}")
