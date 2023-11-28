# app.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello mr. BigDickEnergy!"

if __name__ == "__main__":
    app.run(debug=True)
    