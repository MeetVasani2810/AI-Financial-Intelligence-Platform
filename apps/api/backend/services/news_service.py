import yfinance as yf
from services.sentiment_service import analyze_sentiment

def get_news(symbol : str):
    stock = yf.Ticker(symbol)
    news_list = []
    
    for news in stock.news:

        content = news.get("content",{})
    
        provider = content.get("provider",{})

        title = content.get("title", "N/A")


        sentiment=analyze_sentiment(title)


        news_list.append({
            "title" : title,

            "publisher": provider.get("displayName","N/A"),

            "published_date": content.get("pubDate","N/A"),

            **sentiment
        })
    return news_list

# print(get_news("AAPL"))