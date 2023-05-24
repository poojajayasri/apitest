from flask import Flask, jsonify, request, render_template
from langchain.llms import OpenAI
from flask_cors import CORS
import os
openai_api_key = os.environ.get('OPENAI_API_KEY')

llm = OpenAI(model_name="text-ada-001", openai_api_key=openai_api_key)



app = Flask(__name__)

# Flask routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/answer")
def answer():
    query = request.args.get("query")
    answer = llm(query)
    return jsonify({"answer": answer})

app = Flask(__name__)
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
