from PIL import Image


class ImageProcesser:
    def __init__(self, name, image_array):
        self.image = Image.fromarray(image_array)
        self.name = name

    def show(self):
        self.image.show()

    def save(self):
        self.image.save(self.name + ".png")