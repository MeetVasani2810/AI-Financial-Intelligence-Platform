import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_ai_summary(
    company_name,
    overall_sentiment,
    confidence,
    news_list,
    price_intelligence
):

    headlines = ""

    for index, article in enumerate(news_list[:5], start=1):

        headlines += f"{index}. {article['title']}\n"

    # Extract ONCE (not inside loop)
    monthly_change = price_intelligence["monthly_change"]
    weekly_change = price_intelligence["weekly_change"]
    trend = price_intelligence["trend"]
    current_price = price_intelligence["current_price"]

    prompt = f"""
You are an experienced financial analyst.

Company Name: {company_name}

Current Stock Information:

Current Price: ${current_price}

Monthly Return: {monthly_change}%

Weekly Return: {weekly_change}%

Trend: {trend}

Market Sentiment:

Overall Sentiment: {overall_sentiment}

Confidence Score: {confidence}%

Recent News Headlines:

{headlines}

Your task:

1. Explain the current sentiment in simple language.
2. Connect the news with the stock's recent price performance.
3. Identify major themes appearing in the news.
4. Mention potential risks if explicitly mentioned.
5. Mention potential opportunities if explicitly mentioned.
6. Keep the response between 4 and 6 sentences.
7. Do NOT provide buy, sell, or hold recommendations.
8. Do NOT predict future stock prices.
9. Base your explanation only on the provided information.

Write for a retail investor with limited financial knowledge.
"""

    try:

        response = model.generate_content(prompt)

        return {
            "ai_summary": response.text
        }

    except Exception as e:

        print("Gemini Error:", e)

        return {
            "ai_summary": "Unable to generate AI summary at the moment."
        }