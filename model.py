"""
@Author: Qianhe Yu
@Date: Created in 6/11/2023 9:48 PM

"""

from pydantic import BaseModel


class Item(BaseModel):
    a: int
    b: int


class LoginInfo(BaseModel):
    username: str
    password: str