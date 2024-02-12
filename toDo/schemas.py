from pydantic import BaseModel
from typing import List
from auth.schemas import UserProfile


class NoteResponse(BaseModel):
    id: int
    user: UserProfile

    class Config:
        from_attributes = True


class CreateNote(BaseModel):
    pass

