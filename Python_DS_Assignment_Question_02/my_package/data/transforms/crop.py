#Imports
from PIL import Image
import random
from random import randrange
class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self._height = shape[0]
        self._width = shape[1]
        self._crop_type = crop_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        
        left = (image.size[0]/2) - (self._width/2)
        top = (image.size[1]/2) + (self._height/2)
        right = (image.size[0]/2) + (self._width/2)
        bottom = (image.size[1]/2) - (self._height/2)
        crop_image = image.crop((left, top, right, bottom))
        return crop_image

class RandomCrop(CropImage):
    def __call__(self, image):
        left = randrange(0, image.size[0] - self._width)
        top = randrange(self._height, image.size[1])
        right = left + self._width
        bottom = top - self._height
        crop_image = image.crop((left, top, right, bottom))
        return crop_image