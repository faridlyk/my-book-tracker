from typing import List, Optional
from pydantic import BaseModel

class Session(BaseModel):
    start: Optional[str] = None
    end: Optional[str] = None
    rating: Optional[int] = None
    notes: Optional[str] = None

class Book(BaseModel):
    title: str
    authors: List[str]
    isbn: int
    sessions: List[Session]