from PIL import Image as PILImage

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Image:
    def __init__(self, width, height, base_value=BLACK):
        self.image = PILImage.Image(width, height, base_value)

    def set_pixel(self, x, y, value=WHITE):
        self.image.set_pixel(x, y, value)

    def process_values(self, values):
        for y, line in enumerate(values):
            for x, value in enumerate(line):
                self.set_pixel(x, y, value)

    def save(self, path):
        self.image.save(path)

