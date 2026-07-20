from pathlib import Path


# __file__ returns something like 
# XRay_Project/config.py 

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / 'uploads'

# Create uploads folder automatically if it doesn't exist
UPLOAD_DIR.mkdir(exist_ok=True)


# Hugging Face Configuration

HF_REPO_ID = "Sudheer17/XRay-Classifier"

MODEL_FILES = {
    "vgg16": "best_model.keras"
}

# Model Display Names
MODEL_NAMES = {
    "vgg16": "VGG16 Transfer Learning"
}

# Image Settings
IMAGE_SIZE = (100, 100)
ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png"
}

# Class Labels
CLASS_NAMES = {
    0: "NORMAL",
    1: "PNEUMONIA",
}

# Flask Settings
HOST = "127.0.0.1"
PORT = 5000
DEBUG = True