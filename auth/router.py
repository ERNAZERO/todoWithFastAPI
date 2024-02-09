from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from auth.models import User
from core.database import get_db
from auth.schemas import UserRegistration, UserLogin

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')