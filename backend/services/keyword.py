from keybert import KeyBERT

kw_model = KeyBERT()

def extract_keywords(text, top_n=15):
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 4),
        stop_words="english",
        use_maxsum=True,
        nr_candidates=30,
        top_n=top_n
    )

    return [
        {
            "keyword": keyword,
            "score": round(float(score), 4)
        }
        for keyword, score in keywords
    ]