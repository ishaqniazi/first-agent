from agents import OpenAIChatCompletionsModel , AsyncOpenAI, RunConfig
from dotenv import load_dotenv
import os

_: bool = load_dotenv()
# gemini_api_key: str = os.getenv('GEMINI_API_KEY')for checking the environment variable
# print("GEMINI_API_KEY is set:", os.getenv

client = AsyncOpenAI(
    api_key= os.getenv('GEMINI_API_KEY'),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model='gemini-2.0-flash',
      openai_client=client,
      )

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True,
)