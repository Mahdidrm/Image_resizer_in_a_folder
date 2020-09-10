# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 15:49:37 2020

@author: deramgoz1
"""

import PIL
import os
import os.path
from PIL import Image

f = r'U:/Emotion/face-extracker/CKFace48/Surprise'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((48,48))
    img.save(f_img)