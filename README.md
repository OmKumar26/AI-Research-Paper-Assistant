# 📄 AI Research Paper Assistant

An AI-powered Research Paper Assistant that enables users to upload research papers, extract and analyze their contents, and ask natural language questions using a Retrieval-Augmented Generation (RAG) pipeline.

The project combines NLP techniques, semantic search, vector databases, and Google's Gemini model to provide context-aware answers grounded in the uploaded research paper.

---

## ✨ Features

- 📤 Upload Research Papers (PDF)
- 📄 Extract text from PDFs
- 📝 Automatic Paper Summarization
- 🏷️ Named Entity Recognition (spaCy)
- 🔑 Keyword Extraction (KeyBERT)
- ✂️ Intelligent Text Chunking
- 🧠 Sentence Embeddings (Sentence Transformers)
- 🔍 Semantic Search using FAISS
- 🤖 RAG-based Question Answering with Google Gemini
- 💾 Caching of processed results for faster responses

---

## 🏗️ Project Architecture

```
                PDF Upload
                     │
                     ▼
            Text Extraction (PyMuPDF)
                     │
                     ▼
             Store Extracted Text
                     │
     ┌───────────────┼────────────────┐
     ▼               ▼                ▼
 Summary         Named Entities    Keywords
     │               │                │
     └───────────────┼────────────────┘
                     ▼
             Text Chunking
                     ▼
          Sentence Embeddings
                     ▼
             FAISS Vector Index
                     ▼
             Semantic Retrieval
                     ▼
             Google Gemini (RAG)
                     ▼
            Context-Aware Answers
```

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- Flask-CORS

### NLP
- spaCy
- KeyBERT
- Sentence Transformers
- Hugging Face Transformers

### AI / LLM
- Google Gemini API

### Vector Database
- FAISS

### PDF Processing
- PyMuPDF (fitz)

### Other Libraries
- NumPy
- python-dotenv

---

## 📂 Project Structure

```
AI-Research-Paper-Assistant/
│
├── backend/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   ├── data/
│   ├── uploads/
│   ├── documents/
│   ├── summaries/
│   ├── entities/
│   ├── keywords/
│   ├── chunks/
│   ├── embeddings/
│   ├── faiss_indexes/
│   ├── app.py
│   ├── config.py
│   └── requirements.txt
│
├── frontend/ 
│
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/OmKumar26/AI-Research-Paper-Assistant.git
```

Move into the backend folder

```bash
cd backend
```

Install dependencies

```bash
pip install -r requirements.txt
```

Download the spaCy model

```bash
python -m spacy download en_core_web_sm
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the Flask server

```bash
python app.py
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/upload` | Upload PDF |
| POST | `/summarize` | Generate Summary |
| POST | `/entities` | Extract Named Entities |
| POST | `/keywords` | Extract Keywords |
| POST | `/chunks` | Generate Text Chunks |
| POST | `/embeddings` | Generate Sentence Embeddings |
| POST | `/faiss` | Create FAISS Index |
| POST | `/search` | Semantic Search |
| POST | `/chat` | RAG-based Question Answering |

---

###  Backend

- PDF Upload
- Text Extraction
- Summarization
- Named Entity Recognition
- Keyword Extraction
- Chunking
- Embeddings
- FAISS Indexing
- Semantic Search
- RAG Chatbot
- Result Caching

###  Frontend

- React + Vite UI
- Paper Dashboard
- Chat Interface
- Summary View
- Entity & Keyword Panels
- Modern Responsive Design

---

## 🔮 Future Enhancements

- Compare Multiple Research Papers
- Citation Finder
- Research Gap Detection
- Knowledge Graph Visualization
- Flashcard Generation
- Quiz Generation
- Export Notes
- Multi-Paper Chat
- User Authentication
- Cloud Deployment

---

## 📚 Sample Paper

The repository includes the paper **"Attention Is All You Need"** for demonstration and testing purposes.

---

## 👨‍💻 Author

Developed as an AI/NLP Research Assistant project using Flask, NLP, Semantic Search, FAISS, and Google Gemini.

---
