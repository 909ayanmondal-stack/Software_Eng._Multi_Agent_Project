from dotenv import load_dotenv   
load_dotenv()
from fastapi import FastAPI
from pydantic import BaseModel
from Agent.Planner_Agent import planner
from Agent.Coder_Agent import coder
from Agent.Reviewer import reviewer
from Agent.Executor_Agent import executor
from API.auth import router as auth_router
from API.auth import get_current_user
from fastapi import Depends

app = FastAPI(
    title="Software Engineering Multi-Agent System",
    description="AI-powered agents that plan, write, review and execute code.",
    version="1.0.0" 
)
app.include_router(auth_router, prefix="/auth", tags=["Authentication"]) 

# --- Updated Schemas ---

class PlanRequest(BaseModel):
    requirement: str
    thread_id: str = "default"  # Fixed: Added thread_id so request.thread_id works

class CodeRequest(BaseModel):
    task: str
    thread_id: str = "default"

class ReviewRequest(BaseModel):
    code: str
    thread_id: str = "default"

class ExecuteRequest(BaseModel):
    code: str
    language: str = "python"
    thread_id: str = "default"

class RunAllRequest(BaseModel):
    requirement: str
    language: str = "python" 
    thread_id: str = "default"  # Fixed: Added so your agents can track the session sequential run


# --- Endpoints ---

@app.post("/plan")
def plan(request: PlanRequest):
    result = planner(requirement=request.requirement, thread_id=request.thread_id)
    return {"plan": result}


@app.post("/code")
def code(request: CodeRequest):
    result = coder(task=request.task, thread_id=request.thread_id)
    return {"code": result}


@app.post("/review")
def review(request: ReviewRequest):
    result = reviewer(code=request.code, thread_id=request.thread_id)
    return {"review": result}


@app.post("/execute")
def execute(request: ExecuteRequest):
    result = executor(code=request.code, language=request.language,thread_id=request.thread_id)
    return result


@app.post("/run-all")
def run_all(request: RunAllRequest):
    # Fixed: Passing outputs sequentially down the chain instead of using 
    # undefined fields like request.task or request.code
    
    plan_result = planner(requirement=request.requirement, thread_id=request.thread_id)
    
    # Since 'coder' needs a task, we pass the generated plan to it
    code_result = coder(task=plan_result, thread_id=request.thread_id)
    actual_code = code_result["code"]
    
    # Since 'reviewer' needs code, we pass the generated code to it
    review_result = reviewer(code=actual_code, thread_id=request.thread_id)
    
    # Finally, we pass the code downstream to the executor
    execute_result = executor(code=actual_code, language=request.language,thread_id=request.thread_id)
    
    return {
        "plan": plan_result,
        "code": actual_code,
        "review": review_result,
        "execution": execute_result
    }
@app.post("/plan")
def plan(request: PlanRequest, current_user: str = Depends(get_current_user)):
    result = planner(requirement=request.requirement, thread_id=request.thread_id)
    return {"plan": result, "requested_by": current_user}