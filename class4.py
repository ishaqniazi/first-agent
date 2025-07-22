from agents import Agent, Runner, function_tool , enable_verbose_stdout_logging
from model_config import config
import asyncio

enable_verbose_stdout_logging()
@function_tool
async def fetch_weather(location)-> str:
    """ fetch weather for the given location 
    Args:
    location : location for getting weather"""
    return f"weather in {location} is sunny"

weather_agent = Agent(
    name="weather_agent",
    instructions="You are a helpful assistant that provides answer by weather tool.",
    tools=[fetch_weather],
    tool_use_behavior="stop_on_first_tool"
)
async def main():
    result = await Runner.run(
        weather_agent,
        "what is weather in karachi",
        run_config=config
    )
    print("result>>>", result.final_output)
asyncio.run(main())