from huggingface_hub import hf_hub_download
from tensorflow.keras.models import load_model
from tensorflow.keras import backend as K
import gc

from config import HF_REPO_ID, MODEL_FILES

# Download model files from Hugging Face
print("Downloading model files from Hugging Face...", flush=True)

MODEL_PATHS = {
    model_name: hf_hub_download(
        repo_id=HF_REPO_ID,
        filename=model_file
    )
    for model_name, model_file in MODEL_FILES.items()
}

print("Model files downloaded successfully.", flush=True)

# Store only ONE loaded model
_CURRENT_MODEL = None
_CURRENT_MODEL_NAME = None


def get_model(model_name: str):
    """
    Load only the requested model.
    Unload the previous model if a different model is requested.
    """

    global _CURRENT_MODEL, _CURRENT_MODEL_NAME

    if model_name not in MODEL_PATHS:
        raise ValueError(f"Invalid model: {model_name}")

    # Already loaded
    if _CURRENT_MODEL_NAME == model_name:
        return _CURRENT_MODEL

    # Unload previous model
    if _CURRENT_MODEL is not None:
        print(f"Unloading {_CURRENT_MODEL_NAME}...", flush=True)

        _CURRENT_MODEL = None
        _CURRENT_MODEL_NAME = None

        K.clear_session()
        gc.collect()

    print(f"Loading {model_name}...", flush=True)

    _CURRENT_MODEL = load_model(MODEL_PATHS[model_name])
    _CURRENT_MODEL_NAME = model_name

    print(f"{model_name} loaded successfully.", flush=True)

    return _CURRENT_MODEL