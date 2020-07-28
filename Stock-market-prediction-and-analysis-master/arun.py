
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout
import os

#def create_dataset():
#    x = []
#    y = []
#    for i in range(50, df.shape[0]):
#        x.append(df[i-50:i, 0])
#        y.append(df[i, 0])
#    x = np.array(x)
#    y = np.array(y)
#    return x,y

#x_train, y_train = create_dataset()
#x_train[:1]

#x_test, y_test = create_dataset()
#x_test[:1]
def load():
    model = load_model('arun.h5')

    df = pd.read_csv('Arun_Valley.csv')
    df.head()
    

    df = df['Open'].values
    df = df.reshape(-1, 1)
    print(df.shape)
    df[:5]
   

    dataset_train = np.array(df[:int(df.shape[0]*0.8)])
    dataset_test = np.array(df[int(df.shape[0]*0.8)-50:])
    print(dataset_train.shape)
    print(dataset_test.shape)

    scaler = MinMaxScaler(feature_range=(0,1))
    dataset_train = scaler.fit_transform(dataset_train)
    dataset_train[:5]

    dataset_test = scaler.transform(dataset_test)
    dataset_test[:5]

    def create_dataset(df):
        x = []
        y = []
        for i in range(60, df.shape[0]):
            x.append(df[i-60:i, 0])
            y.append(df[i, 0])
        x = np.array(x)
        y = np.array(y)
        return x,y

    x_train, y_train = create_dataset(dataset_train)
    x_train[:1]

    x_test, y_test = create_dataset(dataset_test)
    x_test[:1]

    # Reshape features for LSTM Layer
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

    model = Sequential()
    model.add(LSTM(units=96, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=96, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=96, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=96))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))

    model.compile(loss='mean_squared_error', optimizer='adam')

    model = load_model('arun.h5')

    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)

    fig, ax = plt.subplots(figsize=(8,4))
    plt.plot(df, color='red',  label="True Price")
    ax.plot(range(len(y_train)+50,len(y_train)+50+len(predictions)),predictions, color='blue', label='Predicted Testing Price')
    plt.legend()
    plt.xlabel("Days")
    plt.ylabel("Stock Price")
    plt.title("Arun Valley")
    plt.show()

    #y_test_scaled = scaler.inverse_transform(y_test.reshape(-1, 1))

    #fig, ax = plt.subplots(figsize=(8,4))
    #ax.plot(y_test_scaled, color='red', label='True Testing Price')
    #plt.plot(predictions, color='blue', label='Predicted Testing Price')
    #plt.legend()
    #plt.show()


