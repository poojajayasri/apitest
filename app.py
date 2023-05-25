from flask import Flask, jsonify, request, render_template
from langchain.llms import OpenAI
from flask_cors import CORS
import os

openai_api_key = os.environ["OPENAI_API_KEY"]
llm = OpenAI(model_name="text-ada-001", openai_api_key=openai_api_key)

app = Flask(__name__)
CORS(app)

# GET route
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# POST route
@app.route("/answer", methods=["POST"])
def answer():
    query = request.form.get("query")
    answer = llm(query)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(port=8000)
