from flask import Flask, request, jsonify
from flask_cors import CORS
from vad import process_audio

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filepath = 'uploaded_audio.wav'
        file.save(filepath)
        results = process_audio(filepath)
        return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
