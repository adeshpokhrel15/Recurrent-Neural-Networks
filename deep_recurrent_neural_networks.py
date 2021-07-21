# -*- coding: utf-8 -*-
"""Deep Recurrent Neural Networks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VoZCWUSCy2rYnG-Tpa1oy-bmjFmOuumT
"""

# Commented out IPython magic to ensure Python compatibility.
#Importing the library
import tensorflow as tf
from d2l import tensorflow as d2l
import math
# %matplotlib inline

#!pip install d2l==0.16.6 #==> if d2l is not working then setup the environment '''

batch_size, num_steps = 32, 35
train_iter, vocab = d2l.load_data_time_machine(batch_size, num_steps)

vocab_size, num_hiddens, num_layers = len(vocab), 256, 2
num_inputs = vocab_size
device_name = d2l.try_gpu()._device_name
strategy = tf.distribute.OneDeviceStrategy(device_name)
rnn_cells = [tf.keras.layers.LSTMCell(num_hiddens) for _ in range(num_layers)]
stacked_lstm = tf.keras.layers.StackedRNNCells(rnn_cells)
lstm_layer = tf.keras.layers.RNN(stacked_lstm, time_major=True,
                                 return_sequences=True, return_state=True)
with strategy.scope():
    model = d2l.RNNModel(lstm_layer, len(vocab))

#Training & Predictions
num_epochs, lr = 500, 2
d2l.train_ch8(model, train_iter, vocab, lr, num_epochs, strategy)

