#-*- coding:utf-8 -*-

import  keras
from nlpmaster.imdb import data
#%%
(train_data, train_labels), (test_data, test_labels) = data.loadLocalImdb(num_words=10000)

imdb = keras.datasets.imdb
path_imdb = 'F://git/my_practice/tensorflow/imdb.npz'
(train_x, train_y), (test_x, test_y) = keras.datasets.imdb.load_data\
    (path=path_imdb, num_words=10000)
print('train enties:{}, labels: {}'.format(len(train_x), len(train_y)))
#%%

