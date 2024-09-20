import tensorflow as tf
from tensorflow import keras
import joblib

# Guardar el modelo en caché

# Definir los datos
palabras = ['apagar la computadora','apaga la computadora','','apague la computadora','', 'ip', 'ping', 'tasklist','reiniciar','cerrar sesión','cierre sesión','mover']
oraciones = ['shutdown /s /t 0', 'ipconfig', 'ping 1.0.0.1', 'tasklist','shutdown /r /t 0','shutdown /l']

# Preprocesar los datos
tokenizer = keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(palabras)
palabras_seq = tokenizer.texts_to_sequences(palabras)
max_len = max([len(seq) for seq in palabras_seq])
palabras_seq = keras.preprocessing.sequence.pad_sequences(palabras_seq, maxlen=max_len)

cerebro=keras.layers.Dense(16, activation='relu')

model = keras.Sequential([
    keras.layers.Embedding(len(tokenizer.word_index) + 1, 16, input_length=max_len),
    keras.layers.GlobalAveragePooling1D(),
    cerebro,
    keras.layers.Dense(len(oraciones), activation='softmax')
])

#model = joblib.load('model.joblib')
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


model.fit(palabras_seq, keras.utils.to_categorical(range(len(oraciones))), epochs=1)
#joblib.dump(model, 'model.joblib')