'''1. BRING ME DATA.

INTRO:
This code trains a a neural network for steering prediction.
We train the weights of the network to minimize the mean squared error between
the steering output of the network and the command of the human driver.

ARCHITECTURE:
    1. NormLayer.
    2. ConvLayer: 2x2 stride, 5x5 kernel, 3 kernels.
    3. ConvLayer: 2x2 stride, 5x5 kernel, 24 kernels.
    4. ConvLayer: 2x2 stride, 5x5 kernel, 36 kernels.
    5. ConvLayer: 3x3 kernel, 48 kernels.
    6. ConvLayer: 3x3 kernel, 64 kernels.
    7. FlattenLayer.
    8. DenseLayer: 1164
    9. DenseLayer: 100
    10. DenseLayer: 50
    11. DenseLayer: 10
    12. DenseLayer: 1
'''

from __future__ import print_function
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.layers import Convolution2D
from keras.optimizers import SGD
from keras.utils import np_utils

batch_size = 32
nb_classes = 10
nb_epoch = 200
data_augmentation = True

# input image dimensions
# TODO: adjust to input video size.
img_rows, img_cols = 32, 32
# TODO: check for number of channels.
img_channels = 3

# the data, shuffled and split between train and test sets
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
print('X_train shape:', X_train.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)

model = Sequential()

# 2. ConvLayer: 2x2 stride, 5x5 kernel, 3 kernels.
model.add(Convolution2D(3, 5, 5,
                        border_mode='same',
                        subsample=(2, 2),
                        input_shape=X_train.shape[1:]))

# 3. ConvLayer: 2x2 stride, 5x5 kernel, 24 kernels.
model.add(Convolution2D(24, 5, 5,
                        border_mode='same',
                        subsample=(2, 2)))

# 4. ConvLayer: 2x2 stride, 5x5 kernel, 36 kernels.
model.add(Convolution2D(36, 5, 5,
                        border_mode='same',
                        subsample=(2, 2)))

# 5. ConvLayer: 3x3 kernel, 48 kernels, no stride.
model.add(Convolution2D(48, 3, 3,
                        border_mode='same'))

# 6. ConvLayer: 3x3 kernel, 64 kernels, no stride.
model.add(Convolution2D(64, 3, 3,
                        border_mode='same'))

# 7. FlattenLayer.
model.add(Flatten())

# 8. DenseLayer: 1164
model.add(Dense(1164))

# 9. DenseLayer: 100
model.add(Dense(100))

# 10. DenseLayer: 50
model.add(Dense(50))

# 11. DenseLayer: 10.Provisionally using 10
model.add(Dense(10))

# Layer output. For real data change to linear activation
# model.add(Activation('linear'))
model.add(Activation('softmax'))

# let's train the model using SGD + momentum (how original).
# TODO: check for values.
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='mean_squared_error',
              optimizer=sgd,
              metrics=['accuracy'])

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# this will do preprocessing and realtime data augmentation
datagen = ImageDataGenerator(
    featurewise_center=True,  # set input mean to 0 over the dataset
    samplewise_center=True,  # set each sample mean to 0
    featurewise_std_normalization=True,  # divide inputs by std of the dataset
    samplewise_std_normalization=True)  # divide each input by its std

datagen.fit(X_train)

# fit the model on the batches generated by datagen.flow()
model.fit_generator(datagen.flow(X_train, Y_train,
                    batch_size=batch_size),
                    samples_per_epoch=X_train.shape[0],
                    nb_epoch=nb_epoch,
                    validation_data=(X_test, Y_test))
