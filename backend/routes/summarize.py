from flask import Blueprint, request, jsonify
import os

from services.pdf_processor import load_text
from services.summarizer import summarize_text

summarize_bp = Blueprint("summarize", __name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")


@summarize_bp.route("/summarize", methods=["POST"])
def summarize():

    data = request.get_json()

    filename = data.get("filename")

    if not filename:
        return jsonify({"error": "Filename required"}), 400

    pdf_path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(pdf_path):
        return jsonify({"error": "File not found"}), 404

    text = load_text(filename)

    summary = summarize_text(text)

    return jsonify({
        "filename": filename,
        "summary": summary
    })