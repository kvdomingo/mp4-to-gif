from argparse import ArgumentParser
from src.main import *


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument('-f', '--filename', type=str)

    args = parser.parse_args()

    frames, fps = read_file(args.filename)
    save_file(args.filename, frames, fps)


if __name__ == '__main__':
    main()
