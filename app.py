from flask import Flask, jsonify, request, render_template
import os
from langchain.llms import OpenAI

llm = OpenAI(model_name="text-ada-001", openai_api_key=openai_api_key)



app = Flask(__name__)

# Set API keys as environment variables
os.environ["OPENAI_API_KEY"] = "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"



# Flask routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/answer")
def answer():
    query = request.args.get("query")
    answer = llm(query)
    return jsonify({"answer": answer})
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
