import datetime

from milestones.milestone import Milestone


def input_int(prompt):
    value = input(prompt)
    try:
        value = int(value)
    except ValueError:
        print("Input error: enter integer")
        value = input_int(prompt)
    return value


def input_milestone_details():
    print("Enter milestone details")
    return {
        "event": input("event: "),
        "year": input_int("year: "),
        "month": input_int("month: "),
        "day": input_int("day: "),
    }


def list_milestones(milestones: dict):
    unsorted_list = []
    for milestone, date in milestones.items():
        unsorted_list.append(f"{datetime.date(*date.values())} {milestone}")

    for milestone in sorted(unsorted_list):
        print(milestone)


def days_passed_since(milestone: Milestone):
    print(f"{milestone.days_since()} days since {milestone.event}")


def months_passed_since(milestone: Milestone):
    print(f"{milestone.months_since()} months since {milestone.event}")


def event_not_found(event):
    print(f'Event not found: "{event}"')
