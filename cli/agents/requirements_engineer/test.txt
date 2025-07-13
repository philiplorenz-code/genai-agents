import asyncio
import json
import os
from typing import Annotated, Dict

from dotenv import load_dotenv
from openai import AsyncOpenAI
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext

# Load environment variables from .env
load_dotenv()
print("OpenAI key:", os.getenv("OPENAI_API_KEY"))
print("🔑 OPENAI_API_KEY loaded:", os.getenv("OPENAI_API_KEY") is not None)

# Set up GenAI agent session
AGENT_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjYjE0ZmQ4ZS0zNWE5LTQzYWUtYTJjZi0yZWVjMTFjNWYxYjUiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6ImVmODk0NDRlLTQ2YWMtNDQ1ZC1iNDM0LWNjYTdlYzQ1MTUyMSJ9.YD2cTSc6bCLooYF_vfGyYZ4zcQiuL3gasw9RwMh2Uhw"  # replace with your actual token
session = GenAISession(jwt_token=AGENT_JWT)

# Instantiate OpenAI client
openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@session.bind(
    name="requirements_engineer",
    description="Transforms vague goals into structured requirements for downstream agents."
)
async def requirements_engineer(
    agent_context: GenAIContext,
    user_request: Annotated[str, "A vague goal like 'Build me a chatbot that helps schedule meetings.'"],
) -> Dict:
    print("📩 Received user request:", user_request)

    prompt = f"""
You are a Requirements Engineer AI. Your task is to extract and structure requirements from a user's message.

Instructions:
- Understand the business need.
- Identify objectives, constraints, stakeholders, and target outputs.
- If anything is missing, suggest follow-up questions in the field "follow_up_questions".
-Please **do not** wrap your response in triple backticks (```) or markdown code blocks.


Output format (JSON):
{{
  "objective": "...",
  "constraints": ["..."],
  "stakeholders": ["..."],
  "preferred_output_format": "...",
  "follow_up_questions": ["..."]
}}

Now process the following input:

{user_request}
"""

    try:
        print("🧠 Calling OpenAI directly via AsyncOpenAI...")

        response = await openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a Requirements Engineer AI."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=800
        )

        raw_output = response.choices[0].message.content
        print("✅ LLM response received.")
        print("📦 Raw output:", raw_output)
        return _postprocess_llm_output(raw_output)

    except Exception as e:
        print("❌ Error calling OpenAI:", str(e))
        import traceback
        traceback.print_exc()
        return {"error": str(e)}


def _postprocess_llm_output(raw_output: str) -> Dict:
    try:
        # Remove markdown code block if present
        if raw_output.strip().startswith("```json"):
            raw_output = raw_output.strip().removeprefix("```json").removesuffix("```").strip()
        elif raw_output.strip().startswith("```"):
            raw_output = raw_output.strip().removeprefix("```").removesuffix("```").strip()

        return json.loads(raw_output)
    except json.JSONDecodeError:
        print("⚠️ JSON decoding failed. Trying fallback extraction...")
        try:
            start = raw_output.find('{')
            end = raw_output.rfind('}')
            json_str = raw_output[start:end + 1]
            return json.loads(json_str)
        except Exception as e:
            print("❌ Fallback JSON extraction also failed.")
            print("Raw output:", raw_output)
            print("Error:", str(e))
            return {
                "error": "Could not parse model output as JSON",
                "raw_output": raw_output
            }


async def main():
    print(f"🚀 Requirements Engineer Agent running with token: {AGENT_JWT[:10]}...")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
