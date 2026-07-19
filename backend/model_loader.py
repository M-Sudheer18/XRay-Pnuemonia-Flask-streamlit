from huggingface_hub import hf_hub_download
from tensorflow.keras.models import load_model

from config import HF_REPO_ID, MODEL_FILES



# Download Models from Hugging Face
print("Downloading models from Hugging Face...")

MODEL_PATHS = {
    model_name : hf_hub_download(
        repo_id=HF_REPO_ID,
        filename=model_file
    ) for model_name, model_file in MODEL_FILES.items()
}
print("All models loaded successfully.")



# Load Models
print("Loading models... Please wait.")

MODELS = {
    model_name: load_model(model_path)
    for model_name, model_path in MODEL_PATHS.items()
}
print("All models downloaded successfully.")
    



# Get Selected Model
def get_model(model_name: str):
    """
    Returns the selected loaded model.

    Parameters
    ----------
    model_name : str
        cnn10, cnn20 or vgg16

    Returns
    -------
    tensorflow.keras.Model
    """
    if model_name not in MODELS:
        raise ValueError(f'Invalid Model: {model_name}')
        
    return MODELS[model_name]
