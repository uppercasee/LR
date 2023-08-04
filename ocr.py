import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np

# Load your ML model (LetterRecognition.keras)
model = tf.keras.models.load_model('LetterRecognition.keras')

class OCRToolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR Tool")

        # Create buttons and labels
        self.upload_button = tk.Button(root, text="Upload Image/PDF", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.result_label = tk.Label(root, font=("Arial", 20))
        self.result_label.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image/PDF Files", "*.png *.jpg *.jpeg *.pdf")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((300, 300))  # Resize the image to display it on the GUI
            self.display_image(image)
            text = self.extract_text(image)
            self.result_label.config(text=text)

    def display_image(self, image):
        img = ImageTk.PhotoImage(image)
        self.image_label.config(image=img)
        self.image_label.image = img

    def extract_text(self, image):
        # Preprocess the image (if required) and use your OCR model to predict the characters
        # expected shape = (None, 64, 64)

        # Convert the image to grayscale
        gray_image = image.convert("L")

        # Resize the image to match the expected input shape of the model (64x64)
        resized_image = gray_image.resize((64, 64))

        # Convert the image to a numpy array
        image_array = np.array(resized_image)

        # Normalize the pixel values to [0, 1]
        image_array = image_array / 255.0

        # Add a batch dimension as the model expects batched input
        image_array = np.expand_dims(image_array, axis=0)

        # Make predictions using the loaded model
        predictions = model.predict(image_array)

        # Process the predictions to extract the text (e.g., argmax for character class)
        predicted_text = process_predictions(predictions)

        return predicted_text

def process_predictions(predictions):
    # Implement your logic to process the predictions and convert them to text
    # Since the input shape is (None, 64, 64), you might have a sequence of characters
    # For example, if you used one-hot encoding for character classes, you can find the argmax for each time step
    # along the sequence to get the characters for the entire input image.

    # Assuming your model outputs probabilities (e.g., softmax), you can use argmax along the last axis (axis=-1)
    predicted_indices = np.argmax(predictions, axis=-1)
    print(predicted_indices)

    # Convert the predicted indices to characters based on your mapping
    # For example, if you have a mapping like "0-9A-Za-z" for class indices 0 to 61:
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    print(characters[44])
    predicted_text = "".join(chr(ord('0') + idx) if 0 <= idx <= 9 else characters[idx - 10] for idx in predicted_indices[0])

    return predicted_text


if __name__ == "__main__":
    root = tk.Tk()
    app = OCRToolApp(root)
    root.mainloop()
