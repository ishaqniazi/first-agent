from agents import Agent,Runner,input_guardrail,RunContextWrapper,TResponseInputItem, GuardrailFunctionOutput
from model_config import config
async def math_guardrial(
    context :RunContextWrapper[None],agent :Agent , input :str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    user_type = "user"
    guardrail_instance = GuardrailFunctionOutput(
        output_info= "Guardrial is failed deu to user type",
        tripwire_triggered=True
    )

