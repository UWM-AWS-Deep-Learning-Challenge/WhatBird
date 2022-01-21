# following this guide https://www.tensorflow.org/guide/keras/transfer_learning

import numpy as np
import tensorflow as tf
from tensorflow import keras

# instantiate a base model and load pre-trained weights into it
base_model = keras.applications.Xception(
    weights='imagenet',             # loading weights pre-trained on ImageNet
    input_shape=(150, 150, 3),
    include_top=False,              # Do not include the ImageNet classifer at the top
)

# freeze all layers in the base model by settings trainable = False
base_model.trainable = False

# create a new model on top of the output of one (or several) layers from the base model
inputs = keras.Input(
    shape=(150, 150, 3)
)

# - we make sure that the base_model is running in inference mode here, 
# - by passing training=False.  This is important for fine-tuning.

x = base_model(
    inputs, 
    training=False
)

# - convert features of shape base_model.output_shape[1:] to vectors
x = keras.layers.GlobalAveragePooling2D()(x)

# - a dense classifier with a single unit (binary classification)
outputs = keras.layers.Dense(1)(x)
model = keras.Model(inputs, outputs)

# load a new dataset
# TODO

# train your new model on your new dataset
model.compile(
    optimizer=keras.optimizers.Adam(),
    loss=keras.losses.BinaryCrossentropy(from_logits=True),
    metrics=[keras.metrics.BinaryAccuracy()]
)

model.fit(new_dataset, epochs=20, callbacks=..., validation_data=...)