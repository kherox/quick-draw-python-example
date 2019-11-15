#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:40:11 2019

@author: kherox
"""

import tensorflow as tf
import numpy as np
import pandas as pd
import os

tf.__version__

from IPython import display

DATASET_PATH = "/home/kherox/datasets/quickdraw/"
filenames = []
files = os.listdir(os.path.join(DATASET_PATH , "training"))

print()

for file in files :
    filenames.append(os.path.join(DATASET_PATH,"training",file))




datasets = tf.data.TFRecordDataset(filenames)
targets  = tf.data.TFRecordDataset(DATASET_PATH+"training.tfrecord.classes")
 
feature_description = {
        "class_index" : tf.io.FixedLenFeature([])
}

i = 0
for data in datasets:
    example = tf.train.Example()
    example.ParseFromString(data.numpy())
    print((example))
    break
