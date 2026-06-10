import yfinance as yf


def get_price_intelligence(symbol: str):

    stock = yf.Ticker(symbol)

    history = stock.history(period="1mo")

    # No data returned
    if history.empty:
        return {
            "current_price": 0,
            "weekly_change": 0,
            "monthly_change": 0,
            "trend": "Unavailable"
        }

    # Remove NaN values from Close column
    close_prices = history["Close"].dropna()

    # Safety check
    if len(close_prices) < 5:
        return {
            "current_price": 0,
            "weekly_change": 0,
            "monthly_change": 0,
            "trend": "Unavailable"
        }

    current_price = float(round(close_prices.iloc[-1], 2))

    week_start_price = float(close_prices.iloc[-5])

    month_start_price = float(close_prices.iloc[0])

    weekly_change = float(
        round(
            ((current_price - week_start_price) / week_start_price) * 100,
            2
        )
    )

    monthly_change = float(
        round(
            ((current_price - month_start_price) / month_start_price) * 100,
            2
        )
    )

    if monthly_change > 5:
        trend = "Bullish"

    elif monthly_change < -5:
        trend = "Bearish"

    else:
        trend = "Sideways"

    return {
        "current_price": current_price,
        "weekly_change": weekly_change,
        "monthly_change": monthly_change,
        "trend": trend
    }


if __name__ == "__main__":
    print(get_price_intelligence("AAPL"))