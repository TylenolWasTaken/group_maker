import random;from math import ceil  # ;)
people = ['aiden', 'jayden', 'nolan', 'conner', 'colin']
for n in range(ceil(len(people) / 2)):  # total group
    tmp_array = []
    if 2 < len(people):
        for i in range(2):  # per person
            idx = random.randint(0, len(people) - 1)
            person = people[idx]
            people.remove(person)
            tmp_array.append(person)
        print(f'Group {n + 1}: {tmp_array}')
        tmp_array.clear()
    else:
        print(f'Group {n + 1}: {people}')