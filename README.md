# AI Ticket Triage API

An AI-powered backend that automatically classifies support tickets — category, priority, and sentiment — so support teams can route and prioritize without reading every message manually.


**Live demo:** https://ai-ticket-triage-ui.vercel.app
**Live API:** https://ai-ticket-triage-api.onrender.com

## What it does

Send it a support message like *"My payment failed twice and I got charged both times"* and it returns:

```json
{
  "category": "billing",
  "priority": "high",
  "sentiment": "negative",
  "summary": "Double charge due to failed payment"
}
```

No manual triage. The AI reads the ticket once and tags it instantly.

## Concepts demonstrated

- **Structured Outputs** — Pydantic + Enums enforce a strict, validated response shape from the LLM every time
- **Prompt Engineering** — a system prompt constrains the model to return clean, parseable JSON only
- **Error Handling** — layered exception handling for API failures, malformed JSON, and schema mismatches, each mapped to the correct HTTP status
- **Streaming Responses** — a second endpoint streams the classification back chunk by chunk using a generator
- **Deployment** — backend on Render, frontend on Vercel, connected via CORS

## Tech stack

FastAPI · Pydantic · Groq API (Llama 3.3 70B) · Python

## API

**POST `/classify`**
Returns the full classification in one response.

**POST `/classify/stream`**
Streams the classification as it's generated.

Request body:
```json
{ "query": "your support ticket text here" }
```

## Run locally

```bash
pip install -r requirements.txt
```

Create a `.env` file:
```
GROQ_API_KEY=your_key_here
```

Start the server:
```bash
uvicorn main:app --reload
```

## Project structure

```
├── main.py          # FastAPI app + routes
├── models.py         # Pydantic schemas + enums
├── prompts.py         # System prompt
├── groq_client.py      # Groq API calls (sync + streaming) + error handling
├── exceptions.py        # Custom exception classes
└── requirements.txt
```
