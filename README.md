# Software Engineering Multi-Agent AI System

An AI-powered software engineering platform that uses multiple specialized AI agents to assist with the software development lifecycle — from requirement analysis and architecture design to code generation, review, and testing.

## 🚀 Overview

The **Software Engineering Multi-Agent AI System** is designed to simulate a collaborative software engineering workflow using specialized AI agents.

Instead of relying on a single AI model for every task, the system divides the development process into multiple responsibilities. Each agent focuses on a specific stage of software development and contributes to the overall workflow.

The project includes:

* React-based frontend
* FastAPI backend
* MongoDB database
* JWT-based authentication
* Specialized AI agents
* REST APIs
* Modular backend architecture
* AI-assisted software development workflow

---

## ✨ Features

### 🤖 Multi-Agent Software Engineering

The system is designed around specialized agents for different software engineering tasks:

1. **Requirement Analyst**

   * Understands user requirements
   * Breaks requirements into structured tasks

2. **Architecture Agent**

   * Analyzes requirements
   * Helps design the software architecture and development flow

3. **Code Agent**

   * Generates implementation-oriented code
   * Uses the output of previous stages as context

4. **Review Agent**

   * Reviews generated code
   * Identifies potential issues and improvements

5. **Testing Agent**

   * Helps analyze functionality
   * Identifies potential testing requirements and issues

---

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │      React UI        │
                    │   Frontend Client    │
                    └──────────┬───────────┘
                               │
                               │ REST API
                               ▼
                    ┌──────────────────────┐
                    │      FastAPI         │
                    │      Backend         │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌────────────┐   ┌────────────┐   ┌────────────┐
       │   Auth     │   │ AI Agents  │   │  Database  │
       │   Module   │   │  Workflow  │   │  MongoDB   │
       └────────────┘   └─────┬──────┘   └────────────┘
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
        Requirement      Architecture       Code
          Agent              Agent           Agent
             │                │                │
             └────────────────┼────────────────┘
                              ▼
                       Review / Testing
                            Agents
```

---

# 🛠️ Tech Stack

## Frontend

* React.js
* Vite
* Tailwind CSS
* JavaScript
* Fetch API
* Browser Local Storage

## Backend

* Python
* FastAPI
* Pydantic
* JWT Authentication
* Passlib / bcrypt
* REST APIs

## Database

* MongoDB

## AI / Agent Layer

* Large Language Models
* Multi-Agent Architecture
* Agent-based software engineering workflow

## Development Tools

* Git
* GitHub
* VS Code
* npm
* Python
* Docker

---

# 📁 Project Structure

```text
Software_Eng._Multi_Agent_Project/
│
├── frontend/
│   │
│   ├── public/
│   │
│   ├── src/
│   │   ├── assets/
│   │   │
│   │   ├── components/
│   │   │   ├── Navbar.jsx
│   │   │   ├── Hero.jsx
│   │   │   ├── Workflow.jsx
│   │   │   ├── Features.jsx
│   │   │   └── Footer.jsx
│   │   │
│   │   ├── Pages/
│   │   │   ├── Login.jsx
│   │   │   └── Register.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
├── backend/
│   │
│   ├── api/
│   ├── agents/
│   ├── models/
│   ├── services/
│   ├── utils/
│   ├── auth.py
│   ├── main.py
│   └── ...
│
├── .env
├── requirements.txt
└── README.md
```

> The backend directory structure may vary depending on the current implementation.

---

# 🔐 Authentication

The application implements authentication using **JWT (JSON Web Tokens)**.

### Authentication Flow

```text
User
 │
 ▼
React Login/Register
 │
 ▼
FastAPI Authentication API
 │
 ├── Validate credentials
 │
 ├── Hash / verify password
 │
 └── Generate JWT
 │
 ▼
React stores access token
 │
 ▼
Authenticated API requests
 │
 ▼
FastAPI verifies JWT
```

### Available Authentication APIs

| Method | Endpoint                | Purpose                   |
| ------ | ----------------------- | ------------------------- |
| POST   | `/auth/register`        | Register a new user       |
| POST   | `/auth/login`           | Authenticate user         |
| GET    | `/auth/profile`         | Get authenticated profile |
| POST   | `/auth/logout`          | Logout                    |
| POST   | `/auth/change-password` | Change password           |

---

# 🔌 Backend API

The backend exposes REST APIs through FastAPI.

The API layer is responsible for:

* Authentication
* User management
* Agent workflow execution
* Request validation
* Communication with AI services
* Database interaction
* Returning structured responses to the frontend

FastAPI also provides interactive API documentation during development.

After starting the backend, the documentation is typically available at:

```text
http://127.0.0.1:8000/docs
```

---

# 🖥️ Frontend

The frontend is built using **React + Vite + Tailwind CSS**.

The frontend provides:

* Landing page
* Authentication UI
* Login
* Registration
* Agent workflow presentation
* API communication
* Responsive UI

### Frontend → Backend Communication

```text
React Component
      │
      ▼
API Service
      │
      ▼
Fetch()
      │
      ▼
FastAPI Endpoint
      │
      ▼
Backend Logic
      │
      ▼
Response
      │
      ▼
React UI
```

---

# ⚙️ Environment Variables

Create a `.env` file inside the `frontend/` directory:

```env
VITE_API_URL=http://127.0.0.1:8000
```

For the backend, configure the required environment variables according to your local setup.

Example:

```env
SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
MONGODB_URL=your_mongodb_connection_string
```

> Never commit real API keys, passwords, database credentials, or secret keys to GitHub.

---

# 🚀 Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/909ayanmondal-stack/Software_Eng._Multi_Agent_Project.git
```

```bash
cd Software_Eng._Multi_Agent_Project
```

---

# 🐍 Backend Setup

Create and activate a virtual environment:

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure your backend environment variables.

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The backend should then be available at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

> If your `main.py` is located inside another package, adjust the Uvicorn module path accordingly.

---

# ⚛️ Frontend Setup

Move into the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

---

# 🔄 Application Workflow

The intended software engineering workflow is:

```text
User Requirement
       │
       ▼
Requirement Analysis
       │
       ▼
Architecture Design
       │
       ▼
Code Generation
       │
       ▼
Code Review
       │
       ▼
Testing
       │
       ▼
Improved Software Solution
```

Each stage can contribute information to subsequent stages, allowing the system to follow a structured software development process.

---

# 🧠 Multi-Agent Approach

A traditional single-agent workflow can attempt to perform every software engineering task using one AI process.

This project instead separates responsibilities into specialized agents.

```text
                 User Requirement
                        │
                        ▼
              Requirement Agent
                        │
                        ▼
             Architecture Agent
                        │
                        ▼
                  Code Agent
                        │
                        ▼
                 Review Agent
                        │
                        ▼
                Testing Agent
```

This modular approach makes individual responsibilities easier to organize, modify, and extend.

---

# 📡 API Integration

The frontend communicates with the backend through HTTP requests.

Example authentication request:

```javascript
fetch(`${API_URL}/auth/login`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    username,
    password,
  }),
})
```

Authenticated requests use the JWT access token:

```text
Authorization: Bearer <access_token>
```

---

# 🗄️ Database

The backend uses **MongoDB** for persistent data storage.

The database layer is responsible for storing application data such as user information and other project-specific data required by the backend.

---

# 🔒 Security

Security-related implementation includes:

* Password hashing
* JWT-based authentication
* Protected API endpoints
* Environment variables for secrets
* Bearer-token authorization
* Input validation through Pydantic models

Secrets and credentials should be stored in environment variables rather than committed to source control.

---

# 🧪 Testing

The backend APIs can be tested using:

* FastAPI Swagger UI
* Postman
* Browser/client requests
* Frontend integration

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 📸 Screenshots

Screenshots can be added here to demonstrate the running application.

Recommended screenshots:

* Landing page
* Login/Register page
* AI agent workflow/dashboard
* Generated agent output

Example:

```markdown
## Screenshots

### Landing Page

![Landing Page](screenshots/landing-page.png)

### Dashboard

![Dashboard](screenshots/dashboard.png)
```

---

# 🐳 Docker

The project can be containerized using Docker for consistent development and deployment environments.

Example workflow:

```bash
docker build -t software-engineering-ai .
```

```bash
docker run -p 8000:8000 software-engineering-ai
```

> Update the commands according to the Docker configuration currently present in the repository.

---

# 📌 Future Improvements

Planned improvements may include:

* Complete AI-agent orchestration
* More specialized software engineering agents
* Improved agent communication
* RAG-based project knowledge
* Persistent project/workspace management
* Automated test generation
* Code execution and validation
* GitHub repository integration
* Deployment pipeline
* Production deployment
* Improved dashboard and visualization
* Enhanced monitoring and logging

---

# 🎯 Project Goals

The primary goal of this project is to explore how **AI agents can collaborate to support software engineering activities**.

The project combines:

```text
Artificial Intelligence
        +
Multi-Agent Systems
        +
Software Engineering
        +
Backend Development
        +
Frontend Development
        +
Database Systems
```

---

# 👨‍💻 Author

**Ayan Mondal**

Master of Computer Applications
National Institute of Technology Kurukshetra

GitHub:
https://github.com/909ayanmondal-stack

LinkedIn:
https://www.linkedin.com/in/ayan-mondal-74360a260

---

# 📄 License

This project is intended for educational, research, and portfolio purposes.

Add the appropriate license file if you decide to distribute the project under an open-source license.
