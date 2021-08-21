from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation_#
from tensorflow.python.keras.layers import Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K
from mtcnn import MTCNN 
import cv2

K.clear_session()

datos_entrenamiento = 'Dedos/Fotos/Entrenamiento'
datos_validacion = 'Dedos/Fotos/Validacion'

iteraciones = 20
altura, longitud = 200, 200
batch_size = 1
pasos = 300/1
pasos_validacion = 300/1
filtrosconv1 = 32
filtrosconv2 = 64
filtrosconv3 = 128
tam_filtro1 = (4, 4)
tam_filtro2 = (3, 3)
tam_filtro3 = (2, 2)
tam_pool = (2, 2)
clases = 5
lr = 0.0005

preprocesamiento_entre = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.3,
    zoom_range=0.3,
    horizontal_flip=True
)
preprocesamiento_vali = ImageDataGenerator(
    rescale = "1./255"
)
image_entreno = preprocesamiento_entre.flow_from_directory(
    datos_entrenamiento,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical',
)
imagen_validacion = preprocesamiento_vali.flow_from_directory(
    datos_validacion,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical'
)
cnn = Sequential()

cnn.add(Convolution2D(filtrosconv1, tam_filtro1, padding = 'same'), input_shape=(altura, longitud, 3), activation = 'relu')
cnn.add(MaxPooling2D(pool_size=tam_pool))

cnn.add(Convolution2D(filtrosconv2, tam_filtro2, padding = 'same', activation = 'relu'))
cnn.add(MaxPooling2D(pool_size = tam_pool))

cnn.add(Convolution2D(filtrosconv3, tam_filtro3, padding = 'same', activation = 'relu'))
cnn.add(MaxPooling2D(pool_size = tam_pool))
cnn.add(Flatten())
cnn.add(Dense(640, activation = 'relu'))
cnn.add(Dropout(0.5))
cnn.add(Dense(clases, activation='softmax' ))

optimizar = tensorflow.keras.optimizers.Adam(learning_rate = lr)
cnn.fir(imagen_entreno, steps_per_epoch = pasos, epochs = iteraciones, validation_data = imagen_validacion, validaton_steps = pasos_validacion)

cnn.save('ModeloVocales2.h5')
cnn.save_weights('pesosVocales2.h5')