🎨 Color Detector

A simple web-based application that detects the dominant colors from an image using K-Means Clustering. Built with Python, Flask, OpenCV, and scikit-learn.

🔧 Features

- Upload any image (JPG, PNG, etc.)
- Detects and displays the most dominant colors
- Clean and user-friendly interface
- Fast and lightweight API using Flask

🖼️ How It Works

- User uploads an image
- Image is processed using OpenCV
- KMeans clustering is applied to group similar colors
- The most dominant colors are extracted and displayed

Tech Stack

- Flask – Backend web framework
- Flask-CORS – Handle cross-origin requests
- OpenCV – Image processing
- scikit-learn – KMeans clustering for color grouping
- NumPy – Numerical processing
- Pillow (PIL) – Image file handling

🚀 Getting Started
Prerequisites
Make sure you have Python 3 and pip installed.

Installation
git clone https://github.com/fadhilalziqra/ColorDetector.git
cd ColorDetector
pip install -r requirements.txt

Run the app
python app.py

Then open your browser and go to
http://localhost:5000

📂 Project Structure
ColorDetector/
│

├── static/                  # Static files (CSS, JS, images)

├── templates/

│   └── color-palette-extractor.html  # Main HTML page

├── app.py                  # Main backend Flask app

├── requirements.txt        # Python dependencies

📌 License
This project is open-source and free to use under the MIT License.
