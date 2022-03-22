import random as rand
import json
import os
import sys
from math import floor, ceil

# argv/argc definitions
argv = sys.argv
argc = len(sys.argv)  # starting at 1


# check for params
if argc < 2:
    print("""
[Error] No names file given, you can make your own based on the json formatting in resources/people.json

USAGE: main.py [people_file]
""")
    exit(1)
elif argc > 2:
    absent_people = argv[2:]


# Future defs
resources_dir = os.path.join('F:\\', 'repos', 'ctc_idk', 'resources')
people_file = os.path.join(resources_dir, f'{argv[1]}')
size = 2

with open(people_file) as json_file:  # TODO: people in global space
    data = json.load(json_file)
    people = data['people']


def group_count(group_size):
    return ceil(len(people) / group_size)


def remove_absent():  # TODO: unlink people var
    temp_people = people
    for person in absent_people:
        temp_people.remove(person.lower())
    return temp_people


def make_groups(count, people):
    g_count = group_count(size)
    for n in range(g_count):
        pass


if __name__ == '__main__':
    people = remove_absent()
