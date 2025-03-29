from pydantic import BaseModel, HttpUrl, Field
from typing import Literal, Optional


class CreateEventsRequest(BaseModel):
    title: str = Field(..., min_length=1)
    type: Literal["hackathon", "meetup", "conference", "workshop"] = Field(...)
    start_date: str = Field(...)
    end_date: str = None
    image: str = Field(...)
    description: str = Field(...)
    registration_url: str = Field(...)
    format: Literal["online", "offline", "hybrid"] = Field(...)
    place: Optional[str] = None


