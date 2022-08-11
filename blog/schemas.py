from typing import List, Union
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str
    
class Blog_Config(Blog):
    class Config():
        orm_mode = True

class User(BaseModel):
    username: str
    email: str
    password: str
    
class ShowUser(BaseModel):
    username: str
    email: str
    blogs: List[Blog_Config] = []
    class Config():
        orm_mode = True
    
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    class Config():
        orm_mode = True
        
class Login(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None