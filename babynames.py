#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration. Here's what the HTML looks like in the
baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 - Extract all the text from the file and print it
 - Find and extract the year and print it
 - Extract the names and rank numbers and print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extracted_names list
"""
__author__ = """
stephguirand
Help from demo, lessons and activities, youtube videos in canvas and
own search on youtube,
stack overflow, Tutors, Facilitators and talking about assignment
in study group.
"""

import argparse
import re
import sys


def extract_names(filename):
    """
    Given a single file name for babyXXXX.html, returns a
    single list starting with the year string followed by
    the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """
    names = []
    f = open(filename, 'rU')
    text = f.read()

    # Get the year
    year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
    if not year_match:
        # did not find a year, exit with an error message
        sys.stderr.write('unavailable year!\n')
        sys.exit(1)
    year = year_match.group(1)
    names.append(year)

    # extract all the data tuples with a findall()
    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)', text)
    # print(tuples)

    # store data into a dict using ea name as a key and that
    # name's rank number as the value.
    # (if the name is already in there, don't add it, since
    # this new rank will be bigger than the previous rank)

    names_in_group = {}
    for group_tuple in tuples:
        (group, boyname, girlname) = group_tuple  # unpack the tuple into 3vars
        if boyname not in names_in_group:
            names_in_group[boyname] = group
        if girlname not in names_in_group:
            names_in_group[girlname] = group

    # get the names, sorted in the right order
    sorted_names = sorted(names_in_group)
    for name in sorted_names:
        names.append(f"{name} {names_in_group[name]}")
    # +++your code here+++
    return(names)


def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more
    # filenames. It will also expand wildcards just like the shell.
    # e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):
    """Create a command line parser object with parsing rules"""
    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    file_list = ns.files

    # option flag
    create_summary = ns.summaryfile

    # For each filename, call `extract_names()` with that single file.
    # Format the resulting list as a vertical list (separated by newline \n).
    # Use the create_summary flag to decide whether to print the list
    # or to write the list to a summary file (e.g. `baby1990.html.summary`).

    # +++your code here+++
    for filename in file_list:
        # print("writing for", filename)
        names = extract_names(filename)
        lines = '\n'.join(names)  # make lines out of the whole list
        if create_summary:
            with open(filename + '.summary', 'w') as f:
                f.write(lines)
        else:
            print(lines)


if __name__ == '__main__':
    main(sys.argv[1:])
