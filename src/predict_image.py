from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras.preprocessing import image
import numpy as np

# classes = {'cardboard': 0, 'glass': 1, 'metal': 2, 'paper': 3, 'plastic': 4, 'trash': 5}
classes = {0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic', 5: 'trash'}

def predict_image(model, image, img_size=(150, 150)):
    # Load the image
    img = load_img(image.file, target_size=img_size)
    
    # Convert the image to a numpy array and scale the pixel values to the range [0,1]
    img_array = img_to_array(img) / 255.0

    # Add an extra dimension to the array, because the model expects batches of images
    img_batch = np.expand_dims(img_array, axis=0)

    # Get the model's predictions for this batch of images
    predictions = model.predict(img_batch)

    # Get the index of the highest score in the predictions array
    predicted_class = np.argmax(predictions[0])

    return classes[predicted_class]
