import math

MismatchedSize = Exception("Mismatched size.")


class Generator:
    def __init__(self, resolution, seed):
        self.resolution = resolution
        self.seed = seed

    def _get_skip(self, values):
        skip = 0
        for index, value in enumerate(reversed(values)):
            skip += value * 2 ** index
        return skip

    def _compute_new_value(self, values):
        if len(values) != self.resolution:
            raise MismatchedSize

        return (self.seed >> self._get_skip(values)) & 1

    def _get_window(self, line, pos):
        pos -= self.resolution // 2
        window = []
        for i in range(pos, pos + self.resolution):
            window.append(line[i % len(line)])
        return window

    def _compute_new_line_value(self, line, pos):
        window = self._get_window(line, pos)
        return self._compute_new_value(window)

    def _generate_line(self, line):
        new_line = [0] * len(line)
        for pos in range(len(line)):
            new_line[pos] = self._compute_new_line_value(line, pos)
        return new_line

    def generate(self, line, height):
        lines = [line]
        for i in range(height-1):
            line = self._generate_line(line)
            lines.append(line)
        return lines




