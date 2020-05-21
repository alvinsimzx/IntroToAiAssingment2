# -*- coding: utf-8 -*-
import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import os
import cv2
from PIL import Image

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import check_random_state


IMG_SIZE = 100


def imageLabelling(imageArr):
    imagepath = os.path.split(imageArr)
    labelName = str(imagepath[0]).split('/')[-1]
    if labelName == "Happy":
        return [1,0]
    elif labelName == "Sad":
        return [0,1]


def training_data():#currently only FEI database
    Happy_array = list()
    Sad_array = list()

    for filename in os.listdir('images/FEISorted/Happy'):
        print(imageLabelling('images/FEISorted/Happy/'+filename))
        data = matplotlib.image.imread('images/FEISorted/Happy/'+filename)
        Happy_array.append(data)

    for filename in os.listdir('images/FEISorted/Sad'):
        data = matplotlib.image.imread('images/FEISorted/Sad/'+filename)
        Sad_array.append(data)


#def SetLabel():




training_data()
