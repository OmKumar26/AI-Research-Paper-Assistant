from flask import Blueprint, request, jsonify
import os
import json
import numpy as np

from services.embedding import generate_embeddings

embedding_bp = Blueprint("embedding", __name__)

CHUNK_FOLDER = os.path.join(os.getcwd(), "chunks")
EMBEDDING_FOLDER = os.path.join(os.getcwd(), "embeddings")

os.makedirs(EMBEDDING_FOLDER, exist_ok=True)


@embedding_bp.route("/embeddings", methods=["POST"])
def embeddings():

    data = request.get_json()
    filename = data.get("filename")

    if not filename:
        return jsonify({"error": "Filename required"}), 400

    chunk_file = os.path.splitext(filename)[0] + "_chunks.json"
    chunk_path = os.path.join(CHUNK_FOLDER, chunk_file)

    if not os.path.exists(chunk_path):
        return jsonify({"error": "Generate chunks first"}), 404

    embedding_file = os.path.splitext(filename)[0] + "_embeddings.npy"
    embedding_path = os.path.join(EMBEDDING_FOLDER, embedding_file)

    if os.path.exists(embedding_path):
        return jsonify({
            "cached": True,
            "filename": filename
        })

    with open(chunk_path, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    embeddings = generate_embeddings(chunks)

    np.save(embedding_path, embeddings)

    return jsonify({
        "cached": False,
        "filename": filename,
        "total_embeddings": len(embeddings)
    })