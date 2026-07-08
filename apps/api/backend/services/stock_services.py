import yfinance as yf

def get_stock_data(symbol:str):

    stock = yf.Ticker(symbol)

    return {

        "name":stock.info.get("longName","N/A"),
        "market_cap":stock.info.get("marketCap","N/A"),
        "pe_ratio":stock.info.get("trailingPE","N/A"),
        "current_price":stock.info.get("currentPrice","N/A")

    }

# print(get_stock_data("AAPL"))