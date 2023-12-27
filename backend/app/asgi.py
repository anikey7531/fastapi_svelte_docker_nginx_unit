from typing import Dict
from fastapi import (
    status,
    HTTPException,
	FastAPI,
	Depends, 
	Body
)
from sqlalchemy.orm import Session
from schemas.users import CreateUserSchema, UserSchema, UserLoginSchema


from db_initializer import get_db
from models import users as user_model
from services.db import users as user_db_services
# -------------------------------
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

app = FastAPI()

@app.post('/signup', response_model=UserSchema)
def signup(
    payload: CreateUserSchema = Body(), 
    session:Session=Depends(get_db)
):
    """Запрос на регистрацию аккаунта"""
    payload.hashed_password = user_model.User.hash_password(payload.hashed_password)
    return user_db_services.create_user(session, user=payload)


@app.get("/")
async def index():
    """
    A simple Hello\qwda World GET request
    """
    return {"message": "Hello, World!"}

from fastapi.security import OAuth2PasswordRequestForm

@app.post('/login', response_model=Dict)
def login(payload: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)):
    """Processes user's authentication and returns a token
    on successful authentication.

    request body:

    - username: Unique identifier for a user e.g email, 
                phone number, name

    - password:
    """
    try:
        user:user_model.User = user_db_services.get_user(
            session=session, email=payload.username
        )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user credentials"
        )

    is_validated:bool = user.validate_password(payload.password)
    if not is_validated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user credentials"
        )

    return user.generate_token()


@app.get("/profile/{id}", response_model=UserSchema)
def profile(id:int, token: str = Depends(oauth2_scheme), session:Session=Depends(get_db)):
    """
        Запрос на получение профиля пользователя
    """
    return user_db_services.get_user_by_id(session=session, id=id)