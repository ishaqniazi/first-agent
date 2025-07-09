from agents import Agent , Runner , OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig, function_tool
from pydantic import BaseModel



external_client = AsyncOpenAI(
    api_key='AIzaSyDWs8mqnOtOiLjsqaJu59FhFv-9jvcbtX8',
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/" ,
)
external_model = OpenAIChatCompletionsModel(
    model = 'gemini-2.0-flash',
    openai_client=external_client
)

config = RunConfig(
    model= external_model,
    model_provider=external_client,
    tracing_disabled=True,
)
class wetherRequest(BaseModel):
    city :str
    wether : str
    temperature : float

agent = Agent(
    name="Weather Assistant",
    instructions="You are a helpful assistant that provides weather information.",
    model=external_model,
    output_type=wetherRequest,
)

result = Runner.run_sync(agent, input="what is the weather in karachi?", run_config=config)

print(result.final_output)
print("type of output", type(result.final_output))