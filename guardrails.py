# from agents import Agent,Runner,input_guardrail,RunContextWrapper,TResponseInputItem, GuardrailFunctionOutput 
# from model_config import config
# async def math_guardrial(
#     context :RunContextWrapper[None],agent :Agent , input :str | list[TResponseInputItem]
# ) -> GuardrailFunctionOutput:
#     user_type = "user"
#     guardrail_instance = GuardrailFunctionOutput(
#         output_info= "Guardrial is failed deu to user type",
#         tripwire_triggered=True
#     )

from model_config import config, model
import asyncio
from agents import (
     Agent, 
     Runner, 
     set_tracing_disabled , 
     input_guardrail , 
     RunContextWrapper , 
     TResponseInputItem , 
     GuardrailFunctionOutput,
     InputGuardrailTripwireTriggered)
from pydantic import BaseModel
from openai.types.responses import ResponseTextDeltaEvent

set_tracing_disabled(disabled=True)

class InputGuardrails(BaseModel):
    related_to_Next_js : bool
    resoning : str

Gagent = Agent(
    name= "input_Gaurdirals",
    instructions="check if the input is related to Next.js if it is not then write false statment",
    model=model,
    output_type=InputGuardrails,
)

@input_guardrail
async def input_guard(
    ctx: RunContextWrapper,agent: Agent, input: str | list [TResponseInputItem]
) -> GuardrailFunctionOutput:
 result = await Runner.run(Gagent , input, context=ctx)
 return GuardrailFunctionOutput(output_info=result, tripwire_triggered=not result.final_output.related_to_Next_js)


main_agent = Agent(
        name = "Next.js Assistant",
        instructions = "you are a helpful assistance which helps with Next.js development.",
        model=model,
        input_guardrails=[input_guard]
        )
async def main():
    result = await Runner.run(main_agent, input="you will help customer according to guardrails help with Next.js", run_config=config)
    try:
       await Runner.run(main_agent, "tell me about javascript",)
       print("Guardrail didn't trip - this is unexpected")
       print(result.final_output)
    except InputGuardrailTripwireTriggered :
                print("Guardrail tripped as expected")
                print(result.final_output)         

asyncio.run(main())