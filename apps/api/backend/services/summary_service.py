def generate_summary(news_data):

    positive = 0
    negative = 0
    neutral = 0

    # Count sentiments
    for article in news_data:

        sentiment = article.get("sentiment", "neutral").lower()

        if sentiment == "positive":
            positive += 1

        elif sentiment == "negative":
            negative += 1

        else:
            neutral += 1

    total = positive + negative + neutral

    # Edge case: no news
    if total == 0:
        return {
            "overall_sentiment": "Unavailable",
            "confidence": 0,
            "summary": "No recent news articles were available for analysis."
        }

    max_count = max(positive, negative, neutral)

    # Determine dominant sentiment
    if max_count == positive:
        overall_sentiment = "Positive"
        summary = (
            "Recent market coverage is generally positive. "
            "Most articles indicate favorable developments with limited negative news."
        )

    elif max_count == negative:
        overall_sentiment = "Negative"
        summary = (
            "Recent market coverage appears negative. "
            "Several articles highlight concerns or unfavorable developments."
        )

    else:
        overall_sentiment = "Neutral"
        summary = (
            "Recent market coverage is mixed and largely neutral. "
            "No strong positive or negative trend dominates the news."
        )

    confidence = round((max_count / total) * 100, 2)

    return {
        "overallsentiment": overall_sentiment,
        "confidence": confidence,
        "summary": summary
    }

# sample_news = [
#     {
#         "title": "Apple launches new AI product",
#         "sentiment": "positive"
#     },
#     {
#         "title": "Apple revenue beats expectations",
#         "sentiment": "positive"
#     },
#     {
#         "title": "Supply chain concerns remain",
#         "sentiment": "negative"
#     }
# ]

# print(generate_summary(sample_news))