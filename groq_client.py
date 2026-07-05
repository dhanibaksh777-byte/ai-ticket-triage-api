from dotenv import load_dotenv
from groq import Groq
from prompts import SYSTEM_PROMPT
from models import TicketOutput
from exceptions import GroqApiError,InvalidResponse
from pydantic import ValidationError
import os

import json



load_dotenv()

client = Groq(api_key=os.getenv("groq_api"))
def classify_ticket(query: str):
    try:
        Response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": query},
            ],
            temperature=0.3,
            
        )
    except Exception as e:
        raise GroqApiError(f"Groq API call failed: {str(e)}")

    raw_text = Response.choices[0].message.content.strip()

    try:
        parsed = json.loads(raw_text)
    except json.JSONDecodeError as e:
        raise InvalidResponse(f"Groq returned invalid JSON: {str(e)}")
    
    try:
        return TicketOutput(**parsed)
    except ValidationError as e:
        raise InvalidResponse(f"Groq response failed schema validation: {str(e)}")

        




def classify_ticket_stream(query : str):
    stream = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [{"role" : "system", "content" :SYSTEM_PROMPT },
                    {"role" : "user", "content" : query},

                    ],
                     temperature=0.3,
                     stream=True,

    )
    for chunks in stream:
        content = chunks.choices[0].delta.content
        if content:
            yield content


    