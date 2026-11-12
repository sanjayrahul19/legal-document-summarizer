import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")


def extract_important_facts(text):

    doc = nlp(text)
    
    facts = {
        "people": [],
        "organizations": [],
        "dates": [],
        "amounts": [],
        "obligations": []
    }

    # Extract named entities
    for entity in doc.ents:

        if entity.label_ == "PERSON":
            facts["people"].append(entity.text)

        elif entity.label_ == "ORG":
            facts["organizations"].append(entity.text)

        elif entity.label_ == "DATE":
            facts["dates"].append(entity.text)

        elif entity.label_ == "MONEY":
            facts["amounts"].append(entity.text)

    # Extract sentences that may contain obligations
    obligation_keywords = [
    "shall",
    "must",
    "will",
    "may",
    "required to",
    "agrees to",
    "undertakes to"
]

    for sentence in doc.sents:

        sentence_text = sentence.text

        if any(
            keyword in sentence_text.lower()
            for keyword in obligation_keywords
        ):
            facts["obligations"].append(sentence_text)

    return facts