from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation_#
from tensorflow.python.keras.layers import Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K

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