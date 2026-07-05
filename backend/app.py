from flask import Flask
from flask_cors import CORS

from routes.upload import upload_bp
from routes.summarize import summarize_bp
from routes.ner import ner_bp
from routes.keyword import keyword_bp
from routes.chunker import chunk_bp
from routes.embedding import embedding_bp
from routes.faiss_index import faiss_bp
from routes.search import search_bp
from routes.rag import rag_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(upload_bp)
app.register_blueprint(summarize_bp)
app.register_blueprint(ner_bp)
app.register_blueprint(keyword_bp)
app.register_blueprint(chunk_bp)
app.register_blueprint(embedding_bp)
app.register_blueprint(faiss_bp)
app.register_blueprint(search_bp)
app.register_blueprint(rag_bp)


@app.route("/")
def home():
    return {
        "message": "AI Research Paper Assistant Backend Running"
    }


if __name__ == "__main__":
    app.run(debug=True)