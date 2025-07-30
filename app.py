
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def show_report():
    try:
        with open("results/compliance_results.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"error": "Compliance results not found. Please run main.py first."}
    return render_template("report.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
