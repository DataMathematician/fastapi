# Create the Pydantic models (допустимая форма данных)

from pydantic import BaseModel, EmailStr, EmailError


# post
class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

# get
class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode=True


# post
class UserBase(BaseModel):
    email: str #EmailStr

class UserCreate(UserBase):
    password: str

# get
class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode=True




