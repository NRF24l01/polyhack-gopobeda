from pydantic import BaseModel, Field
from typing import Optional, Literal


class QueryRequest(BaseModel):
    type: Optional[Literal["hackathon", "meetup", "conference", "workshop"]] = None
    format: Optional[Literal["online", "offline", "hybrid"]] = None
    dateFrom: Optional[int] = None
    dateTo: Optional[int] = None
    offset: Optional[int] = Field(0, ge=0)
    limit: Optional[int] = Field(10, ge=0)

