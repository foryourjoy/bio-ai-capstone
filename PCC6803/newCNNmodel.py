from __future__ import absolute_import, division, print_function, unicode_literals
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
import numpy as np
import random
import itertools
import time
#import kFold
from sklearn.metrics import mean_squared_error
import theano
from keras import optimizers
from tensorflow.keras import datasets, layers, models
from scipy.stats import pearsonr
from sklearn.model_selection import KFold
from scipy.stats import pearsonr
from tqdm import tqdm
data = pd.read_csv('PCC6803 Promoter and reads 100bp.csv')