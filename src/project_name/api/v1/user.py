from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from project_name.models.user import User
from project_name.schemas.user import UserCreate, UserRead, UserUpdate
from project_name.database import get_db, SessionLocal

router = APIRouter()

# Вспомогательная функция для получения пользователя


def get_user_obj(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


@router.post("/users/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(email=user.email, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user_obj(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/", response_model=list[UserRead])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(User).offset(skip).limit(limit).all()


@router.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = get_user_obj(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if user.email is not None:
        object.__setattr__(db_user, "email", user.email)
    if user.name is not None:
        object.__setattr__(db_user, "name", user.name)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user_obj(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"ok": True}
