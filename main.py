"""
@Author: Qianhe Yu
@Date: Created in 6/11/2023 9:04 PM

most api is HTTP
minor are RPC

RPC
stands for Remote Procedure Call, which is a communication protocol that allows a program on one computer to execute a procedure or function on a remote computer over a network. It enables distributed systems to communicate and collaborate seamlessly, as if they were local components of the same system.

usage: uvicorn main:app --reload

"""

from fastapi import FastAPI, HTTPException, Depends

from libs import create_token, get_user
from model import Item, LoginInfo

app = FastAPI()


def add(a, b):  # RPCfunction
    return a + b


@app.get("/add_by_get")  # address
def add_get(a: int, b: int):  # interface
    """
    提供了一個接口地址
    :return:
    """
    c = add(a, b)
    return {"c": c}


@app.post("/add_by_post")
def add_post(a: int, b: int, user: str = Depends(get_user)):  # params  is  an object: what object? Item object
    # c=add(item.a,item.b)
    c = add(a, b)
    return {"c": c}


# res = add(1,2)
# print(res)

_data = {  # cache data
    'user': {
        "username": "beifan",
        "password": "123123"
    }

}


@app.get("/")
def index():
    return {"msg": "Hello， world"}


@app.post("/login")
def login(login_info: LoginInfo):
    if login_info.username != _data['user']['username']:
        # 用户名错误
        # 提前返回响应结果
        raise HTTPException(status_code=400, detail="wrong username")
    if login_info.password != _data['user']['password']:
        # 提前返回密码错误
        pass
        raise HTTPException(status_code=400, detail="wrong password")
    # 生成token 应该是安全 使用密码学

    return {"token": create_token(login_info.username)}
