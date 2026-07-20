# Chest X-Ray Pneumonia Detection
# Frontend API Helper

import requests

# Flask Backend URL

CNN_BACKEND = "https://xray-pnuemonia-flask-streamlit-1.onrender.com"
VGG_BACKEND = "https://xray-pnuemonia-flask-streamlit-2.onrender.com"



# Check Backend Status
def check_status():
    """
    Checks whether the Flask backend is running.
    """

    try:
        response = requests.get(
            f"{CNN_BACKEND}/health",
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
    if model_name == "vgg16":
        predict_url = f"{VGG_BACKEND}/predict"
    else:
        predict_url = f"{CNN_BACKEND}/predict"

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
            predict_url,
            files=files,
            data=data,
            timeout=60
        )

        print("Status Code:", response.status_code)
        print("Response:", response.text)

        if response.status_code != 200:
            return {
                "success": False,
                "error": f"Backend Error ({response.status_code}): {response.text}"
            }

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




















