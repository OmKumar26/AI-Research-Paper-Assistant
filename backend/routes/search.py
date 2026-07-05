from flask import Blueprint, request, jsonify
import os
import json

from services.search import semantic_search

search_bp = Blueprint("search", __name__)

CHUNK_FOLDER = os.path.join(os.getcwd(), "chunks")
FAISS_FOLDER = os.path.join(os.getcwd(), "faiss_indexes")


@search_bp.route("/search", methods=["POST"])
def search():

    data = request.get_json()

    filename = data.get("filename")
    query = data.get("query")

    if not filename or not query:
        return jsonify({"error": "Filename and query required"}), 400

    chunk_path = os.path.join(
        CHUNK_FOLDER,
        os.path.splitext(filename)[0] + "_chunks.json"
    )

    index_path = os.path.join(
        FAISS_FOLDER,
        os.path.splitext(filename)[0] + ".index"
    )

    if not os.path.exists(chunk_path):
        return jsonify({"error": "Chunks not found"}), 404

    if not os.path.exists(index_path):
        return jsonify({"error": "FAISS index not found"}), 404

    with open(chunk_path, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    results = semantic_search(query, index_path, chunks)

    return jsonify({
        "query": query,
        "results": results
    })