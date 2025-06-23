
from pydantic import BaseModel, EmailStr

# Properties shared by all user-related models
class UserBase(BaseModel):
    email: EmailStr

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str

# Properties to return to client
# Note: We do NOT include the password here for security reasons
class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True 