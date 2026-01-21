from pydantic import BaseModel
from typing import List


class User(BaseModel):
    name: str
    email: str
    password: str


class Blog(BaseModel):
    title: str
    body: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    model_config = {"from_attributes": True}


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    model_config = {"from_attributes": True}


class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
    
class Token(BaseModel):
    access_token: str
    token_type: str