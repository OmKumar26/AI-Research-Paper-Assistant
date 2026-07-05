from flask import Blueprint, request, jsonify
import os
import numpy as np
import faiss

from services.faiss_index import create_faiss_index

faiss_bp = Blueprint("faiss", __name__)

EMBEDDING_FOLDER = os.path.join(os.getcwd(), "embeddings")
FAISS_FOLDER = os.path.join(os.getcwd(), "faiss_indexes")

os.makedirs(FAISS_FOLDER, exist_ok=True)


@faiss_bp.route("/faiss", methods=["POST"])
def build_index():

    data = request.get_json()
    filename = data.get("filename")

    if not filename:
        return jsonify({"error": "Filename required"}), 400

    embedding_file = os.path.splitext(filename)[0] + "_embeddings.npy"
    embedding_path = os.path.join(EMBEDDING_FOLDER, embedding_file)

    if not os.path.exists(embedding_path):
        return jsonify({"error": "Generate embeddings first"}), 404

    index_file = os.path.splitext(filename)[0] + ".index"
    index_path = os.path.join(FAISS_FOLDER, index_file)

    if os.path.exists(index_path):
        return jsonify({
            "cached": True,
            "filename": filename
        })

    embeddings = np.load(embedding_path)

    index = create_faiss_index(embeddings)

    faiss.write_index(index, index_path)

    return jsonify({
        "cached": False,
        "filename": filename,
        "vectors": index.ntotal
    })