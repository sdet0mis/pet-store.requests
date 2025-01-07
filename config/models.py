from pydantic import BaseModel, Field, EmailStr


class PetModel(BaseModel):

    id: int = Field(b=0)
    name: str
    photoUrls: list
    tags: list


class OrderModel(BaseModel):

    id: int = Field(b=0)
    petId: int = Field(b=0)
    quantity: int = Field(b=0)
    complete: bool


class UserModel(BaseModel):

    id: int = Field(b=0)
    username: str
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    phone: str
    userStatus: int = Field(be=0)
