import os

BASE_DIR = os.getcwd()

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
TEXT_FOLDER = os.path.join(BASE_DIR, "documents")
SUMMARY_FOLDER = os.path.join(BASE_DIR, "summaries")
ENTITIES_FOLDER = os.path.join(BASE_DIR, "entities")
KEYWORD_FOLDER = os.path.join(BASE_DIR, "keywords")
CHUNK_FOLDER = os.path.join(BASE_DIR, "chunks")
EMBEDDING_FOLDER = os.path.join(BASE_DIR, "embeddings")
FAISS_FOLDER = os.path.join(BASE_DIR, "faiss_indexes")