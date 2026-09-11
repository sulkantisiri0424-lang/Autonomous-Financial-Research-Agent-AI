class ReportAgent:
    """
    Agent responsible for combining research,
    financial analysis, and risk assessment into
    a final research report.
    """

    def generate(
        self,
        company,
        research_data,
        analysis_data,
        risk_data
    ):
        try:
            report = {
                "title": f"Financial Research Report - {company}",
                "company": company,
                "summary": self.create_summary(research_data),
                "financial_analysis": analysis_data,
                "risk_assessment": risk_data,
                "conclusion": self.create_conclusion(
                    analysis_data,
                    risk_data
                ),
                "disclaimer": (
                    "This report is for educational and research "
                    "purposes only and should not be considered "
                    "financial advice."
                )
            }

            return report

        except Exception as e:
            return {
                "error": str(e)
            }

    def create_summary(self, research_data):
        company_name = research_data.get(
            "company_name",
            "Unknown Company"
        )

        sector = research_data.get(
            "sector",
            "N/A"
        )

        industry = research_data.get(
            "industry",
            "N/A"
        )

        return (
            f"{company_name} operates in the "
            f"{sector} sector and {industry} industry. "
            f"The available financial information was "
            f"collected and analyzed by the autonomous "
            f"financial research agents."
        )

    def create_conclusion(
        self,
        analysis_data,
        risk_data
    ):
        valuation = analysis_data.get(
            "valuation",
            "Not available"
        )

        risk_level = risk_data.get(
            "risk_level",
            "Unknown"
        )

        return (
            f"Overall assessment: {valuation} "
            f"Risk level: {risk_level}. "
            "Users should perform additional research "
            "and consult qualified financial professionals "
            "before making investment decisions."
        )