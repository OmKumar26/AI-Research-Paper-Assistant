from flask import Blueprint, request, jsonify
import os

from services.pdf_processor import load_text
from services.chunker import create_chunks

from config import UPLOAD_FOLDER, CHUNK_FOLDER
from utils.cache import load_json, save_json

chunk_bp = Blueprint("chunk", __name__)

os.makedirs(CHUNK_FOLDER, exist_ok=True)


@chunk_bp.route("/chunks", methods=["POST"])
def chunks():

    data = request.get_json()
    filename = data.get("filename")

    if not filename:
        return jsonify({"error": "Filename required"}), 400

    pdf_path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(pdf_path):
        return jsonify({"error": "File not found"}), 404

    chunk_file = os.path.splitext(filename)[0] + "_chunks.json"
    chunk_path = os.path.join(CHUNK_FOLDER, chunk_file)

    # Cache check
    if os.path.exists(chunk_path):
        chunks = load_json(chunk_path)

        return jsonify({
            "cached": True,
            "filename": filename,
            "chunks": chunks
        })

    # Generate chunks
    text = load_text(filename)
    chunks = create_chunks(text)

    # Save cache
    save_json(chunk_path, chunks)

    return jsonify({
        "cached": False,
        "filename": filename,
        "chunks": chunks
    })