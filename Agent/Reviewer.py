from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain_openai import ChatOpenAI
from config import LLM_PROVIDER  
import ast

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
You are a senior software engineer and code reviewer.

Context:
{history}

Code to review:
{code}

Review the code for:
- Bugs
- Logic errors
- Performance issues
- Readability
- Maintainability
- Best practices

If issues exist:
- Explain the issue briefly.
- Suggest a fix.

If no issues are found, respond exactly:
Code looks good.

Output ONLY the review.
""",
    input_variables=["history", "code"]
)

# Chain
chain = prompt | llm

# Memory
memory = {}

# Syntax checker
def check_syntax(code: str) -> dict:
    try:
        ast.parse(code)
        return {
            "valid": True,
            "error": None
        }
    except SyntaxError as e:
        return {
            "valid": False,
            "error": str(e)
        }

# Reviewer
def reviewer(code: str, thread_id: str = "default") -> dict:

    # Check syntax first
    syntax_result = check_syntax(code)

    if not syntax_result["valid"]:
        return {
            "status": "syntax_error",
            "review": f"Syntax Error: {syntax_result['error']}"
        }

    # Get memory
    history = memory.get(thread_id, "")
    history = history[-2000:]  # limit history size

    # LLM review
    try:
        result = chain.invoke({
            "history": history,
            "code": code
        })

        output = (
            result.content
            if hasattr(result, "content")
            else result
        )

    except Exception as e:
        return {
            "status": "error",
            "review": str(e)
        }

    # Save memory
    memory[thread_id] = f"""
{history}

Code:
{code}

Review:
{output}
"""

    memory[thread_id] = memory[thread_id][-5000:]

    return {
        "status": "success",
        "review": output
    }

#just for testing bro
if __name__ == "__main__":
    print(reviewer("def add(a,b): return a+b"))