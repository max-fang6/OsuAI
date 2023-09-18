import keras

# The model has been designed thus far but the data has not been completely processed yet

lstm_model = keras.Sequential()


lstm_model.add(keras.Input(shape=(2,4)))
lstm_model.add(keras.layers.LSTM(64, activation='relu'))

##last layer
lstm_model.add(keras.layers.Dense(1, 'relu'))
print(lstm_model.summary())