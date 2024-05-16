# 1.

from __future__ import absolute_import, division, print_function, unicode_literals
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import numpy as np
import random
from keras.layers.convolutional import MaxPooling2D
from sklearn.metrics import mean_squared_error
import theano
from keras import optimizers
from tensorflow.keras import datasets, layers, models
from scipy.stats import pearsonr
from sklearn.model_selection import KFold
import glob
import matplotlib.pyplot as plt
import numpy as np
import tensorflow_probability as tfp
import time
data = pd.read_csv('/NAS/home/yychoi/research/capstone1/bio-ai-capstone/Training dataset.xlsx')

data.head()

# 2.

def one_hot_encoding(df, seq_column, expression):
    bases = ['A','C','G','T']
    base_dict = dict(zip(bases,range(4)))
    n = len(df)
    total_width = df[seq_column].str.len().max()+20
    X = np.zeros((n,1,4,total_width))
    seqs = df[seq_column].values
    for i in range(n):
        seq = seqs[i]
        for b in range(len(seq)):
            X[i,0,base_dict[seq[b]], b+10+100-len(seq)] = 1    
    X = X.astype(theano.config.floatX)
    return X, total_width

X, total_width = one_hot_encoding(data,'Promoter','Reads')


