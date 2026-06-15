from utils import ask_sarvam
from prompts import build_financial_prompt


def generate_answer(query, data_context):

    prompt = build_financial_prompt(query, data_context)

    return ask_sarvam(prompt)