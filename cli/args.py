import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "-a",
    "--add",
    nargs="?",
    const=True,
    help=("add new milestone entry"),
)

args = parser.parse_args()
