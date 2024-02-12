from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from core.database import get_db
from .models import Note
from auth.router import get_current_user
from toDo.schemas import NoteResponse, CreateNote
from auth.models import User

router = APIRouter()


@router.get('/notes/', response_model=list[NoteResponse], tags=['Notes'])
def note_list(db: Session = Depends(get_db)):
    notes = db.query(Note).all()
    return notes


@router.post('/notes/create', response_model=NoteResponse, tags=['Notes'])
def create_note(note: CreateNote, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_note = Note(title=note.title, description=note.description, finished_date=note.finished_date, user_id=current_user.id)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note
