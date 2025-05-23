import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from database import salvar_interacao

# Carrega e prepara dados
df = pd.read_csv("dados/perguntas_respostas.csv")
perguntas = df["pergunta"].astype(str)
respostas = df["resposta"].astype(str)

# Tokenização
tokenizer = Tokenizer(num_words=10000, oov_token="<OOV>")
tokenizer.fit_on_texts(perguntas)

seqs = tokenizer.texts_to_sequences(perguntas)
padded = pad_sequences(seqs, maxlen=20, padding='post')

# Codificação de saída
respostas_token = tokenizer.texts_to_sequences(respostas)
respostas_padded = pad_sequences(respostas_token, maxlen=20, padding='post')

X_train, X_test, y_train, y_test = train_test_split(padded, respostas_padded, test_size=0.2)

# Modelo simples
modelo = tf.keras.Sequential([
    tf.keras.layers.Embedding(10000, 64),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(20, activation='softmax')  # Saída simplificada
])

modelo.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Treinar
modelo.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Salvar modelo
modelo.save("modelos/modelo_texto.h5")

# Salvar no banco
for pergunta, resposta in zip(perguntas, respostas):
    salvar_interacao(pergunta, resposta)
