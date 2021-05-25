"""
A python library for some additional and helpful things.
"""

__version__ = '1.0.0'
__author__ = 'QuatschVirus'
__license__ = 'MIT'


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
