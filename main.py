"""

"""
import streamlit
from streamlit_webrtc import webrtc_streamer
from keras.models import load_model
from keras.utils import plot_model
import numpy
import cv2

from src.predict_image import predict_image

# Configuración de la página
streamlit.set_page_config(
    page_title="Trash Classifier",
    page_icon="🗑️",
)
# # Carga el modelo desde el archivo
model = load_model("./model/ResNet101V2_TrashClassifierV1.h5")

# Contenido de la página
streamlit.title("Trash Classifier 🗑️")
# # Agrega un selector de vistas en la barra lateral
view = streamlit.sidebar.selectbox(
        label="Selecciona una vista",
        options=[
            "Modo Foto",
            "Modo Streaming",
            "Acerca de"
        ]
    )
# # Dependiendo de la opción seleccionada, muestra una vista diferente
if view == "Modo Foto":
    picture = streamlit.camera_input("Captura un residuo")
    photo = streamlit.sidebar.file_uploader(
                "Arrastra y suelta una imagen aquí",
                type=[
                    'png',
                    'jpg',
                    'jpeg',
                ]
            )
    # # Verifica si se subió una imagen
    if picture or photo:
        if picture:
            streamlit.image(picture, caption="Imagen capturada")
            image_array = numpy.asarray(bytearray(picture.read()), dtype=numpy.uint8)
            image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
            image = cv2.resize(image, (150, 150))

        else:
            streamlit.image(photo, caption="Imagen cargada")
            image = numpy.asarray(photo)

        proceso = streamlit.sidebar.button("Procesar!")
        proceso = streamlit.button("Procesar!", use_container_width=True)

        if proceso:
            streamlit.write("Procesando...")
            # Aquí deberías agregar el código para procesar la imagen con tu modelo predictivo
            predicted_class, confidence = predict_image(model, image)
            if predicted_class:
                streamlit.write(f"El residuo es: {predicted_class} con un {confidence*100:.2f}% de confianza.")
    else:
        streamlit.write("Por favor, sube una imagen.")
elif view == "Modo Streaming":
    # # Código para la segunda vista
    streamlit.write("Bienvenido a la segunda vista.")
    webrtc_streamer(key="example", sendback_audio=False)
elif view == "Acerca de":
    # # Código para la tercera vista
    streamlit.write(model)
    # streamlit.write(plot_model(model))
