import random


def choose_random(*objects):
    if type(objects) is tuple:
        objects = list(objects)
    random.shuffle(objects)
    choose = random.randint(0, len(objects) - 1)
    selection = objects[choose]
    return selection


def random_sequence(length: int):
    sequence = ''
    for i in range(length + 1):
        sequence.join(chr(random.randint(97, 122)))
    return sequence
