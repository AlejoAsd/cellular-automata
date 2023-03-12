import unittest

from generator import Generator


class GeneratorTestCase(unittest.TestCase):
    def test_get_skip_resolution_3(self):
        resolution = 3
        gen = Generator(resolution, 0)
        self.assertEqual(gen._get_skip([1, 1, 1]), 7)
        self.assertEqual(gen._get_skip([1, 0, 0]), 4)
        self.assertEqual(gen._get_skip([0, 0, 1]), 1)
        self.assertEqual(gen._get_skip([0, 0, 0]), 0)

    def test_compute_value_resolution_3(self):
        resolution = 3
        gen = Generator(resolution, int('10000000', 2))
        self.assertEqual(gen._compute_new_line_value((1, 1, 1)), 1)
        self.assertEqual(gen._compute_new_line_value((0, 0, 0)), 0)

        gen = Generator(resolution, int('10000001', 2))
        self.assertEqual(gen._compute_new_line_value((1, 1, 1)), 1)
        self.assertEqual(gen._compute_new_line_value((0, 0, 0)), 1)

    def test_get_window_resolution_3(self):
        resolution = 3
        gen = Generator(resolution, 0)
        self.assertEqual(gen._get_window([1], 0), [0, 1, 0])
        self.assertEqual(gen._get_window([1, 1, 1, 1, 1], 0), [0, 1, 1])
        self.assertEqual(gen._get_window([1, 1, 1, 1, 1], 1), [1, 1, 1])
        self.assertEqual(gen._get_window([1, 1, 1, 1, 1], 2), [1, 1, 1])
        self.assertEqual(gen._get_window([1, 1, 1, 1, 1], 3), [1, 1, 1])
        self.assertEqual(gen._get_window([1, 1, 1, 1, 1], 4), [1, 1, 0])
        self.assertEqual(gen._get_window([1, 1, 1, 1, 1], 5), [1, 0, 0])

    def test_generate_resolution_3(self):
        gen = Generator(3, int('01010101', 2))
        expected = [
            [1, 0, 0, 0, 1, 1],
            [1, 1, 1, 0, 0, 1],
            [0, 0, 1, 1, 0, 1],
            [1, 0, 0, 1, 0, 1],
            [1, 1, 0, 1, 0, 1],
        ]
        height = len(expected)
        result = gen.generate(expected[0], height)
        self.assertEqual(height, len(result))
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
