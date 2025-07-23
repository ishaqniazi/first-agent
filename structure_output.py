from agents import Agent , Runner , OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig, function_tool
from pydantic import BaseModel
from model_config import config

class wetherRequest(BaseModel):
    city :str
    wether : str
    temperature : float

agent = Agent(
    name="Weather Assistant",
    instructions="You are a helpful assistant that provides weather information.",
    output_type=wetherRequest,
)

result = Runner.run_sync(agent, input="what is the weather in karachi?", run_config=config)

print(result.final_output)
print("type of output", type(result.final_output))