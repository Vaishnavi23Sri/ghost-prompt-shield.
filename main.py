from fastapi import FastAPI
from pydantic import BaseModel
from ghost_prompt_shield import GhostPromptShield, SafetyState, SafetyDecision

app = FastAPI(title="Ghost Prompt Shield API")

shield = GhostPromptShield()
state = SafetyState()


class PromptRequest(BaseModel):
    prompt: str


class DecisionResponse(BaseModel):
    decision: str


@app.post("/check", response_model=DecisionResponse)
def check_prompt(request: PromptRequest):
    decision = shield.evaluate(request.prompt, state)
    return {"decision": decision.value}
