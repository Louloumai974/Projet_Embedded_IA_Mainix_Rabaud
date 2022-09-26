import sys, os, array, time
import numpy as np
import matplotlib.pyplot as plt
import IPython

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers, models


os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="1"


def load_esca_data(path):
    with np.load(path) as f:
        x_train, y_train = f['x_train'], f['y_train']
        x_test, y_test = f['x_test'], f['y_test']
        return (x_train, y_train) , (x_test,y_test)

class dataset:
    def _init_(self):
            with np.load('mnist.npz') as f:
                self.x_train, self.y_train = f['x_train'], f['y_train']
                self.x_test, self.y_test = f['x_test'], f['y_test']

test