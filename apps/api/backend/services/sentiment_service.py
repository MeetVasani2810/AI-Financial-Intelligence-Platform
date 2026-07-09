classifier = None

def get_classifier():
    global classifier
    if classifier is None:
        from transformers import pipeline
        classifier = pipeline(
            "sentiment-analysis",
            model="ProsusAI/finbert",
            tokenizer="ProsusAI/finbert"
        )
    return classifier
def analyze_sentiments(texts :list[str]):
    classifier_fn = get_classifier()
    result=classifier_fn(texts)
    clean_response = []

    for prediction in result:
        clean_response.append(
            {
                "sentiment":prediction["label"],
                "confidence":round(prediction["score"],2)
            }
        )
    return clean_response

def analyze_sentiment(text: str):
    classifier_fn = get_classifier()
    prediction = classifier_fn(text)[0]

    return {
        "sentiment": prediction["label"],
        "confidence": round(prediction["score"], 2)
    }

# print (analyze_sentiment("Apple missed earnings expectations"))