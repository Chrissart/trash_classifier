import streamlit
from streamlit_webrtc import webrtc_streamer

streamlit.title("Trash Classifier")


picture = streamlit.camera_input("Take a picture")

if picture:
    streamlit.image(picture)
    
webrtc_streamer(key="example")
