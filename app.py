from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
from enhancer.upscaler import enhance_image

app = Flask(__name__)
CORS(app)  # Enable CORS for mobile frontend

UPLOAD_FOLDER = "inputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/enhance", methods=["POST"])
def enhance():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    # Save uploaded file
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    # Run enhancement
    output_path = enhance_image(input_path)

    if output_path and os.path.exists(output_path):
        return send_file(output_path, mimetype="image/png", as_attachment=True)
    else:
        return jsonify({"error": "Enhancement failed"}), 500

if __name__ == "__main__":
    app.run(debug=True)
