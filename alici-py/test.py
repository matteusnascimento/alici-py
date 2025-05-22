from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

model = Sequential()
model.add(Embedding(input_dim=10000, output_dim=64, input_length=100))  # texto com 100 tokens
model.add(LSTM(64))
model.add(Dense(10, activation='softmax'))  # 10 classes de saída (ajuste conforme necessário)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()
