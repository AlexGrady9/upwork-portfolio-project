from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    name: str


class UserRead(BaseModel):
    id: int
    email: str
    name: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    email: str | None = None
    name: str | None = None
