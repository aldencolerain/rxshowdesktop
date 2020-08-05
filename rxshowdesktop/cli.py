import sys
import argparse
from . import desktop


def main():
    # arguments
    parser = argparse.ArgumentParser(description='')
    subparsers = parser.add_subparsers(help='')

    # desktop commands
    add_parser = subparsers.add_parser('show', help='show desktop')
    add_parser.set_defaults(cmd=desktop.show)

    add_parser = subparsers.add_parser('hide', help='unshow / hide desktop')
    add_parser.set_defaults(cmd=desktop.hide)

    add_parser = subparsers.add_parser('toggle', help='show desktop if hidden, hide desktop if showing')
    add_parser.set_defaults(cmd=desktop.toggle)

    add_parser = subparsers.add_parser('status', help='display status, is desktop showing?')
    add_parser.set_defaults(cmd=lambda: print('showing desktop') if desktop.showing() else print('desktop hidden'))

    add_parser = subparsers.add_parser('locate', help='show package icon locations')
    add_parser.set_defaults(cmd=desktop.locate)

    # parse args and execute command
    args = parser.parse_args()
    if hasattr(args, 'cmd'):
        args.cmd()
        sys.exit()
    else:
        parser.print_help()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
