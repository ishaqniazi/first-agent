from agents import Agent , Runner , OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig, function_tool
from model_config import config

FastFood = Agent(
    name="Fast_food",
    instructions="You are a helpful assistant that help in cooking of fast food .",
)
HealthyFood= Agent(
    name="healthy_food",
    instructions="you are a helpful assistant which give healthy salad receipes"
)
agent = Agent(
    name="chief",
    instructions="you give recipies for health and juck food from the given agents",
    handoffs=[FastFood,HealthyFood]
)
result= Runner.run_sync(agent , input="give me a healthy recipe", run_config=config
)


print(result.final_output)
print("handoff =>>" , agent.handoffs)