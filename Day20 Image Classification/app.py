from flask import Flask, render_template, request, jsonify
from PIL import Image
import numpy as np
import tensorflow as tf

app = Flask(__name__)
model = tf.keras.models.load_model('image_classifier_model.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        # Process the uploaded image
        img = Image.open(file)
        img = img.resize((224, 224))
        img = np.array(img) / 255.0  # Normalize
        img = np.expand_dims(img, axis=0)

        # Make a prediction
        predictions = model.predict(img)
        class_index = np.argmax(predictions)
        class_label = class_labels[class_index]  # Define class labels

        return jsonify({'prediction': class_label})

if __name__ == '__main__':
    app.run(debug=True)
