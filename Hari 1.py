Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from fastapi import FastAPI
... from typing import List, Dict
... import requests
... 
... app = FastAPI()
... 
... stock_data = {
...     "Dow Jones": {"price": 42635.20, "change": "+93.10", "change_percentage": "+0.22%"},
...     "Nasdaq Composite": {"price": 19478.88, "change": "+9.51", "change_percentage": "+0.05%"},
...     "S&P 500": {"price": 5918.25, "change": "+7.59", "change_percentage": "+0.13%"},
...     "S&P/TSX": {"price": 25073.40, "change": "+33.30", "change_percentage": "+0.13%"},
... }
... 
... global_market_report = {
...     "North America": {
...         "Dow Jones": {"price": 42635.20, "change": "+93.10", "change_percentage": "+0.22%"},
...         "Nasdaq Composite": {"price": 19478.88, "change": "+9.51", "change_percentage": "+0.05%"},
...         "S&P 500": {"price": 5918.25, "change": "+7.59", "change_percentage": "+0.13%"},
...         "S&P/TSX": {"price": 25073.40, "change": "+33.30", "change_percentage": "+0.13%"},
...     },
...     "Asia-Pacific": {
...         "Nikkei 225": {"price": 39377.70, "change": "-172.55", "change_percentage": "-0.44%"},
...         "KOSPI": {"price": 2520.21, "change": "-8.21", "change_percentage": "-0.32%"},
...         "Shanghai Index": {"price": 3204.57, "change": "-7.14", "change_percentage": "-0.22%"},
...         "CSI 1000": {"price": 5666.17, "change": "+3.40", "change_percentage": "+0.06%"},
        "Hang Seng": {"price": 19263.52, "change": "-64.55", "change_percentage": "-0.33%"},
    },
    "Europe": {
        "FTSE 100": {"price": 8319.70, "change": "+68.70", "change_percentage": "+0.83%"},
        "DAX": {"price": 20317.10, "change": "+32.90", "change_percentage": "+0.16%"},
        "CAC 40": {"price": 7490.28, "change": "+69.08", "change_percentage": "+0.93%"},
    }
}

major_futures = {
    "Dow Futures": {"price": 42635.20, "change": "+93.10", "change_percentage": "+0.22%"},
    "Nasdaq 100 Futures": {"price": 21180.97, "change": "+24.21", "change_percentage": "+0.11%"},
    "S&P 500 Futures": {"price": 5918.25, "change": "+7.59", "change_percentage": "+0.13%"},
    "US Dollar Index Futures": {"price": 109.18, "change": "-0.05", "change_percentage": "-0.05%"},
    "FTSE 100 Futures": {"price": 8312.0, "change": "-8.5", "change_percentage": "-0.1%"},
    "DAX Futures": {"price": 20443.0, "change": "-8.0", "change_percentage": "-0.04%"},
}

adr_and_gdr = {
    "Infosys ADR": {"price": 22.78, "change": "+0.19", "change_percentage": "+0.84%"},
    "Wipro ADR": {"price": 3.51, "change": "+0.04", "change_percentage": "+1.15%"},
    "HDFC Bank ADR": {"price": 60.38, "change": "-0.15", "change_percentage": "-0.25%"},
    "ICICI Bank ADR": {"price": 29.23, "change": "-0.12", "change_percentage": "-0.41%"},
    "Dr. Reddy's ADR": {"price": 15.81, "change": "+0.10", "change_percentage": "+0.64%"},
}

commodities_and_currencies = {
    "Precious Metals": {
        "Gold": {"price": 2697.60, "change": "+4.70", "change_percentage": "+0.17%"},
        "Silver": {"price": 31.16, "change": "+0.11", "change_percentage": "+0.37%"},
        "Platinum": {"price": 965.30, "change": "-19.50", "change_percentage": "-1.98%"},
    },
    "Energy": {
        "Brent Oil": {"price": 77.16, "change": "-0.05", "change_percentage": "-0.06%"},
        "Crude Oil WTI": {"price": 74.16, "change": "-0.13", "change_percentage": "-0.17%"},
        "Natural Gas": {"price": 3.72, "change": "+0.01", "change_percentage": "+0.22%"},
    },
    "Major Currencies": {
        "USD/INR": {"price": 85.87, "change": "-0.03", "change_percentage": "-0.03%"},
        "EUR/USD": {"price": 1.03, "change": "-0.00", "change_percentage": "-0.02%"},
        "USD/JPY": {"price": 158.26, "change": "+0.12", "change_percentage": "+0.08%"},
    },
    "Metals": {
        "Copper": {"price": 9021.90, "change": "+48.40", "change_percentage": "+0.54%"},
        "Aluminium": {"price": 2537.97, "change": "+47.67", "change_percentage": "+1.91%"},
        "Zinc": {"price": 2815.18, "change": "+22.71", "change_percentage": "+0.81%"},
        "Lead": {"price": 1912.87, "change": "-7.28", "change_percentage": "-0.38%"},
        "Nickel": {"price": 15278.04, "change": "+36.40", "change_percentage": "+0.24%"},
        "Tin": {"price": 29602.00, "change": "-256.99", "change_percentage": "-0.86%"},
    }
}

indian_markets = {
    "Major Indices": {
        "Nifty 50": {"price": 23526.50, "change": "-148.25", "change_percentage": "-0.63%"},
        "Sensex": {"price": 77620.21, "change": "-586.00", "change_percentage": "-0.75%"},
        "Nifty Bank": {"price": 49503.50, "change": "-209.05", "change_percentage": "-0.42%"},
        "India VIX": {"price": 14.66, "change": "+0.19", "change_percentage": "+1.33%"},
    },
    "Gift Nifty": {"price": 23584.5, "change": "-75.5", "change_percentage": "-0.32%"},
    "Sectors": {
        "IT Sector": {
            "Infosys ADR": {"price": 22.78, "change": "+0.19", "change_percentage": "+0.84%"},
            "Wipro ADR": {"price": 3.51, "change": "+0.04", "change_percentage": "+1.15%"},
        },
        "Metal Sector": {
            "Copper": {"price": 9021.90, "change": "+48.40", "change_percentage": "+0.54%"},
            "Aluminium": {"price": 2537.97, "change": "+47.67", "change_percentage": "+1.91%"},
            "Zinc": {"price": 2815.18, "change": "+22.71", "change_percentage": "+0.81%"},
            "Lead": {"price": 1912.87, "change": "-7.28", "change_percentage": "-0.38%"},
            "Nickel": {"price": 15278.04, "change": "+36.40", "change_percentage": "+0.24%"},
            "Tin": {"price": 29602.00, "change": "-256.99", "change_percentage": "-0.86%"},
        },
        "Energy Sector": {
            "Brent Oil": {"price": 77.16, "change": "-0.05", "change_percentage": "-0.06%"},
            "Natural Gas": {"price": 3.72, "change": "+0.01", "change_percentage": "+0.22%"},
        },
        "Banking Sector": {
            "HDFC Bank ADR": {"price": 60.38, "change": "-0.15", "change_percentage": "-0.25%"},
            "ICICI Bank ADR": {"price": 29.23, "change": "-0.12", "change_percentage": "-0.41%"},
        },
    }
}

def fetch_daily_market_news():
    news_api_url = "https://newsapi.org/v2/everything"
    params = {
        "q": "stock market",
        "apiKey": "ALPHA_VANTAGE_API_KEY",  
    }
    response = requests.get(news_api_url, params=params)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get("articles", [])
        return [article["title"] for article in articles]
    return ["Failed to fetch news"]

@app.get("/stocks", response_model=Dict[str, Dict[str, str]])
def get_stock_prices():
    """Retrieve current stock prices and their changes."""
    return stock_data

@app.get("/global-market-report", response_model=Dict[str, Dict[str, Dict[str, str]]])
def get_global_market_report():
    """Retrieve the global market performance report."""
    return global_market_report

@app.get("/major-futures", response_model=Dict[str, Dict[str, str]])
def get_major_futures():
    """Retrieve major futures data."""
    return major_futures

@app.get("/adr-gdr", response_model=Dict[str, Dict[str, str]])
def get_adr_and_gdr():
    """Retrieve ADR and GDR data."""
    return adr_and_gdr

@app.get("/commodities-and-currencies", response_model=Dict[str, Dict[str, Dict[str, str]]])
def get_commodities_and_currencies():
    """Retrieve commodities and currencies data."""
    return commodities_and_currencies

@app.get("/indian-markets", response_model=Dict[str, Dict])
