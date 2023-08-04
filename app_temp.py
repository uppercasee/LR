import base64
from flask import Flask, render_template, request, jsonify
import numpy as np
import cv2
import tensorflow as tf

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('./LetterRecognition.keras', compile=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    # Get the image from post request
    img = request.get_json()['img']
    # Decode the image
    decoded_img = base64.b64decode(img)
    # Convert to numpy array
    np_img = np.fromstring(decoded_img, dtype=np.uint8)
    # Convert to opencv image format
    img = cv2.imdecode(np_img, cv2.IMREAD_GRAYSCALE)
    # Resize the image to 64x64
    img = cv2.resize(img, (64, 64))
    # Reshape the image to 1 channel
    img = img.reshape(1, 64, 64, 1)
    # Normalize the image
    img = img / 255.0
    # Predict the class
    pred = model.predict(img)
    # Get the index of the class with maximum probability
    pred = np.argmax(pred, axis=1)[0]
    # Return the prediction
    return jsonify({'letter': chr(pred + 65)})


if __name__ == '__main__':
    app.run(debug=True)
