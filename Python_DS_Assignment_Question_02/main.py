#Imports
from my_package.model import ImageCaptioningModel
from my_package.data import Dataset, Download
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import numpy as np
from PIL import Image


def experiment(annotation_file, captioner, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        captioner: The image captioner
        transforms: List of transformation classes
        outputs: Path of the output folder to store the images
    '''

    #Create the instances of the dataset, download
    dataset = Dataset(annotation_file, transforms)
    download = Download()


    #Print image names and their captions from annotation file using dataset object
    for i in  range (0, dataset.__len__() - 1):
        obj = dataset.__getann__(i)
        print('File Name : "')
        print(obj['file_name'])
        print('"\nCaptions : "')
        print(obj['captions'])
        print('"\n')


    #Download images to ./data/imgs/ folder using download object
    download = Download()
    for i in  range (0, dataset.__len__() - 1):
        obj = dataset.__getann__(i)

        download.__call__('data/imgs/'+obj['file_name'], obj['url'])


    #Transform the required image (roll number mod 10) and save it seperately
    img = dataset.__transformitem__('./data/imgs/0.jpg')
    img.save('./data/imgs/output/0.jpg')

    #Get the predictions from the captioner for the above saved transformed image
    path = 'data/imgs/output/0.jpg'
    captions = captioner(path, 3)
    print(captions)


def main():
    captioner = ImageCaptioningModel()
    experiment('data/annotations.jsonl', captioner, [], None) # Sample arguments to call experiment()
    experiment('data/annotations.jsonl', captioner, [FlipImage()], None)
    experiment('data/annotations.jsonl', captioner, [BlurImage(1)], None)
    experiment('data/annotations.jsonl', captioner, [RescaleImage(1280)], None)
    experiment('data/annotations.jsonl', captioner, [RescaleImage(320)], None)
    experiment('data/annotations.jsonl', captioner, [RotateImage(90)], None)
    experiment('data/annotations.jsonl', captioner, [RotateImage(-45)], None)



if __name__ == '__main__':
    main()
    # data/annotations.jsonl