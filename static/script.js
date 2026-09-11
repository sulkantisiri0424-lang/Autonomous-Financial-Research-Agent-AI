async function startResearch() {

    const companyInput = document.getElementById("company");
    const status = document.getElementById("status");

    const company = companyInput.value.trim();

    if (!company) {
        status.textContent = "Please enter a company or stock symbol.";
        return;
    }

    status.textContent = "Researching... Please wait.";

    try {

        const response = await fetch("/research", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                company: company
            })
        });

        const data = await response.json();

        if (!data.success) {
            status.textContent =
                "Error: " + (data.error || "Research failed.");
            return;
        }

        displayResults(data);

        status.textContent =
            "Research completed successfully.";

    } catch (error) {

        status.textContent =
            "Unable to connect to the research agent.";

        console.error(error);
    }
}


function displayResults(data) {

    const research = data.research;
    const analysis = data.analysis;
    const risk = data.risk;
    const report = data.report;


    // Company information
    document.getElementById("companyName").textContent =
        research.company_name || "-";

    document.getElementById("symbol").textContent =
        research.symbol || "-";

    document.getElementById("sector").textContent =
        research.sector || "-";

    document.getElementById("industry").textContent =
        research.industry || "-";


    // Financial analysis
    document.getElementById("valuation").textContent =
        analysis.valuation || "-";

    document.getElementById("price").textContent =
        research.current_price || "-";

    document.getElementById("marketSize").textContent =
        analysis.market_size || "-";


    // Risk assessment
    document.getElementById("riskLevel").textContent =
        risk.risk_level || "-";

    const riskList = document.getElementById("riskFactors");

    riskList.innerHTML = "";

    if (risk.risk_factors && risk.risk_factors.length > 0) {

        risk.risk_factors.forEach(function(factor) {

            const li = document.createElement("li");

            li.textContent = factor;

            riskList.appendChild(li);
        });

    } else {

        const li = document.createElement("li");

        li.textContent = "No risk information available.";

        riskList.appendChild(li);
    }


    document.getElementById("recommendation").textContent =
        risk.recommendation || "-";


    // Final report
    document.getElementById("summary").textContent =
        report.summary || "-";

    document.getElementById("conclusion").textContent =
        report.conclusion || "-";

    document.getElementById("disclaimer").textContent =
        report.disclaimer || "-";
}