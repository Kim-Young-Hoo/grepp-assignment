from pydantic import BaseModel, EmailStr, Field

from schemas.base import BaseRead


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=4)
    role: str


class UserRead(BaseRead):
    id: str
    email: EmailStr
    role: str

    class Config:
        orm_mode = True
