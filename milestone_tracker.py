#!/usr/bin/env python3

from types import FunctionType

from cli import tui
from cli.args import args, parser
from milestones.milestone import Milestone
from milestones.storage import Storage

STORAGE = Storage()


def show_time_since_event(event: str, show_function: FunctionType):
    try:
        date = STORAGE.milestones[event]
    except KeyError:
        tui.event_not_found(event)
    else:
        show_function(Milestone(event, **date))


if args.add:
    details = tui.input_milestone_details()

    STORAGE.add_milestone(Milestone(**details))

elif args.list_milestones:
    tui.list_milestones(STORAGE.milestones)

elif args.time_since:
    event = args.time_since
    show_time_since_event(event, tui.days_passed_since)

elif args.months_since:
    event = args.months_since
    show_time_since_event(event, tui.months_passed_since)

else:
    parser.print_help()
