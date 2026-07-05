import spacy
from collections import defaultdict
from data.research_entities import (
    MODELS,
    DATASETS,
    FRAMEWORKS,
    METRICS,
    OPTIMIZERS,
    LOSS_FUNCTIONS,
)

# Load model once when Flask starts
nlp = spacy.load("en_core_web_sm")

def get_research_label(text):
    """
    Returns the research-specific label for an entity if found.
    """

    if text in MODELS:
        return "MODEL"

    if text in DATASETS:
        return "DATASET"

    if text in FRAMEWORKS:
        return "FRAMEWORK"

    if text in METRICS:
        return "METRIC"

    if text in OPTIMIZERS:
        return "OPTIMIZER"

    if text in LOSS_FUNCTIONS:
        return "LOSS_FUNCTION"

    return None

def extract_entities(text):
    """
    Extract named entities from text using spaCy.
    Returns a dictionary containing entity information.
    """

    doc = nlp(text)

    entities = []
    entity_summary = defaultdict(lambda: defaultdict(int))

    for ent in doc.ents:
        research_label = get_research_label(ent.text)

        entities.append({
            "text": ent.text,
            "label": ent.label_,
            "research_label": research_label,
            "start": ent.start_char,
            "end": ent.end_char,
            "sentence": ent.sent.text.strip()
        })
        entity_summary[ent.label_][ent.text] += 1

    entity_summary = {
        label: dict(values)
        for label, values in entity_summary.items()
    }
    
    return {
    "total_entities": len(entities),
    "entities": entities,
    "entity_summary": entity_summary
    }