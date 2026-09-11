class RiskAgent:
    """
    Agent responsible for identifying potential
    financial risks associated with a company.
    """

    def assess(self, company, financial_data, analysis):
        try:
            risks = []
            risk_level = "Low"

            pe_ratio = financial_data.get("pe_ratio")
            current_price = financial_data.get("current_price")
            high_52 = financial_data.get("52_week_high")
            low_52 = financial_data.get("52_week_low")

            # Check valuation risk
            if isinstance(pe_ratio, (int, float)):
                if pe_ratio > 40:
                    risks.append(
                        "High valuation risk due to elevated P/E ratio."
                    )
                    risk_level = "Medium"

            # Check price volatility
            if all(isinstance(x, (int, float))
                   for x in [current_price, high_52, low_52]):

                if high_52 > low_52:
                    price_range = ((high_52 - low_52) / low_52) * 100

                    if price_range > 50:
                        risks.append(
                            "Significant 52-week price variation detected."
                        )
                        risk_level = "Medium"

            # If no major risks were identified
            if not risks:
                risks.append(
                    "No major risk indicators detected from the available data."
                )

            return {
                "company": company,
                "risk_level": risk_level,
                "risk_factors": risks,
                "recommendation": self.generate_recommendation(risk_level)
            }

        except Exception as e:
            return {
                "company": company,
                "risk_level": "Unknown",
                "risk_factors": [str(e)],
                "recommendation": "Further analysis is required."
            }

    def generate_recommendation(self, risk_level):
        if risk_level == "Low":
            return "The available indicators suggest relatively lower financial risk."

        if risk_level == "Medium":
            return "Investors should perform additional research before making decisions."

        return "Detailed financial analysis is strongly recommended."