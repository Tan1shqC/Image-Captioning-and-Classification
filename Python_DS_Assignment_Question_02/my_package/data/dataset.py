    #Imports
import jsonlines
from PIL import Image
import os
import numpy as np

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms=None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self._file = annotation_file
        self._transforms = transforms

     

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        with jsonlines.open(self._file) as reader:
            data = list(reader)
        return len(data)
        

    
    def __getann__(self, idx):
        '''
            return the data items for the index idx as an object
        '''
        with jsonlines.open(self._file) as reader:
            data = list(reader)
        return data[idx]
        

    def __transformitem__(self, path):
        '''
            return transformed PIL Image object for the image in the given path
        '''
        image =  Image.open(path)
        for transform in self._transforms:
            image = transform(image)
        return image