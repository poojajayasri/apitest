from flask import Flask, jsonify, request, render_template
import os
from langchain import OpenAI, LLMMathChain
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.agents import AgentType
from langchain.agents import load_tools
from langchain.utilities.zapier import ZapierNLAWrapper

app = Flask(__name__)

# Set API keys as environment variables
os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "b43422edda2aac30c99f8515e9ea1cd1b68bce30e6d594c005afecaa8f7fb9a5"
os.environ["ZAPIER_NLA_API_KEY"] = "sk-ak-IkhGV8ctjuS3e9Mdsiy3YUYija"

# Initialize tools and agent
llm = OpenAI(temperature=0)
zapier = ZapierNLAWrapper()
toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
zapiertools = toolkit.get_tools()
tools = load_tools(["serpapi","llm-math"], llm=llm)
tools.extend(zapiertools)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Flask routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/answer")
def answer():
    query = request.args.get("query")
    answer = agent.run(query)
    return jsonify({"answer": answer})
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
