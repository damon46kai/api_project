"""
@Author: Qianhe Yu
@Date: Created in 6/25/2023 7:49 PM

"""
import datetime
import jwt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

KEY = "djknsadsalalsmdlawopepowjp0210-3"  # 随机字符串 加密key
TOKEN_EXPIRE = 60 * 24 * 7  # one week expiration


def create_token(username: str):
    """
    base on User info create token
    :param username;
    :return:
    
    """
    d = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRE),
    }

    encoded = jwt.encode(d, KEY, algorithm='HS256')

    return encoded


def get_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl='/login'))):
    """
    from token analyze user info
    :return:
    """
    try:
        d = jwt.decode(token, KEY, algorithms='HS256')
        # 1 . determine if national
        # 2. determine username legal
        username = d.get("username", "-1")
    except(jwt.PyJWTError,):
        raise HTTPException(status_code=403, detail="token unauthorized")

    if username == '-1':
        raise HTTPException(status_code=400, detail="wrong user info ")
