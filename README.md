# 🤖 Software Engineering Multi-Agent System

An AI-powered software engineering assistant that takes a requirement and automatically plans, writes, reviews, and executes code — using a multi-agent architecture powered by Google ADK, LangChain, and Ollama. Now with JWT authentication and MongoDB Atlas integration.

---

## 🧠 Architecture

The system follows a **hub-and-spoke model** where the Root Agent orchestrates 4 specialized sub-agents:

```
User Request (with JWT token)
      ↓
 Root Agent (Google ADK + LiteLLM)
      ↓
  ┌───┴────────────────────────┐
  ↓          ↓         ↓       ↓
Planner   Coder   Reviewer  Executor
  ↓          ↓         ↓       ↓
 Plan      Code     Review  Output
      ↓
 MongoDB Atlas (stores history)
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
| **MongoDB Atlas** | Cloud database for user accounts and history |
| **JWT + bcrypt** | Secure authentication and password hashing |
| **Docker** | Containerization for portable deployment |

---

## 📁 Project Structure

```
Software_Engineer_Multi-Agent_project/
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
        auth.py              # Authentication logic
        database.py          # MongoDB connection
    models/
        __init__.py
        user_model.py        # User data models
    config.py                # LLM provider configuration
    requirements.txt         # Python dependencies
    Dockerfile               # Docker build instructions
    .env.example             # Environment variable template
    FASTAPI_PROJECT.postman_collection.json  # Postman collection for testing
    README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com) installed locally
- MongoDB Atlas account (free)
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
Edit `.env` with your credentials:
```
OPENAI_API_KEY=sk-your-key-here
MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/se_agent_db
SECRET_KEY=your-secret-key-here
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 6. Configure LLM provider
Edit `config.py`:
```python
LLM_PROVIDER = "ollama"   # or "openai"
```

---

## 🚀 Running the Project

### Option 1 — FastAPI (REST API)
```bash
uvicorn API.main:app --reload
```
Open `http://localhost:8000/docs` for the interactive API documentation.

### Option 2 — ADK Web UI (for testing agents visually)
```bash
adk web --port 8000
```
Open `http://127.0.0.1:8000` in your browser, select the `Agent` app, and start chatting.

### Option 3 — Docker
```bash
docker build -t se-agent .
docker run -p 8000:8000 --env-file .env se-agent
```

---

## 🔐 Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| POST | `/auth/register` | Register new user | ❌ |
| POST | `/auth/login` | Login and get JWT token | ❌ |
| GET | `/auth/profile` | Get current user profile | ✅ |
| POST | `/auth/logout` | Logout current user | ✅ |
| POST | `/auth/change-password` | Change user password | ✅ |

### Register Example:
```json
POST /auth/register
{
  "username": "ayan",
  "email": "ayan@gmail.com",
  "password": "test123"
}
```

### Login Example:
```json
POST /auth/login
{
  "username": "ayan",
  "password": "test123"
}
```

### Login Response:
```json
{
  "access_token": "eyJhbGc...",
  "token_type": "bearer",
  "username": "ayan"
}
```

---

## 🔌 Agent API Endpoints

All agent endpoints require JWT token in Authorization header:
```
Authorization: Bearer <your_token>
```

| Method | Endpoint | Description |
|---|---|---|
| POST | `/plan` | Takes a requirement, returns a step-by-step plan |
| POST | `/code` | Takes a plan, returns written code |
| POST | `/review` | Takes code, returns a review report |
| POST | `/execute` | Takes code, runs it, returns output or error |
| POST | `/run-all` | Takes a requirement, runs all 4 agents in sequence |

### Example Request:
```json
POST /run-all
{
  "requirement": "Build a fibonacci calculator in Python"
}
```

### Example Response:
```json
{
  "plan": "1. Define fibonacci function...",
  "code": "def fibonacci(n)...",
  "review": "Code looks good. Suggested improvements...",
  "execution": {"status": "success", "output": "[0, 1, 1, 2, 3, 5, 8]"}
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
- [ ] Automatic LLM fallback (OpenAI → Ollama if API fails)
- [ ] Streaming responses in FastAPI endpoints
- [ ] React frontend with login page and chat UI
- [ ] Railway/cloud deployment for global access

---

## 🐳 Docker Hub

```bash
docker pull 909ayanmondal/alpha-agent:latest
```

---

## 📬 Postman Collection

Import `FASTAPI_PROJECT.postman_collection.json` from the repo root to test all API endpoints instantly (auth + agent endpoints).

---

## 👨‍💻 Author

**Ayan Mondal**
MCA, NIT Kurukshetra
[GitHub](https://github.com/909ayanmondal-stack)

---

## 📄 License

MIT License
