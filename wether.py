from agents import Runner, ItemHelpers , function_tool , Agent , RunConfig , AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from model_config import config


@function_tool(
        name_override="Mosam_update",
        description_override="filhal current mosam ka haal batadain"
)
async def fetch_weather(location:str) -> str:
    """fetch the weather for a given location.
    Args:
        city (str): The location to fetch the weather for.
        """
    print("location", location)
    return f"sunny (location)"
    # return "sunny"
agent = Agent(
        name="Weather Assistant",
        instructions="You are a helpful assistant that provides weather information.",
        tools=[fetch_weather],
    )

result = Runner.run_sync(agent, input=input("which city "), run_config=config)
print(result.final_output)
