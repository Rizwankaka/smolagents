import os
import warnings
import streamlit as st
warnings.filterwarnings("ignore", message="Valid config keys have changed in V2")
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel
from dotenv import load_dotenv
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Agent Assistant",
    page_icon="🤖",
    layout="wide"
)

# Title and description
st.title("🤖 AI Agent Assistant")
st.markdown("Ask questions about stocks, weather, or any other information!")

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for API key
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    if api_key:
        os.environ['GEMINI_API_KEY'] = api_key

# Initialize the agent (only if API key is provided)
@st.cache_resource
def initialize_agent(api_key):
    model = LiteLLMModel(
        model_id="gemini/gemini-2.0-flash-exp",
        api_key=api_key
    )
    search_tool = DuckDuckGoSearchTool()
    return CodeAgent(
        tools=[search_tool], 
        model=model,
        additional_authorized_imports=["yfinance"]
    )

# Main chat interface
user_input = st.chat_input("Type your question here...")

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Process new messages
if user_input and api_key:
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # Get and display AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            agent = initialize_agent(api_key)
            try:
                response = agent.run(user_input)
                st.write(response)
                st.session_state.chat_history.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
elif user_input and not api_key:
    st.warning("Please enter your Gemini API key in the sidebar first.")