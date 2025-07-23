from agents import Agent, Runner, function_tool , enable_verbose_stdout_logging 
from openai.types.responses import ResponseTextDeltaEvent
from model_config import config
import asyncio
import random

# enable_verbose_stdout_logging()
@function_tool
async def fetch_weather(location)-> str:
    """ fetch weather for the given location and near by areas .
    Args:
    location : location for getting weather"""
    return f"weather in {location} is sunny"

async def main():
    weather_agent = Agent(
    name="weather_agent",
    instructions="You are a helpful assistant that provides location-based weather information.",
    tools=[fetch_weather],
    # tool_use_behavior="stop_on_first_tool"
    )
    result = Runner.run_streamed(
        weather_agent,
        "what is weather in karachi",
        run_config=config
    )
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data,ResponseTextDeltaEvent):
            print(event.data.delta, end="")
            # print ("[event_type]/n",event)
            # check event type
asyncio.run(main())