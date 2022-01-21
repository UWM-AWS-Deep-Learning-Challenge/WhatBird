import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from tensorflow.keras.optimizers import Adam
import numpy as np
import matplotlib.pyplot as plt
import os

# creating models dir
if not os.path.isdir('models'):
    os.mkdir('models')

# checking version
print(f'tf version: {tf.__version__}')
print(f'using gpu? -> {tf.test.is_gpu_available()}')
