from flask import Blueprint, request, jsonify
import os

from services.pdf_processor import load_text
from services.ner import extract_entities

from config import UPLOAD_FOLDER, ENTITIES_FOLDER
from utils.cache import load_json, save_json

ner_bp = Blueprint("ner", __name__)

os.makedirs(ENTITIES_FOLDER, exist_ok=True)


@ner_bp.route("/entities", methods=["POST"])
def get_entities():

    data = request.get_json()
    filename = data.get("filename")

    if not filename:
        return jsonify({"error": "Filename required"}), 400

    pdf_path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(pdf_path):
        return jsonify({"error": "File not found"}), 404

    entity_file = os.path.splitext(filename)[0] + "_entities.json"
    entity_path = os.path.join(ENTITIES_FOLDER, entity_file)

    # Cache check
    if os.path.exists(entity_path):
        entities = load_json(entity_path)

        return jsonify({
            "cached": True,
            "filename": filename,
            "entities": entities
        })

    # Generate entities
    text = load_text(filename)
    entities = extract_entities(text)

    # Save cache
    save_json(entity_path, entities)

    return jsonify({
        "cached": False,
        "filename": filename,
        "entities": entities
    })