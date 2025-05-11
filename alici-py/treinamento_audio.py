import tensorflow as tf
import numpy as np
import librosa
import os

# Carregar o modelo de áudio
model_audio = tf.keras.models.load_model('audio_model.h5')

def preprocess_audio(file_path):
    """Preprocessamento do áudio para o modelo"""
    y, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc, axis=1)

def predict_audio(file_path):
    """Faz a predição de áudio"""
    features = preprocess_audio(file_path)
    features = features.reshape(1, -1)
    prediction = model_audio.predict(features)
    return prediction

# Testar com um arquivo de áudio
file_path = 'path_to_audio.wav'
prediction = predict_audio(file_path)
print(f'Predição de áudio: {prediction}')
