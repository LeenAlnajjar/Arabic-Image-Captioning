# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 01:42:42 2023

@author: hp
"""


import os
import random
import shutil
#%%
# Define the source and destination directories
src_dir = 'C:\\Users\\hp\\Desktop\\Personal files\\HTU\\python\\Machine learning\\Project\\Arabic-Image-Captioning-master\\data\\Flicker8k_Dataset'
train_dir = 'C:\\Users\\hp\\Desktop\\Personal files\\HTU\\python\\Machine learning\\Project\\Arabic-Image-Captioning-master\\data\\Flickr8k_train'
test_dir = 'C:\\Users\\hp\\Desktop\\Personal files\\HTU\\python\\Machine learning\\Project\\Arabic-Image-Captioning-master\\data\\Flickr8k_test'
#%%
# Get a list of all image filenames
filenames = [f for f in os.listdir(src_dir) if f.endswith('.jpg') or f.endswith('.png')]

# Shuffle the filenames
random.shuffle(filenames)

# Define the number of images for the test set
num_test_images = int(len(filenames) * 0.2)

# Get the test image filenames
test_filenames = filenames[:num_test_images]

# Get the train image filenames
train_filenames = filenames[num_test_images:]

# Loop over the train images
for filename in train_filenames:
    # Create the full path to the file
    src_path = os.path.join(src_dir, filename)
    # Create the full path to the destination file
    dest_path = os.path.join(train_dir, filename)
    # Move the file to the train directory
    shutil.move(src_path, dest_path)

# Loop over the test images
for filename in test_filenames:
    # Create the full path to the file
    src_path = os.path.join(src_dir, filename)
    # Create the full path to the destination file
    dest_path = os.path.join(test_dir, filename)
    # Move the file to the test directory
    shutil.move(src_path, dest_path)
