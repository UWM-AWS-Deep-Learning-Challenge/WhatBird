from re import I
from importlib_metadata import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping
import numpy as np
import pandas as pd

BATCH_SIZE = 8

def prepare_model():
    model = Sequential()
    model.add(
        Conv2D(
            32, 
            kernel_size=(3,3),
            activation='relu',
            # input_shape=(100,100,3)
            input_shape=(224,244,3)
        )
    )
    model.add(
        MaxPooling2D(
            pool_size=(2,2)
        )
    )
    model.add(Flatten())
    model.add(Dense(16, activation='relu'))
    model.add(Dense(325, activation='sigmoid'))
    model.compile(
        loss="binary_crossentropy",
        optimizer="adam",
        metrics=['accuracy']
    )

    return model


# read in CSVs
bird_classes = pd.read_csv('../data/class_dict.csv')
bird_species = pd.read_csv('../data/birds.csv')

# pre-processing
src_path_train = "../data/train"
src_path_test = "../data/test/"
src_path_valid = "../data/valid"

# impute data
train_data = ImageDataGenerator(
    preprocessing_function = preprocess_input,
    rotation_range=20,
    horizontal_flip=True
)

train_generator = train_data.flow_from_directory(
    src_path_train,
    batch_size=BATCH_SIZE,
    target_size=(224,224),
    class_mode='categorical'
)

valid_data = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=20,
    horizontal_flip=True
)

validation_generator = valid_data.flow_from_directory(
    src_path_valid, 
    batch_size=BATCH_SIZE,
    target_size=(224,224),
    class_mode='categorical'
)

# building a VGG16 model 

vgg_model = VGG16(
    weights='imagenet',
    include_top=False,
    input_shape=(224,224,3)
)
vgg_model.trainable = False

layer0 = tf.keras.layers.Flatten(name='flatten')(vgg_model.output)
layer1 = tf.keras.layers.Dense(4096, activation='relu',name='fc1')(layer0)
layer2 = tf.keras.layers.Dense(4096, activation='relu',name='fc2')(layer1)
out_layer = tf.keras.layers.Dense(325, activation='softmax')(layer2)
vgg_model = tf.keras.Model(vgg_model.input, out_layer)

# setup the optimizaers, callbacks
opt = tf.keras.optimizers.Adam(learning_rate=0.0001)
vgg_model.compile(optimizer=opt, loss="categorical_crossentropy", metrics=['accuracy'])

checkpoint = ModelCheckpoint("model_1060_1.h5", monitor='val_accuracy', verbose=1, save_best_only=True, save_weights_only=False, mode='auto', period=1)
early = EarlyStopping(monitor='val_accuracy', min_delta=0, patience=20, verbose=1, mode='auto')
callbacks = [checkpoint, early]

# create a species class
species = np.array(bird_classes['class'])

# wamrup the model
history = vgg_model.fit(
    train_generator,
    epochs = 1,
    verbose = 1,
    validation_data = validation_generator,
    callbacks = callbacks
)


# train the model for real now
opt = tf.keras.optimizers.Adam(learning_rate=0.00005)
vgg_model.trainable = True
vgg_model.compile(optimizer=opt, loss="categorical_crossentropy", metrics=['accuracy'])

history = vgg_model.fit(
      train_generator, 
      epochs=1,
      verbose=1,
      validation_data = validation_generator,
      callbacks=callbacks)

# try to decrease learning rate again 
opt = tf.keras.optimizers.Adam(learning_rate=0.00001)
vgg_model.compile(optimizer=opt, loss="categorical_crossentropy", metrics=['accuracy'])
callbacks = [early, checkpoint]

history = vgg_model.fit(
      train_generator, 
      epochs=1,
      verbose=1,
      validation_data = validation_generator,
      callbacks=callbacks)

test = ImageDataGenerator(preprocessing_function=preprocess_input)
test_generator = test.flow_from_directory(
        '../data/test',
        target_size=(224, 224),
        batch_size=BATCH_SIZE,
        class_mode='categorical')

vgg_model.evaluate(test_generator,use_multiprocessing=True,workers=10)



