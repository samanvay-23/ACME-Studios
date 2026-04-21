import json
from datetime import datetime

def generate_report():
    report = {
        "generated_on": datetime.now().strftime("%Y-%m-%d"),
        "status": "success",
        "message": "Analytics report generated successfully"
    }

    with open("../analytics/report.json", "w") as f:
        json.dump(report, f, indent=2)

if __name__ == "__main__":
    generate_report()
