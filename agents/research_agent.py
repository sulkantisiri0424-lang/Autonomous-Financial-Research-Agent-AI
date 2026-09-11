import yfinance as yf


class ResearchAgent:
    """
    Autonomous agent responsible for collecting
    basic financial information about a company.
    """

    def research(self, company):
        try:
            ticker = yf.Ticker(company)

            info = ticker.info

            financial_data = {
                "company_name": info.get("longName", company),
                "symbol": company.upper(),
                "sector": info.get("sector", "N/A"),
                "industry": info.get("industry", "N/A"),
                "current_price": info.get("currentPrice", "N/A"),
                "market_cap": info.get("marketCap", "N/A"),
                "pe_ratio": info.get("trailingPE", "N/A"),
                "52_week_high": info.get("fiftyTwoWeekHigh", "N/A"),
                "52_week_low": info.get("fiftyTwoWeekLow", "N/A"),
                "currency": info.get("currency", "N/A")
            }

            return financial_data

        except Exception as e:
            return {
                "company_name": company,
                "symbol": company.upper(),
                "error": str(e)
            }