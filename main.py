import tkinter as tk
import numpy as np
import tensorflow as tf
import cv2
from PIL import Image, ImageDraw, ImageOps
import io
import threading

# Load the trained model
model = tf.keras.models.load_model('LetterRecognition.keras')
# model = tf.keras.models.load_model('MNIST_CNN_model.h5')

# Function to preprocess the image and make the prediction
def predict_character(image):
    # Preprocess the image (resize and normalize)
    image = cv2.resize(image, (64, 64))
    image = image / 255.0
    # Expand dimensions to match the model input shape (batch_size, height, width, channels)
    image = np.expand_dims(image, axis=0)
    # Make the prediction using the loaded model
    prediction = model.predict(image)
    # Get the predicted character
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    predicted_character = characters[np.argmax(prediction)]
    return predicted_character, prediction

# Function to predict the drawn character and display top 5 predictions
def predict_drawn_character():
    image = canvas_to_image(canvas)
    predicted_character, prediction = predict_character(image)
    result_label.config(text=f'Predicted Character: {predicted_character}')

    # Get the top 5 predictions
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    top_5_indices = np.argsort(-prediction[0])[:5]
    top_5_predictions = [(characters[i], prediction[0][i]*100) for i in top_5_indices]

    # Update the predictions label
    predictions_text = '\n'.join(f'{char}: {prob:.2f}%' for char, prob in top_5_predictions)
    predictions_label.config(text=predictions_text)

# Function to convert canvas to grayscale image (PIL Image)
def canvas_to_image(canvas):
    ps = canvas.postscript(colormode='gray')
    image = Image.open(io.BytesIO(ps.encode('utf-8')))
    # Convert to grayscale (1 channel)
    image = image.convert('L')
    # # save the image
    # image.save('image.png')
    return np.array(image)

# # Function to convert canvas to grayscale image (PIL Image)
# def canvas_to_image(canvas):
#     ps = canvas.postscript(colormode='gray')
#     image = Image.open(io.BytesIO(ps.encode('utf-8')))
#     # Resize the image to 28x28
#     image = image.resize((28, 28))
#     # Convert to grayscale (1 channel)
#     image = image.convert('L')
#     # Convert PIL image to numpy array
#     np_image = np.array(image)
#     # Expand dimensions to match the model input shape (batch_size, height, width, channels)
#     np_image = np.expand_dims(np_image, axis=0)
#     # np_image = np.expand_dims(np_image, axis=1)  # Add a channel dimension (None, 1, 28, 28)
#     return np_image

# Function to clear the canvas
def clear_canvas():
    canvas.delete('all')

# Function to predict in a separate thread
def predict_thread():
    threading.Thread(target=predict_drawn_character).start()

# Create the GUI
root = tk.Tk()
root.title('Alphabet Recognition AI')

canvas_width, canvas_height = 640, 640
canvas = tk.Canvas(root, bg='white', width=canvas_width, height=canvas_height)
canvas.pack(pady=10)

result_label = tk.Label(root, text='', font=('Arial', 16))
result_label.pack()

# predict_button = tk.Button(root, text='Predict', command=predict_drawn_character)
# predict_button.pack(pady=10)

clear_button = tk.Button(root, text='Clear', command=clear_canvas)
clear_button.pack(pady=10)

# # Create a label to display the top 5 predicted characters and percentages
# predictions_label = tk.Label(root, text='', font=('Arial', 12))
# predictions_label.pack(side=tk.RIGHT, padx=10)

# # Variables to track whether the user is currently drawing
# is_drawing = False
# drawn_strokes = []

# # Delay in milliseconds before predicting after the user stops drawing
# PREDICTION_DELAY = 500

# # Draw on the canvas
# def start_drawing(event):
#     global is_drawing
#     is_drawing = True
#     drawn_strokes.append(event)

# def stop_drawing(event):
#     global is_drawing
#     is_drawing = False

# def paint(event):
#     if is_drawing:
#         x1, y1 = (event.x - 1), (event.y - 1)
#         x2, y2 = (event.x + 1), (event.y + 1)
#         canvas.create_oval(x1, y1, x2, y2, fill='black', width=5)
#         drawn_strokes.append(event)
#         root.after(PREDICTION_DELAY, predict_drawn_character)

# canvas.bind('<ButtonPress-1>', start_drawing)
# canvas.bind('<B1-Motion>', paint)
# canvas.bind('<ButtonRelease-1>', stop_drawing)

# # Function to predict the drawn character and display top 5 predictions
# def predict_drawn_character():
#     if drawn_strokes:
#         image = canvas_to_image(canvas)
#         predicted_character, prediction = predict_character(image)
#         result_label.config(text=f'Predicted Character: {predicted_character}')

#         # Get the top 5 predictions
#         characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#         top_5_indices = np.argsort(-prediction[0])[:5]
#         top_5_predictions = [(characters[i], prediction[0][i]*100) for i in top_5_indices]

#         # Update the predictions label
#         predictions_text = '\n'.join(f'{char}: {prob:.2f}%' for char, prob in top_5_predictions)
#         predictions_label.config(text=predictions_text)

#         # Clear the drawn strokes after prediction
#         drawn_strokes.clear()

# root.mainloop()

# Create a label to display the top 5 predicted characters and percentages
predictions_label = tk.Label(root, text='', font=('Arial', 12))
predictions_label.pack(side=tk.RIGHT, padx=10)

# Variables to track the drawn strokes
drawn_strokes = []

# Function to draw on the canvas
def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill='black', width=10)
    drawn_strokes.append(event)

canvas.bind('<B1-Motion>', paint)

# Function to predict the drawn character and display top 5 predictions
def predict_drawn_character():
    image = canvas_to_image(canvas)
    predicted_character, prediction = predict_character(image)
    result_label.config(text=f'Predicted Character: {predicted_character}')

    # Get the top 5 predictions
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    top_5_indices = np.argsort(-prediction[0])[:5]
    top_5_predictions = [(characters[i], prediction[0][i]*100) for i in top_5_indices]

    # Update the predictions label
    predictions_text = '\n'.join(f'{char}: {prob:.2f}%' for char, prob in top_5_predictions)
    predictions_label.config(text=predictions_text)

    # Clear the drawn strokes after prediction
    drawn_strokes.clear()

# Function to handle the prediction in a separate thread
def predict_thread():
    while True:
        if drawn_strokes:
            predict_drawn_character()

# Start the prediction thread
prediction_thread = threading.Thread(target=predict_thread)
prediction_thread.daemon = True
prediction_thread.start()

root.mainloop()