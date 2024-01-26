#!/usr/bin/env python3

from cli.args import args
from cli.tui import input_milestone_details, list_milestones, print_time_passed_since
from milestones.milestone import Milestone
from milestones.storage import Storage

STORAGE = Storage()

if args.add:
    details = input_milestone_details()

    STORAGE.add_milestone(Milestone(**details))

if args.list_milestones:
    list_milestones(STORAGE.milestones)

if args.time_since:
    targes_milestone_event = args.time_since

    # Assemble `Milestone` from given arg and info from `STORAGE.milestones`

    print_time_passed_since(
        Milestone(targes_milestone_event, **STORAGE.milestones[targes_milestone_event])
    )
