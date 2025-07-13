import asyncio
from typing import Annotated,Optional,List,Dict
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext

AGENT_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI5ZDMzYzEzYS1lYzI2LTQ2ZjctOTJkZi0wOGNlNzE0NzY2ZTUiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6ImVmODk0NDRlLTQ2YWMtNDQ1ZC1iNDM0LWNjYTdlYzQ1MTUyMSJ9._3QvA1vsEjCpzT0x_9NaKByctNUJSPYsnRx0vdGV8lo" # noqa: E501
session = GenAISession(jwt_token=AGENT_JWT)

# Define a standard requirement schema
def format_requirements(goal: str, constraints: List[str], stakeholders: Dict[str, str]) -> Dict:
    return {
        "goal": goal,
        "constraints": constraints,
        "stakeholders": stakeholders,
    }

@session.bind(
    name="requirements_engineer",
    description="Acts as the translator between the user and the system. It transforms vague goals or requests into structured, machine-readable requirements for downstream agents."
)
async def requirements_engineer(
    agent_context: GenAIContext,
    user_request: Annotated[
        str,
        "A vague or loosely defined goal from the user, e.g., 'I want a task manager that works offline and syncs with Google Calendar.'",
    ],
):
    """Transforms vague user input into structured requirements."""
   # Step 1: Initial parsing (you can swap this with LLM call for better extraction later)
    goal = user_request.strip()
    
    # Simulated logic (you'll want to replace this with something LLM-backed)
    constraints = []
    stakeholders = {"user": "primary user"}
    if "offline" in user_request.lower():
        constraints.append("Must work without internet connectivity.")
    if "google calendar" in user_request.lower():
        constraints.append("Should integrate with Google Calendar.")
        
    # Step 2: Check for missing or ambiguous elements
    missing_info = []
    if not constraints:
        missing_info.append("No technical constraints identified.")
    if not goal:
        missing_info.append("Goal is unclear or missing.")
    
    # Step 3: Format final requirement
    structured_output = {
        "requirements": format_requirements(goal, constraints, stakeholders),
        "missing_info": missing_info
    }
    
    return structured_output

    


async def main():
    print(f"Requirements Engineer Agent started with token: {AGENT_JWT}")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
