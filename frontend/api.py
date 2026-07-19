# Chest X-Ray Pneumonia Detection
# Frontend API Helper

import requests

# Flask Backend URL

BASE_URL = "http://127.0.0.1:5000"

PREDICT_URL = f"{BASE_URL}/predict"
HEALTH_URL  = f"{BASE_URL}/health"

# Check Backend Status
def check_status():
    """
    Checks whether the Flask backend is running.

    Returns
    -------
    bool
        True if backend is available.
        False otherwise.
    """

    try:
        response = requests.get(
            HEALTH_URL,
            timeout=5
        )

        return response.status_code == 200
    
    except requests.exceptions.RequestException:
        return False
    
    

# Predict Image
def predict_image(image_file, model_name):
    """
    Sends an X-ray image to the Flask backend
    for prediction.

    Parameters
    ----------
    image_file : UploadedFile
        Streamlit uploaded image.

    model_name : str
        cnn10
        cnn20
        vgg16

    Returns
    -------
    dict
        JSON response from Flask.
    """
    # Reset the file pointer
    image_file.seek(0)

     
    files = {
        "image": (
            image_file.name,
            image_file,
            image_file.type
        )
    }

    data = {
        "model": model_name
    }

    try:
        response = requests.post(
            PREDICT_URL,
            files=files,
            data=data,
            timeout=60
        )
        return response.json()
    
    except requests.exceptions.RequestException:

        return {
            "success": False,
            "error" : "Unable to connect to Flask backend."
        }


if __name__ == "__main__":

    print("Checking Flask Server...")

    if check_status():
        print("Backend is Running ✅")
    else:
        print("Backend is NOT Running ❌")




















