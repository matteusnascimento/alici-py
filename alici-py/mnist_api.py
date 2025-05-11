import tensorflow as tf

# Carregar o dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar
x_train, x_test = x_train / 255.0, x_test / 255.0

# Definir o modelo
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compilar
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Treinar
model.fit(x_train, y_train, epochs=5)

# Avaliar
model.evaluate(x_test, y_test)

def predict_image(image_array):
    image_array = image_array.reshape(1, 28, 28, 1)
    prediction = model.predict(image_array)
    predicted_label = np.argmax(prediction)  # Pega o índice do maior valor
    return predicted_label


# Salvar
model.save('mnist_model.h5')
print("Modelo salvo como mnist_model.h5")
