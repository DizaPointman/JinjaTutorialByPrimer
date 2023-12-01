# app.py

from flask import Flask, render_template

app = Flask(__name__)

max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine", "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
    {"name": "Franz", "score": 69},
    {"name": "Schmebulock", "score": 42},
    {"name": "Schmebulock", "score": 19}
]

@app.route("/")
def home():
    return render_template("base.html", title="Jinja and Flask")

@app.route("/results")
def results():
    context = {
        "title": "Results",
        "students": students,
        "test_name": test_name,
        "max_score": max_score
    }
    return render_template("results.html", **context)

# **context -> unpack context including keywords: {"name": "Sandrine", "score": 100}
# With the asterisk operators, you’re passing the items of context as keyword arguments into render_template()
# https://stackoverflow.com/questions/69527239/what-is-context-variable-in-airflow-operators

if __name__ == "__main__":
    app.run(debug=True)
        