from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from Agent.Planner_Agent import planner
from Agent.Coder_Agent import coder
from Agent.Reviewer import reviewer
from Agent.Executor_Agent import executor

from config import ROOT_MODEL


def casual_chat(message: str) -> str:
    """
    Use ONLY for greetings, small talk, introductions,
    and general conversation.
    """
    return f"Hey! {message}"


root_agent = Agent(
    model=LiteLlm(model=ROOT_MODEL),

    name="Root_Agent",

    description="Software engineering orchestrator.",

    instruction="""
You are Ayan's AI assistant.

FIRST classify the user's message.

CATEGORY 1: Casual conversation
Examples:
- hi
- hello
- hey
- what's up
- how are you
- who are you
- what can you do

Action:
Call casual_chat.

CATEGORY 2: Software engineering tasks
Examples:
- build a login system
- create an API
- design a database
- review code
- execute code

Action:
Use the appropriate tool.

Tool Selection:

Requirement / Design
→ planner

Code Generation
→ coder

Code Review
→ reviewer

Code Execution
→ executor

End-to-End Request:
planner
→ coder
→ reviewer
→ executor

Never use planner for greetings.
Never use coder for greetings.
Never use reviewer for greetings.
Never use executor for greetings.
""",

    tools=[
        casual_chat,
        planner,
        coder,
        reviewer,
        executor,
    ],
)