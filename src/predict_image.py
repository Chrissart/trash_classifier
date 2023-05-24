from keras.utils import load_img, img_to_array
import numpy
import io

# classes = {'cardboard': 0, 'glass': 1, 'metal': 2, 'paper': 3, 'plastic': 4, 'trash': 5}
classes = {0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic', 5: 'trash'}

def predict_image(model, image, img_size=(150, 150)):
    image = load_img(image, target_size=img_size)
    input_arr = img_to_array(image)
    input_arr = numpy.array([input_arr])
    
    # Get the model's predictions for this batch of images
    predictions = model.predict(input_arr)

    # Get the index of the highest score in the predictions array
    predicted_class = numpy.argmax(predictions[0])
    print(predictions, predicted_class)
    
    return classes[predicted_class], max(predictions[0])

# image = tf.keras.utils.load_img(image_path)
# input_arr = tf.keras.utils.img_to_array(image)
# input_arr = np.array([input_arr])  # Convert single image to a batch.
# predictions = model.predict(input_arr)