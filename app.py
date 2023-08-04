import io
import cv2
from flask import Flask, render_template, request, jsonify
import base64
from PIL import Image
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load your ML model (LetterRecognition.keras)
model = tf.keras.models.load_model('LetterRecognition.keras')

def preprocess_image(img_data):
    img_str = img_data.split(',')[1]
    decoded = base64.b64decode(img_str)
    image = Image.open(io.BytesIO(decoded)).convert("L")
    image = image.resize((64, 64))
    image = np.array(image)
    image = image.reshape(1, 64, 64, 1)
    image = image / 255.0
    return image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        image_data = data['image_data']
        processed_image = preprocess_image(image_data)
        # save the image
        cv2.imwrite('image.png', processed_image)
        prediction = model.predict(processed_image)
        # Get the predicted character
        characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        predicted_character = characters[np.argmax(prediction)]
        return jsonify({'prediction': predicted_character})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
