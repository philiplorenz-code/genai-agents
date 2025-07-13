import asyncio
from typing import Any, Annotated

from genai_session.session import GenAISession

session = GenAISession(
    jwt_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjYzRiM2Q2NC00YWU3LTRhNjUtYTllMC00ZjEzYWNjYmM0OGIiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6ImFlOWEzZDM3LThmNWMtNGMzZS1iNjIwLWQ3YzVkZDk2MzBjYiJ9.mjkCZH7Ch_AQcLVFvNvek1D5CAqzHVErOhp-LfRANkc"
)


@session.bind(name="read_txt_file", description="Get content from the txt file")
async def read_text_file(
        agent_context,
        file_id: Annotated[str, "ID of the file to read"]
) -> dict[str, Any]:
    file = await agent_context.files.get_by_id(file_id)
    file_content = file.read().decode("utf-8")
    return file_content


async def main():
    print(f"Agent with ID {session.jwt_token} started")
    await session.process_events()


if __name__ == "__main__":
    asyncio.run(main())
