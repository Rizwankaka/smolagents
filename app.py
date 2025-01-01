from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from smolagents.agents import ToolCallingAgent
from smolagents import tool, TransformersModel, LiteLLMModel
from typing import Optional
import os 
from dotenv import load_dotenv
load_dotenv()

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


# Initialize the model
model = LiteLLMModel(
    model_id="gemini/gemini-2.0-flash-exp",
    api_key=os.getenv('GEMINI_API_KEY')
)

# Create the search tool object
search_tool = DuckDuckGoSearchTool()

# Create the agent with the tool object and additional imports
agent = CodeAgent(
    tools=[search_tool], 
    model=model,
    additional_authorized_imports=["yfinance"]  # Move this parameter here
)

agent.run("Fetch the APPL stock price. Use YFinance library.")