from pydantic import BaseModel, HttpUrl, Field
from typing import Literal, Optional


class CreateEventsRequest(BaseModel):
    title: str = Field(..., min_length=1)
    type: Literal["hackathon", "meetup", "conference", "workshop"] = Field(...)
    start_date: int = Field(...)
    end_date: int = Field(...)
    image: str = Field(...)
    description: str = Field(...)
    registration_url: HttpUrl = Field(...)
    format: Literal["online", "offline", "hybrid"] = Field(...)
    place: Optional[str] = None


