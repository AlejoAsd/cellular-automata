from PIL import Image as PILImage, ImageDraw as PILImageDraw

WHITE = (1,)
BLACK = (0,)


class Image:
    def __init__(self, width, height, base_value=WHITE):
        self.image = PILImage.new('1', [width, height], base_value)
        self.image_draw = PILImageDraw.Draw(self.image)

    def set_pixel(self, x, y, value=BLACK):
        self.image_draw.point([x, y, x+1, y+1], fill=value)

    def process_values(self, values):
        for y, line in enumerate(values):
            for x, value in enumerate(line):
                self.set_pixel(x, y, value)

    def show(self, path):
        self.image.show(path)

    def save(self, path, scale=1):
        new_size = [coord * scale for coord in self.image.size]
        self.image.resize(new_size).save(path, quality=95)
