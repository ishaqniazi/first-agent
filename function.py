from agents import Agent , Runner , OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig, function_tool
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