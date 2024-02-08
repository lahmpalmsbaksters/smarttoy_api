from pydantic import BaseModel, Field


class User(BaseModel):
    id: int = Field(...)
    username: str = Field(...)
    email: str = Field(...)
