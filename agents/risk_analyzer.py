import os
import openai, json
from dotenv import load_dotenv
load_dotenv()
# from configs import settings

# openai.api_key = settings.openai_api_key

def run(business_model: dict) -> dict:
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # client = openai.OpenAI(api_key="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")
    prompt = f"""
You are a risk management consultant. Given this business model JSON, list the top 5 risks and for each, a mitigation strategy.  
Return:
{{
  "risks": [ {{ "risk": "...", "mitigation": "..." }}, … ]
}}
Only JSON.
Business model:
{json.dumps(business_model, indent=2)}
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


# def run(business_model: dict) -> dict:
#     # ask LLM to list top 5 risks and how to mitigate them
#     return { "risks": [...], "mitigations": [...] }
