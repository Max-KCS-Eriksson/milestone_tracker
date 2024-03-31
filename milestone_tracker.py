#!/usr/bin/env python3

from cli import tui
from cli.args import args, parser
from milestones.milestone import Milestone
from milestones.storage import Storage

STORAGE = Storage()

if args.add:
    details = tui.input_milestone_details()

    STORAGE.add_milestone(Milestone(**details))

elif args.list_milestones:
    tui.list_milestones(STORAGE.milestones)

elif args.time_since:
    event = args.time_since
    date_details = STORAGE.milestones[event]

    tui.print_time_passed_since(Milestone(event, **date_details))

else:
    parser.print_help()
