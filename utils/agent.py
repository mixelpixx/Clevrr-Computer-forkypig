from langchain.agents import AgentExecutor, create_react_agent
from langchain_experimental.tools import PythonAstREPLTool
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import pyautogui as pg # type: ignore

_ = load_dotenv()
os.environ['OPENAI_API_TYPE'] = 'azure'

openai = AzureChatOpenAI(
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_deployment="gpt-4o",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

gemini = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro-latest",
    google_api_key="AIzaSyC8hyTcHxEEhRRmcQSynMoXqDNtc27Lme4",
)

models = {
    "gemini": gemini,
    "openai": openai
}

def create_clevrr_agent(model, prompt):
    print("============================================\nInitialising Clevrr Agent\n============================================")
    df_locals = {}
    df_locals["pg"] = pg
    tools = [PythonAstREPLTool(locals=df_locals)]
    agent = create_react_agent(model, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True, return_intermediate_steps=True)
    return agent_executor