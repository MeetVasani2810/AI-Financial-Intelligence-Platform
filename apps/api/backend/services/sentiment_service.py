from transformers import pipeline


classifier = pipeline(
    "sentiment-analysis",
    model="ProsusAI/finbert",
    tokenizer="ProsusAI/finbert"
)
def analyze_sentiments(texts :list[str]):

    result=classifier(texts)
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

    prediction = classifier(text)[0]

    return {
        "sentiment": prediction["label"],
        "confidence": round(prediction["score"], 2)
    }

# print (analyze_sentiment("Apple missed earnings expectations"))