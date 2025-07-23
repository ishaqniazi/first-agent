import asyncio
import random
from agents import Runner, ItemHelpers , function_tool , Agent , RunConfig , AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from model_config import config
# from agents import Agent, Runner , RunConfig , AsyncOpenAI ,OpenAIChatCompletionsModel , set_tracing_disabled
# import asyncio
# from openai import AsyncOpenAI

# # client = AsyncOpenAI(
# #     api_key=gemini_api_key,
# #     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# # )

# # set_tracing_disabled(disabled=True)
# set_tracing_disabled(True)

# async def main():
#     # This agent will use the custom LLM provider
#     agent = Agent(
#         name="Assistant",
#         instructions="You only respond in 6 lines with out blank.",
#         model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
#     )

#     result = await Runner.run(
#         agent,
#         input=input()
#     )
#     print(result.final_output)


# if __name__ == "__main__":
#     asyncio.run(main())

# # assistance = Agent(
# #     name = 'bola assistant',
# #     instructions ='you are a helpful assistant that provide '
# # )

# # result = Runner.run(starting_agent=assistance,input=input(),run_config=config)

# # print(result.final_output)
# async def how_many_jokes():
#     return 3

@function_tool 
async def how_many_jokes():
    """Decides how many jokes to tell."""
    # Randomly decide to tell 1, 2, or 3 jokes
    return random.randint(1, 3)
# how_many_jokes = Tool(
#     name="how_many_jokes",
#     description="Decides how many jokes to tell.",
#     func=how_many_jokes,
# )


agent = Agent(
        name="Joke Teller",
        instructions="You are a helpful assistant. First, determine how many jokes to tell, then provide urdu pakistani jokes.",
        tools=[how_many_jokes],
    )

result = Runner.run_sync(agent, input="Tell me some jokes!", run_config=config)


print(result.final_output ,result.last_agent.tools )