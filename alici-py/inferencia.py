from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

# Lista das classes do CIFAR-100, para mapeamento dos índices de volta ao nome
classes = [
    'apple', 'aquarium_fish', 'baby', 'bear', 'beaver', 'bed', 'bee', 'beetle', 'bicycle', 'bottle',
    'bowl', 'boy', 'bridge', 'bus', 'butterfly', 'cabbage', 'camel', 'can', 'castle', 'caterpillar',
    'cattle', 'chair', 'chimpanzee', 'clock', 'cloud', 'cockroach', 'couch', 'crab', 'crocodile',
    'cup', 'dinosaur', 'dolphin', 'elephant', 'flatfish', 'forest', 'fox', 'girl', 'hamster',
    'house', 'kangaroo', 'keyboard', 'lamp', 'lawn_mower', 'leopard', 'lion', 'lizard', 'lobster',
    'man', 'maple_tree', 'motorcycle', 'mountain', 'mouse', 'mushroom', 'oak_tree', 'orange',
    'orchid', 'otter', 'palm_tree', 'pear', 'pickup_truck', 'pine_tree', 'plain', 'plate', 'poppy',
    'porcupine', 'possum', 'rabbit', 'raccoon', 'ray', 'road', 'rocket', 'rose', 'sea', 'seal',
    'shark', 'shrew', 'skunk', 'skyscraper', 'snail', 'snake', 'spider', 'squirrel', 'streetcar',
    'sunflower', 'sweet_pepper', 'table', 'tank', 'telephone', 'television', 'tiger', 'tractor',
    'train', 'trout', 'tulip', 'turtle', 'wardrobe', 'whale', 'willow_tree', 'wolf', 'woman',
    'worm'
]

# Carregar modelo salvo
modelo = load_model("modelo_animais_cifar100.h5")

def preprocessar_imagem(caminho_imagem):
    img = Image.open(caminho_imagem).resize((32, 32))
    img = np.array(img) / 255.0
    return img.reshape(1, 32, 32, 3)

def classificar_imagem(caminho_imagem):
    img = preprocessar_imagem(caminho_imagem)
    predicoes = modelo.predict(img)
    indice_classe = np.argmax(predicoes)
    nome_classe = classes[indice_classe]
    confianca = predicoes[0][indice_classe]
    return nome_classe, confianca

# Teste rápido (rodar esse script diretamente)
if __name__ == "__main__":
    caminho = "exemplo.jpg"  # coloque aqui o caminho da imagem que quer testar
    classe, confianca = classificar_imagem(caminho)
    print(f"Classe prevista: {classe} com confiança {confianca:.2f}")
