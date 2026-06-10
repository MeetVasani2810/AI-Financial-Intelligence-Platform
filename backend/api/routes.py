from fastapi import APIRouter

from services.stock_services import get_stock_data
from services.news_service import get_news
from services.summary_service import generate_summary
from services.ai_summary_service import generate_ai_summary
from services.price_intelligencelayer import get_price_intelligence

router = APIRouter()


@router.get("/stock/{symbol}")
def get_stock(symbol: str):

    stock_data = get_stock_data(symbol)

    stock_news = get_news(symbol)

    summary_data = generate_summary(stock_news)

    overall_sentiment = summary_data["overallsentiment"]
    confidence = summary_data["confidence"]

    company_name = stock_data["name"]

    price_intelligence = get_price_intelligence(symbol)

    ai_summary = generate_ai_summary(
        company_name,
        overall_sentiment,
        confidence,
        stock_news,
        price_intelligence
    )

    return {
        "symbol": symbol,
        "stock_data": stock_data,
        "market_summary": ai_summary,
        "price_intelligence": price_intelligence
    }