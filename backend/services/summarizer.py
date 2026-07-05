from transformers import pipeline

MODEL_NAME = "sshleifer/distilbart-cnn-12-6"

summarizer = None


def get_summarizer():
    global summarizer

    if summarizer is None:
        print("Loading summarization model...")
        summarizer = pipeline(
            "summarization",
            model=MODEL_NAME
        )

    return summarizer


def summarize_text(text):

    model = get_summarizer()

    text = text[:4000]

    result = model(
        text,
        max_length=180,
        min_length=60,
        do_sample=False
    )

    return result[0]["summary_text"]