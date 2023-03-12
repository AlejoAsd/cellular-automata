from PIL import Image as PILImage, ImageDraw as PILImageDraw

WHITE = (1,)
BLACK = (0,)


class Image:
    def __init__(self, width, height, scale=10, base_value=BLACK):
        self.scale = scale
        self.image = PILImage.new('1', [width * scale, height * scale], base_value)
        self.image_draw = PILImageDraw.Draw(self.image)

    def _scale_value(self, value):
        return value * self.scale

    def _scale_iterable(self, iterable):
        return [self._scale_value(i) for i in iterable]

    def set_pixel(self, x, y, value=BLACK):
        coords = self._scale_iterable([x, y, x+1, y+1])
        self.image_draw.rectangle(coords, fill=value)

    def process_values(self, values):
        for y, line in enumerate(values):
            for x, value in enumerate(line):
                self.set_pixel(x, y, value)

    def show(self, path):
        self.image.show(path)

    def save(self, path):
        self.image.save(path)

