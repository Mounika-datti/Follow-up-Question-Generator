from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from evaluators.answer_evaluator import evaluate_answer
from rules.followup_rules import apply_rules
from generators.question_generator import generate_question

from memory.interview_memory import (
    get_followup_count,
    increment_followup
)

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input Schema
class InterviewInput(BaseModel):

    session_id: str

    previous_question: str

    candidate_answer: str


# Home Route
@app.get("/")
def home():

    return {
        "message": "AI Follow-up Generator Running"
    }


# Follow-up Generation Route
@app.post("/generate-followup")
def generate_followup(data: InterviewInput):

    # Step 1: Evaluate Candidate Answer
    evaluation = evaluate_answer(
        data.previous_question,
        data.candidate_answer
    )

    # Step 2: Get Current Follow-up Count
    followup_count = get_followup_count(
        data.session_id
    )

    # Step 3: Apply Rules
    rule_type = apply_rules(
        evaluation,
        followup_count
    )

    # Step 4: Generate AI Follow-up Question
    followup_question = generate_question(
        rule_type,
        evaluation,
        data.previous_question,
        data.candidate_answer
    )

    # Step 5: Increment Session Follow-up Count
    increment_followup(data.session_id)

    # Final Response
    return {

        "previous_question": data.previous_question,

        "candidate_answer": data.candidate_answer,

        "evaluation": evaluation,

        "followup_question": followup_question,

        "followup_count": followup_count + 1
    }