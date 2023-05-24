
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.applications.resnet import decode_predictions
from tensorflow.keras.applications.resnet import preprocess_input


classes = {0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic', 5: 'trash'}

def generar_mapa_calor_gradcam(img_array, modelo, nombre_ultima_capa_conv=None, indice_prediccion=None):
    # Creamos un modelo que mapea las entradas del modelo a las activaciones de la última capa convolucional y las salidas del modelo original
    modelo_gradcam = tf.keras.models.Model(
        [modelo.inputs], [modelo.get_layer(nombre_ultima_capa_conv).output, modelo.output]
    )

    # Computamos los gradientes de la clase predicha con respecto a las características de salida de la última capa convolucional
    with tf.GradientTape() as cinta:
        salida_ultima_capa_conv, predicciones = modelo_gradcam(img_array)
        if indice_prediccion is None:
            indice_prediccion = tf.argmax(predicciones[0])
        canal_clase = predicciones[:, indice_prediccion]

    # Calculamos el gradiente de la salida de la clase predicha con respecto a la salida de la última capa convolucional
    gradientes = cinta.gradient(canal_clase, salida_ultima_capa_conv)

    # Hacemos un pooling global de los gradientes a través de los ejes (0, 1, 2) para obtener el valor medio de los gradientes para cada canal del feature-map
    gradientes_promedio = tf.reduce_mean(gradientes, axis=(0, 1, 2))

    # Multiplicamos cada canal en el feature-map por "cuánto importa este canal" con respecto a la clase predicha
    salida_ultima_capa_conv = salida_ultima_capa_conv[0]
    mapa_calor = salida_ultima_capa_conv @ gradientes_promedio[..., tf.newaxis]
    mapa_calor = tf.squeeze(mapa_calor)

    # Normalizamos el mapa de calor entre 0 y 1 para su visualización
    mapa_calor = tf.maximum(mapa_calor, 0) / tf.math.reduce_max(mapa_calor)
    return mapa_calor.numpy()

def superponer_mapa_calor(mapa_calor, img, alpha=0.4, colormap=cv2.COLORMAP_VIRIDIS):
    mapa_calor = cv2.resize(mapa_calor, (img.shape[1], img.shape[0]))
    mapa_calor = cv2.applyColorMap(np.uint8(255 * mapa_calor), colormap)
    salida = cv2.addWeighted(cv2.cvtColor(img, cv2.COLOR_RGB2BGR), alpha, mapa_calor, 1 - alpha, 0)
    return salida

def predecir_imagen(ruta_imagen, modelo, nombre_ultima_capa_conv='conv5_block3_out'):
    img = image.load_img(ruta_imagen, target_size=(150, 150))
    img_array = preprocess_input(image.img_to_array(img))
    img_array = np.expand_dims(img_array, axis=0)

    predicciones = modelo.predict(img_array)
    mapa_calor = generar_mapa_calor_gradcam(img_array, modelo, nombre_ultima_capa_conv)
    mapa_calor = cv2.resize(mapa_calor, (img.size[0], img.size[1]))

    img = np.asarray(img)
    imagen_superpuesta = superponer_mapa_calor(mapa_calor, img)
    
    plt.matshow(imagen_superpuesta)
    return classes[np.argmax(predicciones[0])], max(predicciones[0])