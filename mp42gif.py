from argparse import ArgumentParser
from src.main import *


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument('-f', '--filename', type=str)
    parser.add_argument('-c', '--compression', type=float, default=100)
    parser.add_argument('-b', '--backend', type=str, default='imagemagick')
    parser.add_argument('-o', '--output', type=str, default='')
    parser.add_argument('-i', '--interactive', help='Interactive mode', action='store_true')

    args = parser.parse_args()
    
    if args.interactive:
        args.filename = input('Enter filename of mp4: ')
        args.compression = input('Enter compression in percent (leave blank for none): ')
        if not args.compression:
            args.compression = 100
        args.output = input('Enter filename to save to (leave blank if same as source filename): ')
        args.backend = input('Enter writer backend (leave blank to autodetect): ')
        if not args.backend:
            args.backend = 'imagemagick'
        if not args.output:
            args.output = args.filename
    else:
        if not args.output:
            args.output = f'{args.filename.split(".")[0]}.gif'

    frames, fps = read_file(args.filename, args.compression, args.output)
    save_file(args.output, frames, fps, args.backend)


if __name__ == '__main__':
    main()
