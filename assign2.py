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



def imageLabelling(imageArr):
    labelName = imageArr.split('')
    if(labelName=="Happy"):
        return

def training_data():#currently only FEI database
    Happy_array = list()
    Sad_array = list()

    for filename in os.listdir('images/FEISorted/Happy'):
        data = matplotlib.image.imread('images/FEISorted/Happy/'+filename)
        data = data.reshape(100,100,3)
        Happy_array.append(data)

    for filename in os.listdir('images/FEISorted/Sad'):
        data = matplotlib.image.imread('images/FEISorted/Sad/'+filename)
        Sad_array.append(data)

    print(Happy_array[4].shape)
#def SetLabel():




training_data()
