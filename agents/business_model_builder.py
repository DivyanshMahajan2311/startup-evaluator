import os
import openai, json
from dotenv import load_dotenv
load_dotenv()
# from configs import settings

# openai.api_key = settings.openai_api_key

def run(market_data: dict) -> dict:
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # client = openai.OpenAI(api_key="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")
    prompt = f"""
You are a business model expert. Based on this market data JSON, create a business model JSON with:
  - revenue_streams: [ ... ]
  - cost_structure: [ ... ]
  - customer_segments: [ ... ]

Market data:
{json.dumps(market_data, indent=2)}
Respond with JSON only.
"""
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role":"system","content":"You are a helpful assistant."},
          {"role":"user","content":prompt}
        ],
        temperature=0.7,
    )
    return json.loads(resp.choices[0].message.content)




# def run(market_data: dict) -> dict:
#     # feed market_data into LLM to sketch out a business model canvas
#     return { "revenue_streams": [...], "cost_structure": [...] }
