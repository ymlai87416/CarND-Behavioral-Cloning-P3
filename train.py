import csv
import cv2
import numpy as np
import tensorflow as tf
from PIL import Image

lines = []

with open("./train_data/track_1_normal/driving_log.csv") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
            lines.append(line)

images = []
measurements = []
correction = [0, 0.2, -0.2]

for line in lines:
	measurement = float(line[3])
	if(measurement > -0.05 and measurement < -0.05 and random.random() > 0.3):
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
	#print('debug', image)
    augmented_images.append(image)
    augmented_measurements.append(measurement)
    augmented_images.append(cv2.flip(image, 1))
    augmented_measurements.append(measurement*-1.0)

X_train = np.array(augmented_images)
y_train = np.array(augmented_measurements)

#print('debug', X_train, y_train)

from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Cropping2D, Dropout
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D

dropout_rate=0.5

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
model.add(Dense(1164))
model.add(Dropout(dropout_rate))
model.add(Dense(100))
model.add(Dropout(dropout_rate))
model.add(Dense(50))
model.add(Dropout(dropout_rate))
model.add(Dense(10))
model.add(Dropout(dropout_rate))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
model.fit(X_train, y_train, validation_split=0.2, shuffle=True, nb_epoch=5)

model.save('model.h5')
exit()

