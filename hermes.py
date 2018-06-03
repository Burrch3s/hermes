#!/usr/bin/python3


import argparse
from funcs.now import *
from funcs.later import *

def init_args():

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(
            dest='cmd',
            help="Choose between current options: now or later for poster")

    # hermes now <args>
    now = subparser.add_parser(
            "now",
            help="Get a poster right now!")
    now.add_argument(
            "-n",
            dest="number",
            default=1,
            type=int,
            help="Number of posters to grab")
    now.add_argument(
            "-s",
            dest="save",
            default=False,
            action="store_true",
            help="Save picture for later")

    # hermes later <args>
    later = subparser.add_parser(
            "later",
            help="Schedule a poster for later!")
    later.add_argument(
            "-t",
            dest="time",
            type=int,
            help="Hour to present picture at (obviously cant use -h ugh)")
    later.add_argument(
            "-m",
            dest="minute",
            type=int,
            default=0,
            help="Minute of the hour to present picture at")
    later.add_argument(
            "-d",
            dest="daily",
            default=False,
            action="store_true",
            help="Schedule poster at HH:MM of every day")

    return(parser)


if __name__ == '__main__':
    parser = init_args()
    args = parser.parse_args()

    if args.cmd == 'now':
        get_picture()
