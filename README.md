# 🤖 Software Engineering Multi-Agent System

An AI-powered software engineering assistant that takes a requirement and automatically plans, writes, reviews, and executes code — using a multi-agent architecture powered by Google ADK, LangChain, and Ollama.

---

## 🧠 Architecture

The system follows a **hub-and-spoke model** where the Root Agent orchestrates 4 specialized sub-agents:

```
User Request
      ↓
 Root Agent (Google ADK + LiteLLM)
      ↓
  ┌───┴────────────────────────┐
  ↓          ↓         ↓       ↓
Planner   Coder   Reviewer  Executor
  ↓          ↓         ↓       ↓
 Plan      Code     Review  Output
```

| Agent | Role | Description |
|---|---|---|
| **Root Agent** | Orchestrator | Reads user input, decides which agent(s) to call |
| **Planner Agent** | Task Planner | Breaks requirements into numbered step-by-step plans |
| **Coder Agent** | Code Writer | Writes code for each step of the plan |
| **Reviewer Agent** | Code Reviewer | Reviews code for bugs, security issues, improvements |
| **Executor Agent** | Code Runner | Runs the code and returns output or errors |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Google ADK** | Root agent orchestration and tool routing |
| **LangChain** | Prompt templates, chains, and memory in sub-agents |
| **Ollama (qwen3:8b)** | Local LLM — runs 100% offline, no paid API needed |
| **OpenAI (optional)** | Alternative LLM provider via config switch |
| **FastAPI** | REST API endpoints for each agent |
| **Docker** | Containerization for portable deployment |

---

## 📁 Project Structure

```
software-engineering-agent/
    Agent/
        __init__.py          # Exports root_agent for ADK
        Planner_Agent.py     # Planner sub-agent
        Coder_Agent.py       # Coder sub-agent
        Reviewer.py          # Reviewer sub-agent
        Executor_Agent.py    # Executor sub-agent
        Root_Agent.py        # Root agent (orchestrator)
    API/
        __init__.py
        main.py              # FastAPI endpoints
    notebooks/               # Reference notebooks
    config.py                # LLM provider configuration
    requirements.txt         # Python dependencies
    Dockerfile               # Docker build instructions
    .env.example             # Environment variable template
    README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com) installed locally
- Git

### 1. Clone the repository
```bash
git clone https://github.com/909ayanmondal-stack/Software_Eng._Multi_Agent_Project.git
cd Software_Eng._Multi_Agent_Project
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Pull the Ollama model
```bash
ollama pull qwen3:8b
```

### 5. Configure environment
```bash
cp .env.example .env
```
Edit `.env` if using OpenAI:
```
OPENAI_API_KEY=sk-your-key-here
```

### 6. Configure LLM provider
Edit `config.py`:
```python
LLM_PROVIDER = "ollama"   # or "openai"
```

---

## 🚀 Running the Project

### Option 1 — ADK Web UI (for testing agents visually)
```bash
adk web --port 8000
```
Open `http://127.0.0.1:8000` in your browser, select the `Agent` app, and start chatting.

### Option 2 — FastAPI (REST API)
```bash
uvicorn API.main:app --reload
```
Open `http://localhost:8000/docs` for the interactive API documentation.

### Option 3 — Docker
```bash
docker build -t alpha-agent .
docker run -p 8000:8000 alpha-agent
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/plan` | Takes a requirement, returns a step-by-step plan |
| POST | `/code` | Takes a plan, returns written code |
| POST | `/review` | Takes code, returns a review report |
| POST | `/execute` | Takes code, runs it, returns output or error |
| POST | `/run-all` | Takes a requirement, runs all 4 agents in sequence |

### Example Request
```json
POST /plan
{
  "requirement": "Build a login system in Python"
}
```

### Example Response
```json
{
  "status": "planning",
  "plan": "1. Create a User model\n2. Hash password using bcrypt\n3. Generate JWT token..."
}
```

---

## 💬 Example Usage (ADK Web UI)

| You type | What happens |
|---|---|
| `Build a login system in Python` | Root Agent calls Planner → returns step-by-step plan |
| `Now write the code` | Root Agent calls Coder → returns Python code |
| `Review this code: def add(a,b): return a+b` | Root Agent calls Reviewer → returns review report |
| `Run this code: print("Hello World")` | Root Agent calls Executor → returns output |
| `Build a calculator end to end` | Root Agent calls all 4 agents in sequence |

---

## 🧪 Testing Individual Agents

```bash
python -m Agent.Planner_Agent
python -m Agent.Coder_Agent
python -m Agent.Reviewer
python -m Agent.Executor_Agent
```

---

## ⚠️ Known Limitations

- **Casual conversation**: `qwen3:8b` (8B parameter model) may occasionally route greetings to the Planner tool — this is a known limitation of smaller local models. Use OpenAI for more consistent routing behavior.
- **Java/C++ execution**: Executor currently supports Python and JavaScript only. Java/C++ support is planned as a future improvement (requires compile step).
- **Speed**: Local Ollama models are slower than cloud APIs. Full pipeline (plan → code → review → execute) may take 3-10 minutes on a MacBook Air.

---

## 🔮 Future Improvements

- [ ] Add Java and C++ execution support in Executor Agent
- [ ] Persistent memory across sessions (database-backed)
- [ ] Automatic LLM fallback (OpenAI → Ollama if API fails)
- [ ] Streaming responses in FastAPI endpoints
- [ ] Frontend UI for the pipeline

---

## 🐳 Docker Hub

```bash
docker pull yourusername/se-agent:latest
```

---

## 📬 Postman Collection

Import `postman_collection.json` from the repo root to test all 5 API endpoints instantly.

---

## 👨‍💻 Author

**Ayan Mondal**
NIT Kurukshetra
[GitHub](https://github.com/909ayanmondal-stack)

---

## 📄 License

MIT License
