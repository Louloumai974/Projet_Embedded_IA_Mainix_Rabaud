from PIL import Image
import os, sys
import cv2
import numpy as np


# Path to image directory
path1 = "./processed_esca_dataset/test/esca"
dirs = os.listdir( path1 )
dirs.sort()
x_train=[]

def load_dataset():
    # Append images to a list
    for item in dirs:
        if os.path.isfile(path1+item):
            im = Image.open(path1+item).convert("RGB")
            im = np.array(im)
            x_train.append(im)

if __name__ == "__main__":
    
    load_dataset()
    
    # Convert and save the list of images in '.npy' format
    imgset=np.array(x_train)
    np.save("x_test_esca.npy",imgset)


# Path to image directory
path = "./processed_esca_dataset/test/healthy"
dirs = os.listdir( path )
dirs.sort()
x_train=[]

def load_dataset():
    # Append images to a list
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item).convert("RGB")
            im = np.array(im)
            x_train.append(im)

if __name__ == "__main__":
    
    load_dataset()
    
    # Convert and save the list of images in '.npy' format
    imgset=np.array(x_train)
    np.save("x_test_healthy.npy",imgset)


esca = np.load('x_test_esca.npy')
healthy = np.load('x_test_healthy.npy')
x_test = []

x_test = np.append(esca,healthy)

np.save('x_test.npy',x_test)

y_test = np.full(len(esca),'1')
y_test = np.append(y_test,np.full(len(healthy),'2')) 
np.save('y_test.npy',y_test) 

