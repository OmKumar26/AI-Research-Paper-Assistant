from flask import Blueprint, request, jsonify
import os

from services.pdf_processor import load_text
from services.keyword import extract_keywords

from config import UPLOAD_FOLDER, KEYWORD_FOLDER
from utils.cache import load_json, save_json

keyword_bp = Blueprint("keyword", __name__)

os.makedirs(KEYWORD_FOLDER, exist_ok=True)


@keyword_bp.route("/keywords", methods=["POST"])
def keywords():

    data = request.get_json()
    filename = data.get("filename")

    if not filename:
        return jsonify({"error": "Filename required"}), 400

    pdf_path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(pdf_path):
        return jsonify({"error": "File not found"}), 404

    keyword_file = os.path.splitext(filename)[0] + "_keywords.json"
    keyword_path = os.path.join(KEYWORD_FOLDER, keyword_file)

    # Cache check
    if os.path.exists(keyword_path):
        keywords = load_json(keyword_path)

        return jsonify({
            "cached": True,
            "filename": filename,
            "keywords": keywords
        })

    # Generate keywords
    text = load_text(filename)
    keywords = extract_keywords(text)

    # Save cache
    save_json(keyword_path, keywords)

    return jsonify({
        "cached": False,
        "filename": filename,
        "keywords": keywords
    })