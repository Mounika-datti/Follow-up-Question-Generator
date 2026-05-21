# Follow-up Question Generator

An AI-powered adaptive interview system that generates intelligent follow-up questions based on candidate answers using NLP, semantic similarity, rule-based evaluation, and OpenRouter LLM integration.

---

# 🚀 Project Overview

The Follow-up Question Generator is designed to simulate an intelligent AI interviewer capable of:

- Evaluating candidate answers
- Detecting missing concepts
- Measuring semantic relevance
- Generating adaptive follow-up questions
- Preventing infinite follow-up chains
- Maintaining interview context

The system uses:
- FastAPI backend
- React frontend
- spaCy NLP
- Sentence Transformers
- OpenRouter LLM integration

---

# 🎯 Features

✅ Intelligent AI-generated follow-up questions  
✅ Semantic similarity evaluation  
✅ NLP keyword extraction  
✅ Adaptive interview flow  
✅ Session memory tracking  
✅ Rule-based decision engine  
✅ OpenRouter LLM integration  
✅ React frontend UI  
✅ FastAPI REST APIs  
✅ Infinite follow-up prevention  

---

# 🏗️ Project Architecture

```text
React Frontend
       ↓
FastAPI Backend
       ↓
Answer Evaluator
       ↓
Semantic Similarity Engine
       ↓
Rule Engine
       ↓
OpenRouter LLM
       ↓
AI Follow-up Generation
```

---

# 📂 Project Structure

```text
followup-question-generator/
│
├── app.py
├── requirements.txt
├── .env
│
├── evaluators/
│   └── answer_evaluator.py
│
├── generators/
│   └── question_generator.py
│
├── rules/
│   └── followup_rules.py
│
├── llm/
│   └── openrouter_client.py
│
├── memory/
│   └── interview_memory.py
│
├── nlp/
│   ├── keyword_extractor.py
│   └── similarity.py
│
├── data/
│   └── templates.json
│
└── frontend/
    └── React Frontend
```

---

# ⚙️ Technologies Used

## Backend
- Python
- FastAPI
- Uvicorn

## Frontend
- React
- Axios
- HTML
- CSS
- JavaScript

## AI/NLP
- spaCy
- Sentence Transformers
- OpenRouter API
- Semantic Similarity
- NLP Keyword Extraction

---

# 📦 Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/followup-question-generator.git
```

## 2. Navigate to Project Folder

```bash
cd followup-question-generator
```

## 3. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

## 4. Install spaCy Model

```bash
python -m spacy download en_core_web_sm
```

## 5. Configure Environment Variables

Create `.env`

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

Get API key from:
https://openrouter.ai

## 6. Run Backend Server

```bash
python -m uvicorn app:app --reload
```

Backend runs on:
http://127.0.0.1:8000

## 7. Open Swagger API Docs

http://127.0.0.1:8000/docs

---

# 🎨 Frontend Setup

## 1. Go to Frontend Folder

```bash
cd frontend
```

## 2. Install Frontend Dependencies

```bash
npm install
npm install axios
```

## 3. Run React Frontend

```bash
npm start
```

Frontend runs on:
http://localhost:3000

---

# 🧪 API Example

## Request

```json
{
  "session_id": "session1",
  "previous_question": "What is React state?",
  "candidate_answer": "State stores component data."
}
```

## Response

```json
{
  "evaluation": {
    "score": 4,
    "confidence": 0.4,
    "keywords_found": [
      "state"
    ],
    "missing_topics": [
      "react"
    ],
    "word_count": 4,
    "semantic_similarity": 0.56
  },
  "followup_question": "Can you explain how React components can update their state and what triggers these updates?",
  "followup_count": 1
}
```

---

# 🧠 How It Works

## Step 1 — Candidate Answer Evaluation

The system:
- extracts keywords
- calculates semantic similarity
- checks answer quality
- evaluates confidence

## Step 2 — Rule Engine

Rules determine:
- clarification needed
- missing concepts
- off-topic answers
- advanced follow-up generation

## Step 3 — AI Follow-up Generation

The system sends:
- question
- answer
- evaluation

to OpenRouter LLM for intelligent follow-up generation.

---


 ⚠️ Edge Cases Handled

✅ Empty answers  
✅ Short answers  
✅ Off-topic responses  
✅ Infinite follow-up prevention  
✅ API failures  
✅ LLM fallback logic  
# 📊 Future Improvements

- Voice-based AI interviews
- Analytics dashboard
- Reinforcement learning
- Adaptive difficulty levels
- Authentication system
- Cloud deployment
- Database integration
