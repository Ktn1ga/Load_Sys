import numpy as np
import pickle


import tensorflow as tf


from sklearn.metrics import mean_squared_error as MSE




def ann_168(data):
    data= data[:,4:]
    data=data.flatten()
    data = data[np.newaxis,:]
    with open('model/x_scaler.txt', 'rb') as file:
        x_scaler = pickle.load(file)
    data=x_scaler.transform(data)
    file_model = 'model/ann_168/model'
    model = tf.keras.models.load_model(file_model)
    pre_y = model.predict(data)
    with open('model/y_scaler.txt', 'rb') as file:
        y_scaler = pickle.load(file)
    pre_y = y_scaler.inverse_transform(pre_y)

    return pre_y

def lstm_168(data):
    data= data[:,4:]
    data=data.flatten()
    data = data[np.newaxis,:]
    with open('model/x_scaler.txt', 'rb') as file:
        x_scaler = pickle.load(file)
    data=x_scaler.transform(data)
    data = data.reshape(data.shape[0], 1, data.shape[1])
    file_model = 'model/lstm_168/model'
    model = tf.keras.models.load_model(file_model)
    pre_y = model.predict(data)
    with open('model/y_scaler.txt', 'rb') as file:
        y_scaler = pickle.load(file)
    pre_y = y_scaler.inverse_transform(pre_y)

    return pre_y

def gru_168(data):
    data= data[:,4:]
    data=data.flatten()
    data = data[np.newaxis,:]
    with open('model/x_scaler.txt', 'rb') as file:
        x_scaler = pickle.load(file)
    data=x_scaler.transform(data)
    data = data.reshape(data.shape[0], 1, data.shape[1])
    file_model = 'model/gru_168/model'
    model = tf.keras.models.load_model(file_model)
    pre_y = model.predict(data)
    with open('model/y_scaler.txt', 'rb') as file:
        y_scaler = pickle.load(file)
    pre_y = y_scaler.inverse_transform(pre_y)

    return pre_y



def k_ann(data):
    data= data[:,4:]
    c_mean = np.load('model/K_ANN/mean.npy')
    y=[]
    for day in data:
        MSElist = []
        for label in c_mean:
            MSElist.append(MSE(day,label))
        num = MSElist.index(min(MSElist))
        y.append(num)
    y=np.array(y)
    y=y[:,np.newaxis]
    data = np.hstack((data,y))

    p1 = data[:, :-1].flatten()
    p2 = data[:, -1]
    data = np.hstack((p1, p2))

    data = data[np.newaxis,:]

    with open('model/x_k_scaler.txt', 'rb') as file:
        x_scaler = pickle.load(file)
    data=x_scaler.transform(data)

    file_model = 'model/K_ANN/model'
    model = tf.keras.models.load_model(file_model)
    pre_y = model.predict(data)
    with open('model/y_k_scaler.txt', 'rb') as file:
        y_scaler = pickle.load(file)
    pre_y = y_scaler.inverse_transform(pre_y)

    return pre_y

def k_tcn(data):
    data= data[:,4:]
    c_mean = np.load('model/K_ANN/mean.npy')
    y=[]
    for day in data:
        MSElist = []
        for label in c_mean:
            MSElist.append(MSE(day,label))
        num = MSElist.index(min(MSElist))
        y.append(num)
    y=np.array(y)
    y=y[:,np.newaxis]
    data = np.hstack((data,y))

    p1 = data[:, :-1].flatten()
    p2 = data[:, -1]
    data = np.hstack((p1, p2))

    print('hi',data.shape)
    data = data[np.newaxis,:]

    with open('model/x_k_scaler.txt', 'rb') as file:
        x_scaler = pickle.load(file)
    data=x_scaler.transform(data)
    data = data.reshape(data.shape[0], 1, data.shape[1])
    file_model = 'model/K_TCN/model'
    model = tf.keras.models.load_model(file_model)
    pre_y = model.predict(data)
    with open('model/y_k_scaler.txt', 'rb') as file:
        y_scaler = pickle.load(file)
    pre_y = y_scaler.inverse_transform(pre_y)

    return pre_y