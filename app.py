from flask import Flask, render_template, request, jsonify

from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.risk_agent import RiskAgent
from agents.report_agent import ReportAgent

app = Flask(__name__)

# Initialize autonomous agents
research_agent = ResearchAgent()
analysis_agent = AnalysisAgent()
risk_agent = RiskAgent()
report_agent = ReportAgent()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "message": "Autonomous Financial Research Agent is running"
    })


@app.route("/research", methods=["POST"])
def research():
    try:
        data = request.get_json()

        company = data.get("company", "").strip()

        if not company:
            return jsonify({
                "success": False,
                "error": "Please enter a company name."
            }), 400

        # Agent 1: Research
        research_result = research_agent.research(company)

        # Agent 2: Financial Analysis
        analysis_result = analysis_agent.analyze(research_result)

        # Agent 3: Risk Assessment
        risk_result = risk_agent.assess(
            company,
            research_result,
            analysis_result
        )

        # Agent 4: Report Generation
        final_report = report_agent.generate(
            company,
            research_result,
            analysis_result,
            risk_result
        )

        return jsonify({
            "success": True,
            "company": company,
            "research": research_result,
            "analysis": analysis_result,
            "risk": risk_result,
            "report": final_report
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )