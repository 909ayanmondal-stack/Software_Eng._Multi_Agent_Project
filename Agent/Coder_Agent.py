from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain_openai import ChatOpenAI
from config import LLM_PROVIDER

# Select LLM
if LLM_PROVIDER == "ollama":
    llm = OllamaLLM(model="qwen3:8b",temperature=0)
else:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Prompt
prompt = PromptTemplate(
    template="""
You are an expert software developer.

Previous conversation:
{history}

Current Task:
{task}

IMPORTANT INSTRUCTIONS:
- Write code in the most appropriate programming language.
- If no language is specified, choose the BEST language.
- Output ONLY code.
- Do NOT add explanations or comments.
- Ensure code is complete and runnable.
""",
    input_variables=["history", "task"]
)

# Chain
chain = prompt | llm

# Memory
memory = {}

def coder(task: str, thread_id: str = "default") -> dict:
    history = memory.get(thread_id, "")

    result = chain.invoke({
        "history": history,
        "task": task
    })

    # handle both OpenAI + Ollama
    output = result.content if hasattr(result, "content") else result

    memory[thread_id] = f"""
{history}

Task:
{task}

Code:
{output}
"""

    return {
        "status": "coding",
        "code": output
    }

# just for testing  bro
if __name__ == "__main__":
    print(coder(task="Create a User model in Python"))
    