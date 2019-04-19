#!/usr/bin/env python
import subprocess
import argparse
from time import sleep
from CoreAutomation import *
import re
import time

if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cleanup', dest='cleanup')
    parser.add_argument('-fp', '--fpsetup', dest='fpsetup')
    parser.add_argument('-sp', '--spsetup', dest='spsetup')
    parser.add_argument('-ffp', '--ffpsetup', dest='ffpsetup')

    args = parser.parse_args()

    if args.cleanup:
        print "cleanup"
    if args.fpsetup:
        print "fpsetup"
    if args.spsetup:
        print "spsetup"
    if args.ffpsetup:
        print "ffpsetup"
