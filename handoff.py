from agents import Agent, Runner, AsyncOpenAI,RunConfig , OpenAIChatCompletionsModel , handoff, RunContextWrapper, HandoffInputData
external_client = AsyncOpenAI(
    api_key='GEMINI_API_KEY',
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

Nextjs_Agent = Agent(
    name="Next.js_Assistant",
    instructions="you are a helpful assistant that provide information about Next.js"
)

Python_Agent = Agent(
    name="Python_Assistant",
    instructions="you are a helpful assistant that provide information about Python"
)
#handoff function with array
# Triage_Agent = Agent(
#     name="Triage_Assistance",
#     instructions="you are a helpful assistant that Navigate between Next.js and Python",
#     handoffs=[Python_Agent,Nextjs_Agent]
# )

#handoff function with object work for facility to customize it (or agent is ok but we change it name from handoff in run time in one agent  )
#change name in hand off with the help of tool_name_override
Nextjs_handoff = handoff(
    agent = Nextjs_Agent,
    tool_name_override ="Next.js wala baba"
)
#input filter 

async def on_handoff(context: RunContextWrapper[None]):
    print("Handoff to Python Agent")

handoff_obj = handoff(
    agent=Nextjs_handoff,
    on_handoff=on_handoff
)
 
def handoff_input_function(inputData:HandoffInputData):

    return HandoffInputData(
        input_history=inputData.input_history,
        pre_handoff_items=inputData.pre_handoff_items,
        
    )

    
Triage_Agent = Agent(
    name="Triage_Assistance",
    instructions="you are a helpful assistant that Navigate between Next.js and Python",
    handoffs=[Nextjs_handoff,Python_Agent]
)

result = Runner.run_sync(handoff_obj, "I want to get help python decorator", run_config=config)#runcongig likhna hoga

# print("Final Output",result.final_output)

# print("current agent",result.last_agent.name)