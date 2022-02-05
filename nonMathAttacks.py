import random
import numpy as np

from PIL import ImageFilter, ImageChops, Image, ImageDraw, ImageOps
from skimage.util import random_noise

class NonMathAttacks():
    currentSeed = None

    def __init__(self, seed=None):
        if seed:
            self.seed(seed)

    def seed(self, seed):
        random.seed(seed)
        self.currentSeed = seed

    def gaussianBlur(self, image):
        # Applying the Gaussian Blur filter
        atkImage = image.filter(ImageFilter.GaussianBlur(radius=1.5))
        return atkImage

    def gaussianNoise(self, image):
        # convert PIL Image to ndarray
        image_array = np.asarray(image)

        # Noise
        atkImage = random_noise(
            image_array, mode='gaussian', seed=self.currentSeed)
        atkImage = (255 * atkImage).astype(np.uint8)

        return Image.fromarray(atkImage)

    def boxBlur(self, image):
        atkImage = image.filter(ImageFilter.BoxBlur(radius=1))
        return atkImage

    def sharpen(self, image):
        atkImage = image.filter(ImageFilter.SHARPEN)
        return atkImage

    def invertColor(self, image):
        atkImage = ImageChops.invert(image)
        return atkImage

    def greyscale(self, image):
        atkImage = ImageOps.grayscale(image).convert("RGB")
        return atkImage

    def splitMergeRGB(self, image):
        red, green, blue = image.split()
        atkImage = Image.merge("RGB", (green, red, blue))
        return atkImage

    def randomBlackBox(self, image):
        size = 50
        x = random.randint(50, 250-size)
        y = random.randint(50, 250-size)

        img_draw = ImageDraw.Draw(image)
        img_draw.rectangle([(x, y), (x+size, y+size)],
                        outline='black', fill='black')
        return image

    def saltAndPepper(self, image):
        # Amount of noise
        amount = 0.1
        atkImage = ImageOps.grayscale(image)
        atkImage = np.copy(np.array(atkImage))

        # ADD SALT
        nbSalt = np.ceil(amount * atkImage.size * 0.5)
        coords = [np.random.randint(0, i - 1, int(nbSalt))
                for i in atkImage.shape]
        atkImage[tuple(coords)] = 1

        # ADD PEPPER
        nbPepper = np.ceil(amount * atkImage.size * 0.5)
        coords = [np.random.randint(0, i - 1, int(nbPepper))
                for i in atkImage.shape]
        atkImage[tuple(coords)] = 0

        return Image.fromarray(atkImage).convert("RGB")
