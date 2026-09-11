class AnalysisAgent:
    """
    Agent responsible for analyzing financial data
    collected by the Research Agent.
    """

    def analyze(self, financial_data):
        try:
            current_price = financial_data.get("current_price")
            pe_ratio = financial_data.get("pe_ratio")
            market_cap = financial_data.get("market_cap")

            analysis = {
                "valuation": self.evaluate_valuation(pe_ratio),
                "price_status": self.evaluate_price(current_price),
                "market_size": self.evaluate_market_cap(market_cap),
                "overall_assessment": "Financial analysis completed successfully."
            }

            return analysis

        except Exception as e:
            return {
                "error": str(e)
            }

    def evaluate_valuation(self, pe_ratio):
        if pe_ratio == "N/A" or pe_ratio is None:
            return "P/E ratio information is not available."

        try:
            pe_ratio = float(pe_ratio)

            if pe_ratio < 15:
                return "Potentially undervalued based on P/E ratio."
            elif pe_ratio <= 30:
                return "P/E ratio is within a moderate range."
            else:
                return "Potentially highly valued based on P/E ratio."

        except (ValueError, TypeError):
            return "Unable to evaluate P/E ratio."

    def evaluate_price(self, current_price):
        if current_price == "N/A" or current_price is None:
            return "Current price information is not available."

        return f"Current market price: {current_price}"

    def evaluate_market_cap(self, market_cap):
        if market_cap == "N/A" or market_cap is None:
            return "Market capitalization information is not available."

        try:
            market_cap = float(market_cap)

            if market_cap >= 200_000_000_000:
                return "Large-cap company."
            elif market_cap >= 10_000_000_000:
                return "Mid-to-large-cap company."
            else:
                return "Small-to-mid-cap company."

        except (ValueError, TypeError):
            return "Unable to evaluate market capitalization."