"""

"""
import streamlit
from PIL import Image
from streamlit_webrtc import webrtc_streamer
from keras.models import load_model
from keras.utils import plot_model

from src.predecir_imagen import predecir_imagen

# Configuración de la página
streamlit.set_page_config(
    page_title="Trash Classifier",
    page_icon="🗑️",
)
# # Carga el modelo desde el archivo
@streamlit.cache(allow_output_mutation=True)
def load_model_in_cache():
  model=load_model('/content/my_model2.hdf5')
  return model
with streamlit.spinner('Cargando todo lo necesario..'):
  model=load_model("./model/ResNet101V2_TrashClassifierV1.h5")

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
        print("Picture ", type(picture))
        print("Photo ", type(photo))
        if picture:
            streamlit.image(picture, caption="Imagen capturada")
            image = picture
        else:
            print("Espero debuguees esto rápido :)", type(photo))
            streamlit.image(photo, caption="Imagen cargada")
            image = Image.open(photo).tobytes()
            

        sidebar_process = streamlit.sidebar.button("Procesar!", use_container_width=True, key="sidebar_proceso")
        proceso = streamlit.button("Procesar!", use_container_width=True, key="main_proceso")

        if proceso or sidebar_process:
            streamlit.write("Procesando...")
            predicted_class, confidence = predecir_imagen(model, image)
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
