from pydantic import BaseModel, ValidationError

class UserModel(BaseModel):
    id: int
    email: str
    name: str
    age: int

class AuthResponseModel(BaseModel):
    token: str
    user: UserModel

def assert_user_response_structure(response, expected_email=None, expected_age=None):

    try:
        user_obj = UserModel(**response["body"]["user"])
    except ValidationError as e:
        assert False, f"User response validation error: {e}"

    if expected_email:
        assert user_obj.email == expected_email
    if expected_age is not None:
        assert user_obj.age == expected_age

def assert_auth_response_structure(response, expected_email=None, expected_age=None):
    try:
        auth_obj = AuthResponseModel(**response["body"])
    except ValidationError as e:
        assert False, f"Auth response validation error: {e}"

    assert isinstance(auth_obj.token, str)
    assert len(auth_obj.token) > 0
    if expected_email:
        assert auth_obj.user.email == expected_email
    if expected_age is not None:
        assert auth_obj.user.age == expected_age 