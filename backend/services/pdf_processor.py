import fitz
import os

DOCUMENT_FOLDER = os.path.join(os.getcwd(), "documents")
os.makedirs(DOCUMENT_FOLDER, exist_ok=True)


def extract_text(pdf_path):
    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


def save_text(filename, text):
    txt_filename = os.path.splitext(filename)[0] + ".txt"

    txt_path = os.path.join(DOCUMENT_FOLDER, txt_filename)

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)

    return txt_path


def load_text(filename):

    txt_filename = os.path.splitext(filename)[0] + ".txt"

    txt_path = os.path.join(DOCUMENT_FOLDER, txt_filename)

    with open(txt_path, "r", encoding="utf-8") as f:
        return f.read()