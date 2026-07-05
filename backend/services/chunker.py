from services.ner import nlp


def create_chunks(text, chunk_size=4, overlap=1):
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]

    chunks = []
    chunk_id = 1

    i = 0

    while i < len(sentences):
        chunk_text = " ".join(sentences[i:i + chunk_size])

        chunks.append({
            "id": chunk_id,
            "text": chunk_text
        })

        chunk_id += 1
        i += chunk_size - overlap

    return chunks