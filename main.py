from fastapi.responses import StreamingResponse
from groq_client import classify_ticket_stream
from fastapi import FastAPI, HTTPException
from groq_client import classify_ticket
from models import TicketInput
from exceptions import GroqApiError, InvalidResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/classify/stream")
def classify_stream(ticket : TicketInput):
    return StreamingResponse(

        classify_ticket_stream(ticket.query),
        media_type="text/plain"
    )
    
@app.post("/classify")
def classify(ticket: TicketInput):
    try:
        result = classify_ticket(ticket.query)
        return result
    except GroqApiError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except InvalidResponse as e:
        raise HTTPException(status_code=502, detail=str(e))

