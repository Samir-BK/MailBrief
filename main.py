from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import openai

app = Flask(__name__)

load_dotenv()
client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)



@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ask", methods = ["POST"])
def ask():
    query = request.form.get("question")

    response = client.responses.create(
        model = "openai/gpt-oss-20b",
        input = [
            {
                "role": "system", "content": "Act like a helpful personal assistant"
            },
            {
                "role": "user", "content": query
            }
        ],
        temperature = 0.7,
        max_output_tokens = 512
        )
    answer = response.output_text.strip()
    return jsonify({"response": answer}), 200

@app.route("/summarize", methods = ["POST"])
def summarize():
    email = request.form.get("email")
    prompt = f"Summarize the following email in 6-7 sentences: {email}"
    response = client.responses.create(
        model = "openai/gpt-oss-20b",
        input = [
            {
                "role": "system", "content": "Act like a professional email assistant"
            },
            {
                "role": "user", "content": prompt
            }
        ],
        temperature = 0.6,
        max_output_tokens = 512
    )
    summary = response.output_text.strip()
    return jsonify({"response": summary}), 200

if __name__ == "__main__":
    app.run(debug=True)
