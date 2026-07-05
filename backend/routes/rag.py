from flask import Blueprint, request, jsonify
import os
import json

from services.search import retrieve_chunks
from services.rag import generate_answer

rag_bp = Blueprint("rag", __name__)

CHUNK_FOLDER = os.path.join(os.getcwd(), "chunks")
FAISS_FOLDER = os.path.join(os.getcwd(), "faiss_indexes")


@rag_bp.route("/chat", methods=["POST"])
def chat():

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

    with open(chunk_path, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    results = retrieve_chunks(query, index_path, chunks)

    context = "\n\n".join([r["text"] for r in results])

    answer = generate_answer(query, context)

    return jsonify({
        "question": query,
        "answer": answer,
        "sources": [r["chunk_id"] for r in results]
    })