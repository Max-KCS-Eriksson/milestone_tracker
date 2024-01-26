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
