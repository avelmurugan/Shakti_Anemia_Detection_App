#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 23:20:45 2023

@author: arjunvelmurugan
"""

import tensorflow as tf
from tensorflow.keras import layers, models

def create_cnn_model(input_shape):
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))  # Single output for blood hemoglobin level
    return model

input_shape = (3, 3, 3)  # Replace height and width with the dimensions of your images
model = create_cnn_model(input_shape)
model.compile(optimizer='adam', loss='mse', metrics=['mae'])  # Mean squared error loss and mean absolute error metrics

# Assuming X_train and y_train are your training images and labels
model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.1)
