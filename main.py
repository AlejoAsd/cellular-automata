from generator import Generator
from random import randint

from image import Image


def random_line(size):
    return [randint(0, 1) for i in range(size)]


def compile_rule(str_rule):
    return int(str_rule, 2)


if __name__ == '__main__':
    width = 200
    height = 200

    gen = Generator(3, compile_rule('01010101'))
    # values = gen.generate([1, 0, 0, 0, 1, 1], height)
    # values = gen.generate(random_line(width), height)
    values = gen.generate([0]*100 + [1] + [0] * 99, height)

    image = Image(width, height)
    values = image.process_values(values)
    image.save('./test.png', 4)
