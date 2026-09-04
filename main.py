from flask import Flask, render_template
import os
from dotenv import load_dotenv
app = Flask(__name__)

load_dotenv()
api_key  = os.getenv("GROQ_API_KEEY")

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ask")
def ask():
    return "<p></p>"

@app.route("/summarize")
def summarize():
    return "<p></p>"

if __name__ == "__main__":
    app.run(debug=True)
