#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple sample module with Skype smileys
"""

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--on", help="tells the world you are on the DB", action="store_true")
parser.add_argument("--off", help="tells the world you are off the DB", action="store_true")

args = parser.parse_args()

if args.on:

	print "X-Bot issues verbal lock: %s is on the database" % os.environ["SKYPE_FULLNAME"]

if args.off:

	print "X-Bot removes verbal lock: %s is off the database.  Please run git pull && bin/load-database" % os.environ["SKYPE_FULLNAME"]
