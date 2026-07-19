from pathlib import Path

import numpy as np
from PIL import Image
from tensorflow.keras.applications.vgg16 import preprocess_input
from config import IMAGE_SIZE, ALLOWED_EXTENSIONS

# Validate Image Extension
def allowed_file(filename: str) -> bool:
    """
    Check whether the uploaded file has a valid image extension.
    """

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

# CNN Preprocessing
def preprocess_cnn(image_path: str | Path) -> np.ndarray:
    """
    Preprocess image for CNN models.

    Output Shape:
        (1, 100, 100, 1)
    """
    image = Image.open(image_path).convert("L")

    # Converting Image Size
    image = image.resize(IMAGE_SIZE)

    # Image to Array
    image = np.array(image, dtype=np.float32)

    # image Normalizaton
    image /= 255.0

    # Expanding the dimentions
    image = np.expand_dims(image, axis=-1)

    # Expanding the Dimentions 
    image = np.expand_dims(image, axis=0)

    return image

# VGG16 Preprocessing
def preprocess_vgg(image_path: str | Path) -> np.ndarray:
    """
    Preprocess image for VGG16 model.

    Output Shape:
        (1, 100, 100, 3)
    """
    # Converting Image to RGB
    image = Image.open(image_path).convert('RGB')

    # Resizing Image
    image = image.resize(IMAGE_SIZE)

    # img --> Array
    image = np.array(image, dtype=np.float32)

    image = preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    return image