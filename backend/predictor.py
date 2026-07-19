import numpy as np

from config import CLASS_NAMES, MODEL_NAMES
from model_loader import get_model
from preprocess import preprocess_cnn, preprocess_vgg


# Predict Pneumonia
def predict(image_path: str, model_name: str) -> dict:
    """
    Predict whether the uploaded X-ray is NORMAL or PNEUMONIA.
    
    Parameters
    ----------
    image_path : str | Path
        Uploaded image path.

    model_name : str
        cnn10, cnn20 or vgg16

    Returns
    -------
    dict
        Prediction result.
    """
    # Select Image Preprocessing
    if model_name in ("cnn10", "cnn20"):
        image = preprocess_cnn(image_path)
    elif model_name == "vgg16":
        image = preprocess_vgg(image_path)
    else:
        raise ValueError(f"Invalid model: {model_name}")
    
    # Load Selected Model
    model = get_model(model_name)

    # Model Prediction
    prediction = model.predict(image, verbose=0)

    print("Prediction Shape:", prediction.shape)
    print("Prediction:", prediction)   

    # Binary Sigmoid Model 

    if prediction.shape[1] == 1:

        score = float(prediction[0][0])

        if score >= 0.5:
            prediction_label = "PNEUMONIA"
            confidence = score * 100
        else:
            prediction_label = "NORMAL"
            confidence = (1 - score) * 100

        probabilities = {
            "NORMAL": round((1 - score) * 100, 2),
            "PNEUMONIA": round(score * 100, 2)
        }

    # Two-Class Softmax Model
    elif prediction.shape[1] == 2:
        class_index = int(np.argmax(prediction[0]))

        prediction_label = CLASS_NAMES[class_index]
        confidence = float(prediction[0][class_index]) * 100

        probabilities = {
            CLASS_NAMES[0]: round(float(prediction[0][0]) * 100, 2),
            CLASS_NAMES[1]: round(float(prediction[0][1]) * 100, 2)
        }
    else:
        raise ValueError(
            f"Unsupported model output shape: {prediction.shape}"
        )

    # Return Prediction
    return {
        "prediction": prediction_label,
        "confidence": round(confidence, 2),
        "probabilities": probabilities,
        "model": MODEL_NAMES[model_name]
    }




