import math

from generator import Generator
from random import randint

from image import Image


def random_line(size):
    return [randint(0, 1) for i in range(size)]


def compile_rule(str_rule):
    return int(str_rule, 2)


if __name__ == '__main__':
    width = 1000
    height = 1000
    resolution = 3

    for i in range(256):
        print(i)
        gen = Generator(resolution, i)
        values = gen.generate(random_line(width), height)
        image = Image(width, height)
        image.process_values(values)
        image.save('./' + str(i) + '.png', 4)
