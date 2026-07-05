from pydantic import BaseModel,Field
from enum import Enum

class Category(str,Enum):
    BILLING = "billing"
    TECHNICAL = "technical"
    ACCOUNT = "account"
    GENERAL = "general"


class Priority(str,Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class Sentiment(str,Enum):
    POSITIVE = "positive"
    NEuTRAL = "neutral"
    NEGATIVE = "negative"


class TicketInput(BaseModel):
    query : str = Field(...,min_length=5,description="the support tickets from the user")


class TicketOutput(BaseModel):
    category : Category
    priority : Priority
    sentiment : Sentiment
    summary : str = Field(...,description="one line summary of the issue")