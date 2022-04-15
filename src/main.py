#! /usr/bin/python

import random
import json
import os
import argparse
from math import ceil
from pathlib import Path


# minor definitions
def group_count(group_size):
    return ceil(len(people) / group_size)


def remove_absent():
    for person in absent_people:
        people.remove(person.lower())


# main make group function
def make_groups(count):
    for n in range(count):  # total group
        tmp_array = []
        if size < len(people):
            for i in range(size):  # per person
                idx = random.randint(0, len(people) - 1)
                person = people[idx]
                people.remove(person)
                tmp_array.append(person)
            print(f'Group {n + 1}: {tmp_array}')
            tmp_array.clear()
        else:
            print(f'Group {n + 1}: {people}')


if __name__ == '__main__':
    # path definitions & global definitions
    path = Path(os.path.dirname(__file__)).parent
    resources_dir = os.path.join(path, 'resources')
    people_file = os.path.join(resources_dir, 'people.json')
    class_name = None

    # arg parser setup
    parser = argparse.ArgumentParser(description='generates groups based on size and class.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-A', '--am', action='store_true')
    group.add_argument('-P', '--pm', action='store_true')
    parser.add_argument('--absent', metavar='PERSON', nargs='+', help='People absent separated by spaces')
    parser.add_argument('size', metavar='SIZE', type=int, help='Size of each group')

    # arg parsing
    args = parser.parse_args()
    size = args.size
    absent_people = args.absent

    if args.am:
        class_name = 'AM'
    elif args.pm:
        class_name = 'PM'

    with open(people_file) as json_file:
        data = json.load(json_file)
        people = data[class_name]

    if isinstance(absent_people, list):
        remove_absent()

    gcount = group_count(size)
    make_groups(gcount)
