import os
import openai
import json
from dotenv import load_dotenv
load_dotenv()
# from configs import settings

# openai.api_key = settings.openai_api_key

def run(validated_problem: str) -> dict:
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # client = openai.OpenAI(api_key="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")
    prompt = f"""
You are a market researcher. Given this validated problem statement, produce a JSON object with:
  - market_size: string (e.g. "$15B")
  - growth_rate: string (e.g. "8% per year")
  - top_competitors: [list of names]

Problem statement:
\"\"\"{validated_problem}\"\"\"
Respond with JSON and nothing else.
"""
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"system","content":"You are a helpful assistant."},
                  {"role":"user","content":prompt}],
        temperature=0.7,
    )
    text = resp.choices[0].message.content.strip()

    # Remove code fencing if present
    if text.startswith("```"):
        parts = text.split("```")
        if len(parts) >= 2:
            text = parts[1].strip()
    # Remove any leading non-JSON prefix
    brace_idx = text.find('{')
    if brace_idx > 0:
        text = text[brace_idx:]

    if not text:
        print("Error: Empty response from API.")
        return {}
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        print("Error: Response is not valid JSON.\nResponse was:", text)
        return {}




# import os
# import openai
# import json
# # from configs import settings

# # openai.api_key = settings.openai_api_key

# def run(validated_problem: str) -> dict:
#     client = openai.OpenAI(api_key="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")
#     prompt = f"""
# You are a market researcher. Given this validated problem statement, produce a JSON object with:
#   - market_size: string (e.g. "$15B")
#   - growth_rate: string (e.g. "8% per year")
#   - top_competitors: [list of names]

# Problem statement:
# \"\"\"{validated_problem}\"\"\"
# Respond with JSON and nothing else.
# """
#     resp = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role":"system","content":"You are a helpful assistant."},
#                   {"role":"user","content":prompt}],
#         temperature=0.7,
#     )
#     text = resp.choices[0].message.content.strip()
#     # return json.loads(text)
#     if text.startswith("```"):
#         text = text.split("```")[1].strip()
#     if not text:
#         print("Error: Empty response from API.")
#         return {}
#     try:
#         return json.loads(text)
#     except json.JSONDecodeError:
#         print("Error: Response is not valid JSON.\nResponse was:", text)
#         return {}




# def run(validated_problem: str) -> dict:
#     # e.g., use ChatGPT + web data scraping (or placeholder logic)
#     return {
#       "market_size": "...",
#       "competitors": ["A", "B"],
#       "growth_rate": "..."
#     }
