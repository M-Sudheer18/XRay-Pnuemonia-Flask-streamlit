from pathlib import Path

import numpy as np
from PIL import Image
from config import IMAGE_SIZE, ALLOWED_EXTENSIONS
from tensorflow.keras.applications.vgg16 import preprocess_input

# Validate Image Extension
def allowed_file(filename: str) -> bool:
    """
    Check whether the uploaded file has a valid image extension.
    """

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


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

