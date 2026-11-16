import pickle
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import Model,load_model
from keras import optimizers


from keras import metrics, regularizers, backend
from keras.layers import Input, Dense
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import Conv1D,MaxPooling1D, Flatten,AveragePooling1D,Reshape,concatenate
from keras.layers import Conv2D, GlobalMaxPooling1D ,MaxPooling2D
from tensorflow.keras.layers import Concatenate
from keras.models import load_model
from tensorflow.keras.layers import Input,GRU, Conv2D, Dense,Add,Subtract, Dropout,Multiply, BatchNormalization, Activation,Lambda, Flatten, Reshape, MaxPooling2D, concatenate
from keras.optimizers import Adam
import os

import matplotlib.pyplot as plt

from tensorflow.keras.layers import Input,Activation, Conv1D,concatenate, MaxPooling1D, Dropout, GRU, Flatten, Dense, Concatenate, Lambda,Multiply, Add, Subtract, Reshape
from tensorflow.keras.models import Model
import tensorflow as tf
import sys
sys.stdout.reconfigure(encoding='utf-8')

def cal1(x_degrees):
    x_tensor = tf.convert_to_tensor(x_degrees, dtype=tf.float32)
    w = tf.concat([x_tensor * (i + 1) for i in range(128)], axis=-1)
    y = tf.cos(w)
    return tf.expand_dims(y, axis=-1)

def cal2(x_degrees):
    x_tensor = tf.convert_to_tensor(x_degrees, dtype=tf.float32)
    w = tf.concat([x_tensor * (i + 1) for i in range(128)], axis=-1)
    y = tf.sin(w)
    return tf.expand_dims(y, axis=-1)



def CNN(input_shape=(128, 2), input_shape2=(128, 1), classes=11):

    # Define input layers
    dr = 0.5 # dropout rate (%)
    input = Input(shape=input_shape + (1,), name='input1')  # Shape will be (None, 2, 128, 1)
    input1 = Input(input_shape2, name='input2')
    input2 = Input(input_shape2, name='input3')

    x1 = Flatten()(input)
    x1= Dense(80, name='fc1')(x1)
    x1 = Activation('relu')(x1)

    x1= Dense(1, name='fc4')(x1)
    x1 = Activation('linear')(x1)


    cos1= Lambda(cal1)(x1)
    sin1 = Lambda(cal2)(x1)
    x11 = Multiply()([input1, cos1])
    x12 = Multiply()([input2, sin1])
    x21 = Multiply()([input2, cos1])
    x22 = Multiply()([input1, sin1])
    y1 = Add()([x11,x12])
    y2 = Subtract()([x21,x22])
    y1 = Reshape(target_shape=(128, 1), name='reshape1')(y1)
    y2 = Reshape(target_shape=(128, 1), name='reshape2')(y2)
    x11 = concatenate([y1, y2])
    x3 = Reshape(target_shape=((128, 2, 1)), name='reshape3')(x11)

    # spatial feature
    x3 = Conv2D(75, (8,2), padding='valid', activation="relu", name="conv1_1", kernel_initializer='glorot_uniform')(
        x3)
    x3 = Conv2D(25, (5,1), padding='valid', activation="relu", name="conv1_2", kernel_initializer='glorot_uniform')(
        x3)
    # temporal feature
    x4 = Reshape(target_shape=((117,25)), name='reshape4')(x3)
    x4= GRU(units=128)(x4)

    x = Dense(classes, activation='softmax', name='softmax')(x4)


    model = Model(inputs = [input,input1,input2], outputs=x)



    return model





model=CNN()

model.load_weights('C:/Users/asus/Downloads/CNN2_80ff(2).keras')


file_path = 'C:/Users/asus/Downloads/mydata12.pkl'
if os.path.getsize(file_path) > 0:
    with open(file_path, 'rb') as f:
        loaded_array1, loaded_array2, loaded_array3 = pickle.load(f)
    print("Arrays loaded successfully.")
else:
    print("The file is empty.")
test_Y_hat =100*model.predict([loaded_array1,loaded_array2,loaded_array3],batch_size=1)
mean_array = np.mean(test_Y_hat, axis=0).reshape(1, 11)

print("Mean array :")
print(mean_array)
modtype=['8PSK','AM-DSB','AM-SSB','BPSK','CPFSK','GFSK','4-PAM','16-QAM','64-QAM','QPSK','WBFM']
y=np.argmax(mean_array)
m=modtype[int(y)]
print("modulation:",m)

