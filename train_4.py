import csv
import cv2
import numpy as np
import tensorflow as tf
from PIL import Image

lines = []

images = []
measurements = []
correction = [0, 0.2, -0.2]

with open("./train_data/track_2_error_2/driving_log.csv") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
            lines.append(line)

for line in lines:
    measurement = float(line[3])
    if(measurement > -0.05 and measurement < -0.05 and random.random() > 0.4):
        continue
    for i in range(3):
        source_path = line[i]
        filename = source_path.split('\\')[-1]
        current_path = './train_data/track_2_error_2/IMG/' + filename
        image = Image.open(current_path)
        image = np.array(image.convert('YCbCr'))
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
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

from keras.models import Sequential, load_model
from keras.layers import Flatten, Dense, Lambda, Cropping2D, Dropout
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D


model = load_model('model.h5')

model.compile(loss='mse', optimizer='adam')
model.fit(X_train, y_train, validation_split=0.2, shuffle=True, nb_epoch=3)

model.save('model.h5')
exit()

