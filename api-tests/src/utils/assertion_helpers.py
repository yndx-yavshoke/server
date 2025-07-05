from pydantic import BaseModel, ValidationError

class UserModel(BaseModel):
    id: int
    email: str
    name: str
    age: int | None = None

class AuthResponseModel(BaseModel):
    token: str
    user: UserModel

def assert_user_response_structure(response):

    try:
        user_obj = UserModel(**response["body"]["user"])
    except ValidationError as e:
        assert False, f"User response validation error: {e}"

def assert_auth_response_structure(response):

    try:
        auth_obj = AuthResponseModel(**response["body"])
    except ValidationError as e:
        assert False, f"Auth response validation error: {e}"

    assert isinstance(auth_obj.token, str)
    assert len(auth_obj.token) > 0
    