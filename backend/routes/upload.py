from flask import Blueprint, request, jsonify
import os
from services.pdf_processor import extract_text, save_text
upload_bp = Blueprint("upload", __name__)

# Absolute path to uploads folder
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@upload_bp.route("/upload", methods=["POST"])
def upload_pdf():
    print("\n========== Upload Request ==========")
    print("Current Working Directory:", os.getcwd())
    print("Content-Type:", request.content_type)
    print("Request Files:", request.files)

    if "file" not in request.files:
        print(" No file found in request")
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    print("Filename:", file.filename)

    if file.filename == "":
        print(" No file selected")
        return jsonify({"error": "No file selected"}), 400

    if not file.filename.lower().endswith(".pdf"):
        print(" Invalid file type")
        return jsonify({"error": "Only PDF files are allowed"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    print("Saving to:", filepath)

    try:
        file.save(filepath)
        text = extract_text(filepath)
        save_text(file.filename, text)
        print("File saved successfully")
    except Exception as e:
        print("Error while saving:", str(e))
        return jsonify({"error": str(e)}), 500

    return jsonify({
    "message": "PDF uploaded successfully",
    "filename": file.filename
})