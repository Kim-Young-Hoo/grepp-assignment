from pydantic import BaseModel, validator
from typing import Any
from uuid import UUID


class BaseRead(BaseModel):
    id: Any

    @validator('id', pre=True, allow_reuse=True)
    def parse_uuid(cls, value):
        if isinstance(value, UUID):
            return str(value)
        return value

    class Config:
        orm_mode = True
