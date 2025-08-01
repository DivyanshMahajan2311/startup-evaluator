import os
import openai
from dotenv import load_dotenv
load_dotenv()

def run(idea_text: str) -> dict:
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # client = openai.OpenAI(api_key="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")
    prompt = f"Validate if this startup idea solves a real problem: {idea_text}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a startup idea validator."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=256
    )
    return response.choices[0].message.content




# import os
# import openai
# # from configs import settings

# def run(idea_text: str) -> dict:
#     openai.api_key = os.getenv("OPENAI_API_KEY")
#     # openai.api_key = settings.openai_api_key
#     prompt = f"Validate if this startup idea solves a real problem: {idea_text}"
#     resp = openai.ChatCompletion.create( ... )
#     return resp.choices[0].message.content
