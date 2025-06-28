from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Tambahkan ini
from sklearn.cluster import KMeans
import numpy as np
import cv2
import io
from PIL import Image

app = Flask(__name__)
CORS(app)  # Izinkan semua origin (default)

@app.route('/')
def home():
    return render_template('color-palette-extractor.html')

@app.route('/extract-colors', methods=['POST'])
def extract_colors():
    file = request.files['image']
    image = Image.open(file.stream).convert('RGB')
    image = np.array(image)

    if image.shape[0] * image.shape[1] > 500_000:
        scale = 0.5
        image = cv2.resize(image, (0, 0), fx=scale, fy=scale)

    pixels = image.reshape((-1, 3))
    kmeans = KMeans(n_clusters=5, random_state=0).fit(pixels)
    colors = kmeans.cluster_centers_.astype(int)

    # Urutkan berdasarkan jumlah pixel per cluster
    labels = kmeans.labels_
    counts = np.bincount(labels)
    sorted_indices = np.argsort(counts)[::-1]
    sorted_colors = colors[sorted_indices]

    hex_colors = ['#{:02x}{:02x}{:02x}'.format(*color) for color in sorted_colors]

    return jsonify(hex_colors)

if __name__ == '__main__':
    app.run(debug=True)