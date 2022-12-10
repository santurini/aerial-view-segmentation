import numpy as np 
import pandas as pd
from PIL import Image
from tqdm import tqdm
import os

IMAGE_PATH = input("Insert path to Images: ")
MASK_PATH = input("Insert path to Masks: ")
SAVE_PATH = input("Insert path to Saving Folder: ")

H = int(input("Insert desired Height: "))
W = int(input("Insert desired Width: "))
SHAPE = (W, H)

if not os.isdir(SAVE_PATH):
    os.mkdir(SAVE_PATH)
    os.mkdir(SAVE_PATH + 'original_images/')
    os.mkdir(SAVE_PATH + 'label_images_semantic/')
    
CLASSES = {
    0: {0, 6, 10, 11, 12, 13, 14, 21, 22, 23}, # --> 0: [155,38,182], 'obstacles'
    1: {5, 7}, # --> 1: [14,135,204], 'water'
    2: {2, 3, 8, 19, 20}, # --> 2: [124,252,0], 'nature'
    3: {15, 16, 17, 18}, # --> 3: [255,20,147], 'moving'
    4: {1, 4, 9} # --> 4: [169,169,169], 'landable'
}

palette = [
    [155,38,182],
    [14,135,204],
    [124,252,0],
    [255,20,147],
    [169,169,169]
]

def create_df():
    name = []
    mask = []
    for dirname, _, filenames in os.walk(IMAGE_PATH): # given a directory iterates over the files
        for filename in filenames:
            f = filename.split('.')[0]
            name.append(f)

    return pd.DataFrame({'id': name}, index = np.arange(0, len(name))).sort_values('id').reset_index(drop=True)

def relabel(img, CLASSES):
    factor = 0.1
    img = np.array(img)
    s = img.shape
    
    for i in range(len(CLASSES)):    
      img = np.array([i*factor if j in CLASSES[i] else j for j in img.flatten()]).reshape(s)

    return Image.fromarray((img/factor).astype('uint8'))

def processing(X, shape, CLASSES, palette):
    
    for idx in tqdm(range(len(X))):
    
        image = np.array(Image.open(IMAGE_PATH + X[idx] + '.jpg')) 
        mask = np.array(Image.open(MASK_PATH + X[idx] + '.png'))

        # resize images
        image = np.array(Image.fromarray(image).resize(shape, Image.LINEAR))
        mask = Image.fromarray(mask).resize(shape, Image.NEAREST) # so values won't change
        mask = relabel(mask, CLASSES).convert('P')

        # Color the masks
        pal = [value for color in palette for value in color]
        mask.putpalette(pal)

        # save images as png to avoid losses or changes in the values of the pixels
        Image.fromarray(image).save(SAVE_PATH + 'original_images/' + X[idx] + '.png')
        mask.save(SAVE_PATH + 'label_images_semantic/' + X[idx] + '.png')
        
X = create_df()['id'].values # image id
processing(X, SHAPE, CLASSES, palette)