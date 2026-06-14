from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from typing import Annotated

from core.security import (
    verify_password,
    create_token,
    hash_password
)

auth = APIRouter(
    prefix="",
    tags=["Authentication"]
)

passu = hash_password("141706")

fake_users_db = {
    "harsh": {
        "username": "harsh",
        "password": passu,
    }
}

@auth.post("/login")
def login(
    form_data: Annotated[
        OAuth2PasswordRequestForm,
        Depends()
    ]
):

    user = fake_users_db.get(
        form_data.username
    )

    if (
        not user
        or
        not verify_password(
            form_data.password,
            user["password"]
        )
    ):

        raise HTTPException(
            status_code=400,
            detail="Invalid Credentials"
        )

    access_token = create_token(
        {
            "sub": form_data.username
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }