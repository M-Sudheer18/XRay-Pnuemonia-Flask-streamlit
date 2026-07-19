import os
import traceback

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

from config import HOST, PORT, DEBUG, UPLOAD_DIR
from predictor import predict
from preprocess import allowed_file

# Flask App
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = str(UPLOAD_DIR)


# Home Route
@app.route('/', methods = ['GET'])
def home():
    return jsonify({
        "message": "Chest X-Ray Pneumonia Detection API",
        "status": "Running",
        "available_models": [
            "cnn10",
            "cnn20",
            "vgg16"
        ]
    })

# Health Check
@app.route('/health', methods = ['GET'])
def health():
    return jsonify({
        'status': 'Healthy'
    })

# Debug Route (Temporary)
@app.route("/debug", methods=["POST"])
def debug():
    return jsonify({
        "files": list(request.files.keys()),
        "form": request.form.to_dict()
    })


# Prediction Route
@app.route('/predict', methods = ['POST'])
def predict_route():
    # if "image" not in request.files:
    print("request.files :", request.files)
    print("request.form  :", request.form)
    if "image" not in request.files:
        return jsonify({
            'error': 'No Image Uploaded'
        }), 400
    image = request.files['image']


    # Check Filename
    if image.filename == '':
        return jsonify({
            'error': 'No image selected.'
        }), 400
    

    # Validate image format
    if not allowed_file(image.filename):
        return jsonify({
            "error": "Invalid image format. Use JPG, JPEG or PNG."
        }), 400
    

    # Selected model
    model_name = request.form.get('model', 'cnn10')
    
    # Save image
    filename = secure_filename(image.filename)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(image_path)
    print("Saved Image :", image_path)
    print("Exists      :", os.path.exists(image_path))
    print("Size (bytes):", os.path.getsize(image_path))

    try:
        result = predict(
            image_path,
            model_name
        )
        # Delete uploaded image after prediction
        if os.path.exists(image_path):
            os.remove(image_path)

        return jsonify(result)
    
    except Exception as e:
        print("\n========== ERROR ==========")
        traceback.print_exc()
        print("===========================\n")

        if os.path.exists(image_path):
            os.remove(image_path)
        return jsonify({
            "error": str(e)
        }), 500
    
# Run Server
if __name__ == '__main__':
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG
    )