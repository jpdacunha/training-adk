import os

from google.genai import types
from google.adk.agents import LlmAgent
from google.adk.models import Gemini
from google.adk.code_executors.agent_engine_sandbox_code_executor import (
    AgentEngineSandboxCodeExecutor,
)

RETRY_OPTIONS = types.HttpRetryOptions(initial_delay=1, max_delay=3, attempts=30)

sandbox_resource_name = os.environ.get("SANDBOX_RESOURCE_NAME")
assert sandbox_resource_name, (
    "SANDBOX_RESOURCE_NAME is not set. "
    "Complete Task 2: 'Add the sandbox resource name to .env' before running adk web."
)

root_agent = LlmAgent(
    model=Gemini(model=os.getenv("MODEL"), retry_options=RETRY_OPTIONS),
    name="cymbal_analyst",
    description="Financial analyst agent for Cymbal Analytics",
    instruction="""You are a financial analyst at Cymbal Analytics.
    When asked to analyze data, create charts or visualizations, or perform calculations, you MUST write clean Python code in a Python code block.
    The sandbox environment already has portfolio price data pre-loaded as a pandas DataFrame named df. The DataFrame index is dates. Columns are stock tickers ('GOOGL', 'MSFT', 'AMZN') with daily closing prices.
    Always use df directly for portfolio computations without recreating it.
    Always interpret the code execution output for the user after showing the numbers.""",
    code_executor=AgentEngineSandboxCodeExecutor(
        # Use of env variable provided by .env file
        sandbox_resource_name=sandbox_resource_name,
    ),
)
