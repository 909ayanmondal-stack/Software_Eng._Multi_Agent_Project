from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain_openai import ChatOpenAI
from config import LLM_PROVIDER

# Select LLM
if LLM_PROVIDER == "ollama":
    llm = OllamaLLM(
        model="qwen3:8b",
        temperature=0
    )
else:
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

# Prompt
prompt = PromptTemplate(
    template="""
You are an expert software planning assistant.

Previous conversation:
{history}

Current requirement:
{requirement}

Your job is to break it down into a clear, numbered step-by-step development plan.
Each step should be short and actionable.

Return only the numbered plan, nothing else.
""",
    input_variables=["history", "requirement"]
)

# chain
chain = prompt | llm

# Simple in-memory storage
memory = {}


def planner(requirement: str, thread_id: str = "default") -> dict:
    """
    Takes a software requirement and returns a step-by-step plan.
    Remembers previous conversations for the same thread_id.
    """

    history = memory.get(thread_id, "")

    result = chain.invoke({
        "history": history,
        "requirement": requirement
    })

    # Handle both OpenAI and Ollama responses
    output = result.content if hasattr(result, "content") else result

    # Save conversation
    memory[thread_id] = f"""
{history}

User Requirement:
{requirement}

Generated Plan:
{output}
"""

    return {
        "status": "planning",
        "plan": output
    }


# for testing bro
if __name__ == "__main__":
    print(planner("Build a login system in Python"))