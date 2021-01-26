from argparse import ArgumentParser
from src.main import *


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument('-f', '--filename', type=str)
    parser.add_argument('-c', '--compression', type=int, default=100)
    parser.add_argument('-o', '--output', type=str, default='')

    args = parser.parse_args()
    if not args.output:
        args.output = f'{args.filename.split(".")[0]}.gif'

    frames, fps = read_file(args.filename, args.compression, args.output)
    save_file(args.output, frames, fps)


if __name__ == '__main__':
    main()
