import asyncio
from typing import Annotated, Literal
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext

AGENT_JWT = "REPLACE_WITH_YOUR_TOKEN"
session = GenAISession(jwt_token=AGENT_JWT)


@session.bind(name="argumentation_input_agent", description="Captures project brief and preferences")
async def input_agent(
    ctx: GenAIContext,
    project_idea: Annotated[str, "Describe the IT project idea."],
    required_depth: Annotated[Literal["basic", "intermediate", "deep"], "Level of detail required."],
    output_format: Annotated[Literal["markdown", "typset", "slides"], "Preferred output format."]
):
    return {
        "project_idea": project_idea,
        "required_depth": required_depth,
        "output_format": output_format
    }


@session.bind(name="argumentation_parser_agent", description="Parses objectives and perspectives")
async def parser_agent(
    ctx: GenAIContext,
    project_idea: Annotated[str, "Project idea to parse."],
):
    objectives = ["Objective A", "Objective B"]
    perspectives = ["Stakeholder 1", "Stakeholder 2"]
    return {"objectives": objectives, "perspectives": perspectives}


@session.bind(name="argumentation_pro_con_agent", description="Develops key arguments")
async def pro_con_agent(
    ctx: GenAIContext,
    objectives: Annotated[list, "List of project objectives."],
):
    pros = [{"objective": obj, "pro": f"Benefit of {obj}"} for obj in objectives]
    cons = [{"objective": obj, "con": f"Risk of {obj}"} for obj in objectives]
    return {"pros": pros, "cons": cons}


@session.bind(name="argumentation_stats_agent", description="Pulls public metrics")
async def stats_agent(
    ctx: GenAIContext,
    keyword: Annotated[str, "Keyword or sector for market stats."],
):
    return {"market_size": "10B USD", "trend": "Growing", "benchmarks": "Standard XYZ"}


@session.bind(name="argumentation_evaluator_agent", description="Evaluates ROI, effort, and fit")
async def evaluator_agent(
    ctx: GenAIContext,
    pros_cons: Annotated[dict, "Pros and cons dictionary."],
):
    return {
        "ROI": "Moderate",
        "Effort": "High",
        "Strategic Fit": "Aligned"
    }


@session.bind(name="argumentation_formatter_agent", description="Formats the final output")
async def formatter_agent(
    ctx: GenAIContext,
    structured_data: Annotated[dict, "Full structured argumentation data."],
    format_type: Annotated[Literal["markdown", "typset", "slides"], "Format to output."]
):
    return f"Formatted {format_type} document with data: {structured_data}"


async def main():
    print("Collaborative Argumentation Framework Agent started")
    await session.process_events()


if __name__ == "__main__":
    asyncio.run(main())