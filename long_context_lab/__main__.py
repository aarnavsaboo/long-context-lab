from argparse import ArgumentParser
import json
from .needles import make_task


def main():
    parser = ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    make = sub.add_parser("make")
    make.add_argument("--tokens", type=int, default=4096)
    make.add_argument("--position", type=float, default=.5)
    make.add_argument("--seed", default="0")
    args = parser.parse_args()
    task = make_task(args.tokens * 4, args.position, args.seed)
    print(json.dumps(task.__dict__))


if __name__ == "__main__":
    main()
