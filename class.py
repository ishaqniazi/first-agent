import os
from agents.tool import def
from agents import Agent, Runner, AsyncOpenAI, RunConfig, function_tool, OpenAIChatCompletionsModel, handoff, RunContextWrapper, HandoffInputData
import requests
from model_config import config


@function_tool()
def data (price: int):
    """
 Search for all products from https://dummyjson.com/products that match the given item
    and are priced less than or equal to the specified price.

    Return the result in one of the following formats:

    If one item is found:
    I found one {item} that is close to your specified price:

    *   **{Product Title}:** ${Product Price}

    If multiple items are found:
    I found {N} {item}s under your specified price:

    *   **{Product Title 1}:** ${Product Price 1}
    *   **{Product Title 2}:** ${Product Price 2}
    ...

    If no items are found:
    Sorry, no {item}s found under ${price}.
"""
    response = requests.get("https://dummyjson.com/products")
    products = response.json().get("products", [])
    return products if products else "No matching products found."


agent = Agent(
    name="searchData_agent",
    instructions="you are a helpful assistant that provide search url and return the result from the given tool.",
    tools=[data])

result = Runner.run_sync(
    agent,
    input=input("Enter the price and item to search: "),
    run_config=config)

print(result.final_output)