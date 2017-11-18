import csv
import cv2
import numpy as np
import tensorflow as tf
from PIL import Image
import random

## Prepare the training set, the train set is to drive forward
lines = []

images = []
measurements = []
correction = [0, 0.2, -0.2]

with open("./train_data/track_2_normal_2/driving_log.csv") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
            lines.append(line)

for line in lines:
    measurement = float(line[3])
	# reduce the number of forward driving in train dataset
    if(measurement > -0.05 and measurement < 0.05 and random.random() > 0.4):
        continue
    for i in range(3):
        source_path = line[i]
        filename = source_path.split('\\')[-1]
        current_path = './train_data/track_2_normal_2/IMG/' + filename
        image = Image.open(current_path)
        image = np.array(image.convert('YCbCr'))
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
        images.append(image)
        measurements.append(measurement + correction[i])

lines = []
with open("./train_data/track_1_normal/driving_log.csv") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
            lines.append(line)

for line in lines:
    measurement = float(line[3])
	# reduce the number of forward driving in train dataset
    if(measurement > -0.05 and measurement < 0.05 and random.random() > 0.3):
        continue
    for i in range(3):
        source_path = line[i]
        filename = source_path.split('\\')[-1]
        current_path = './train_data/track_1_normal/IMG/' + filename
        image = Image.open(current_path)
        image = np.array(image.convert('YCbCr'))
        images.append(image)
        measurements.append(measurement + correction[i])


augmented_images, augmented_measurements = [], []
for image, measurement in zip(images, measurements):
    augmented_images.append(image)
    augmented_measurements.append(measurement)
    augmented_images.append(cv2.flip(image, 1))
    augmented_measurements.append(measurement*-1.0)

X_train = np.array(augmented_images)
y_train = np.array(augmented_measurements)

## Prepare the test set, the test set is to drive in another direction
lines = []

images = []
measurements = []

with open("./test_data/track_1/driving_log.csv") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
            lines.append(line)

for line in lines:
    measurement = float(line[3])
    source_path = line[0]
    filename = source_path.split('\\')[-1]
    current_path = './test_data/track_1/IMG/' + filename
    image = Image.open(current_path)
    image = np.array(image.convert('YCbCr'))
    images.append(image)
    measurements.append(measurement)

lines = []
with open("./test_data/track_2/driving_log.csv") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
            lines.append(line)

for line in lines:
    measurement = float(line[3])
    source_path = line[0]
    filename = source_path.split('\\')[-1]
    current_path = './test_data/track_2/IMG/' + filename
    image = Image.open(current_path)
    image = np.array(image.convert('YCbCr'))
    images.append(image)
    measurements.append(measurement)

X_test = np.array(images)
y_test = np.array(measurements)

from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Cropping2D, Dropout
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D

dropout_rate=0.0

model = Sequential()
model.add(Lambda(lambda x: x /255.0 - 0.5, input_shape=(160,320,3)))
# input 3@160x320
model.add(Cropping2D(cropping=((70,25), (0,0))))
# input 3@65x320
model.add(Convolution2D(24, 5, 5, activation="relu", subsample=(2,2)))
# input 24@31x158
model.add(Convolution2D(36, 5, 5, activation="relu", subsample=(2,2)))
# input 36@14x77
model.add(Convolution2D(48, 5, 5, activation="relu", subsample=(2,2)))
# input 48@5x37
model.add(Convolution2D(64, 3, 3, activation="relu"))
# input 64@3x35
model.add(Convolution2D(64, 3, 3, activation="relu"))
# input 64@1x32
model.add(Flatten())
model.add(Dropout(dropout_rate))
model.add(Dense(1164, activation="relu"))
model.add(Dropout(dropout_rate))
model.add(Dense(100, activation="relu"))
model.add(Dropout(dropout_rate))
model.add(Dense(50, activation="relu"))
model.add(Dropout(dropout_rate))
model.add(Dense(10, activation="relu"))
model.add(Dropout(dropout_rate))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
model.fit(X_train, y_train, validation_split=0.2, shuffle=True, nb_epoch=5)

model.save('model.h5')

scores = model.evaluate(X_test, y_test, verbose=0)
print("Test score (dropout: %.1f) : %.3f" % (dropout_rate, scores))

