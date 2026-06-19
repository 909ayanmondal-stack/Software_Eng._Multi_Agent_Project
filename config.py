LLM_PROVIDER = "openai"
if LLM_PROVIDER == "ollama":
    ROOT_MODEL = "ollama/qwen3:8b"
else:
    ROOT_MODEL = "gpt-4o-mini"
    
