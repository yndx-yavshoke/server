import requests
import pytest
import time
from config import BASE_URL, BASE_EMAIL

def generate_unique_email():
    """Generates a unique email address using a timestamp."""
    timestamp = int(time.time() * 1000)
    return f"{BASE_EMAIL}_{timestamp}@example.com"

# вспомогательные функции для генерации уникальных реквизитов пользователей


@pytest.fixture(scope="function")
def unique_user_data():
    """
    Fixture to provide unique user data (email, password) for registration.
    Scoped to 'function' to ensure uniqueness for each test that uses it.
    """
    email = generate_unique_email()
    password = "securepassword123"
    print(f"\nGenerated unique user data: Email={email}, Password={password}")
    return {"email": email, "password": password}


@pytest.fixture(scope="function")
def registered_user(unique_user_data):
    """
    Fixture to register a unique user before a test runs.
    Returns the user's email and password.
    """
    register_url = f"{BASE_URL}/auth/register"
    response = requests.post(register_url, json=unique_user_data)
    assert response.status_code == 200, f"Failed to register user: {response.text}"
    print(f"Registered user: {unique_user_data['email']}")
    return unique_user_data


@pytest.fixture(scope="function")
def authenticated_user(registered_user):
    """
    Fixture to register and then log in a user, returning the auth token and user data.
    """
    login_url = f"{BASE_URL}/auth/login"
    response = requests.post(login_url, json=registered_user)
    assert response.status_code == 200, f"Failed to log in user: {response.text}"
    token = response.json().get("token")
    user_data = response.json().get("user")
    assert token, "Login response did not contain a token"
    assert user_data, "Login response did not contain user data"
    print(f"Authenticated user: {registered_user['email']} with token: {token[:10]}...")
    return {"token": token, "user": user_data}

# непосредственно сами тесты


def test_health_check():
    """
    Tests the /health endpoint to ensure the API is reachable.
    """
    url = f"{BASE_URL}/health"
    print(f"Testing GET {url}")
    response = requests.get(url)

    assert response.status_code == 200, \
        f"Expected status code 200, but got {response.status_code}. Response: {response.text}"
    print("Health check successful!")


def test_user_registration_success(unique_user_data):
    """
    Tests successful user registration.
    """
    url = f"{BASE_URL}/auth/register"
    payload = unique_user_data
    print(f"\nTesting POST {url} with {payload['email']}")
    response = requests.post(url, json=payload)

    assert response.status_code == 200, \
        f"Expected status code 200 for registration, got {response.status_code}. Response: {response.text}"
    data = response.json()
    assert "token" in data, "Response did not contain a token"
    assert "user" in data, "Response did not contain user data"
    assert data["user"]["email"] == payload["email"], "Registered user email mismatch"
    print(f"User {payload['email']} registered successfully.")

def test_user_registration_existing_user(registered_user):
    """
    Tests registration with an already existing user.
    Should return a 422 status code with an error.
    """
    url = f"{BASE_URL}/auth/register"
    payload = registered_user
    print(f"\nTesting POST {url} with existing user {payload['email']}")
    response = requests.post(url, json=payload)

    assert response.status_code == 422, \
        f"Expected status code 422 for existing user, got {response.status_code}. Response: {response.text}"
    data = response.json()
    assert "fields" in data, "Response did not contain 'fields' for validation error"
    assert "email" in data["fields"], "Error fields did not contain 'email'"
    print(f"Correctly handled registration of existing user {payload['email']}.")


def test_user_login_success(authenticated_user):
    """
    Tests successful user login using the authenticated_user fixture.
    The fixture itself handles the registration and login, this test just asserts its output.
    """
    print(f"\nTesting successful login for {authenticated_user['user']['email']}.")
    assert "token" in authenticated_user, "Authenticated user fixture did not return a token"
    assert "user" in authenticated_user, "Authenticated user fixture did not return user data"
    print(f"Login successful for user {authenticated_user['user']['email']}.")


def test_user_login_invalid_credentials():
    """
    Tests user login with invalid credentials.
    Should return a 422 status code.
    """
    url = f"{BASE_URL}/auth/login"
    payload = {
        "email": "nonexistent@example.com",
        "password": "wrongpassword"
    }
    print(f"\nTesting POST {url} with invalid credentials for {payload['email']}")
    response = requests.post(url, json=payload)

    assert response.status_code == 422, \
        f"Expected status code 422 for invalid credentials, got {response.status_code}. Response: {response.text}"
    data = response.json()
    assert "fields" in data, "Response did not contain 'fields' for validation error"
    assert "email" in data["fields"] or "password" in data["fields"], \
        "Error fields did not contain 'email' or 'password'"
    print("Correctly handled login with invalid credentials.")


def test_get_user_me_success(authenticated_user):
    """
    Tests retrieving authenticated user's data from /user/me.
    """
    url = f"{BASE_URL}/user/me"
    token = authenticated_user["token"]
    expected_user_data = authenticated_user["user"]

    headers = {"Authorization": f"Bearer {token}"}
    print(f"\nTesting GET {url} with authenticated user {expected_user_data['email']}")
    response = requests.get(url, headers=headers)

    assert response.status_code == 200, \
        f"Expected status code 200 for /user/me, got {response.status_code}. Response: {response.text}"

    response_data = response.json()
    assert "user" in response_data, "Response did not contain 'user' key"
    returned_user = response_data["user"]

    assert returned_user["id"] == expected_user_data["id"], "User ID mismatch"
    assert returned_user["email"] == expected_user_data["email"], "User email mismatch"
    assert returned_user["name"] == expected_user_data["name"], "User name mismatch"
    if "age" in expected_user_data:
        assert "age" in returned_user, "Age expected but not found in response"
        assert returned_user["age"] == expected_user_data["age"], "User age mismatch"
    else:
        assert "age" not in returned_user, "Age not expected but found in response"

    print(f"Successfully retrieved user data for {expected_user_data['email']}.")


def test_get_user_me_unauthorized():
    """
    Tests /user/me endpoint without authentication.
    Should return 401.
    """
    url = f"{BASE_URL}/user/me"
    print(f"\nTesting GET {url} without authorization")
    response = requests.get(url)

    assert response.status_code == 401, \
        f"Expected status code 401 for unauthorized access, got {response.status_code}. Response: {response.text}"
    response_data = response.json()
    assert "message" in response_data, "Response did not contain 'message' key for unauthorized error"
    print("Correctly handled unauthorized access to /user/me.")


def test_patch_user_name_success(authenticated_user):
    """
    Tests updating the authenticated user's name via /user/name.
    """
    url = f"{BASE_URL}/user/name"
    token = authenticated_user["token"]
    original_user_email = authenticated_user["user"]["email"]
    new_name = "New Test Name"

    headers = {"Authorization": f"Bearer {token}"}
    payload = {"name": new_name}
    print(f"\nTesting PATCH {url} for user {original_user_email} with new name: '{new_name}'")
    response = requests.patch(url, headers=headers, json=payload)

    assert response.status_code == 200, \
        f"Expected status code 200 for user name update, got {response.status_code}. Response: {response.text}"

    response_data = response.json()
    assert "user" in response_data, "Response did not contain 'user' key"
    updated_user = response_data["user"]

    assert updated_user["name"] == new_name, "User name was not updated correctly"
    assert updated_user["email"] == original_user_email, "User email unexpectedly changed"
    print(f"User {original_user_email} name updated successfully to '{new_name}'.")

    verify_url = f"{BASE_URL}/user/me"
    verify_response = requests.get(verify_url, headers=headers)
    assert verify_response.status_code == 200
    assert verify_response.json()["user"]["name"] == new_name, \
        "Verification: /user/me did not return the updated name."


def test_patch_user_name_unauthorized():
    """
    Tests /user/name endpoint without authentication.
    Should return 401.
    """
    url = f"{BASE_URL}/user/name"
    payload = {"name": "Unauthorized Name"}
    print(f"\nTesting PATCH {url} without authorization")
    response = requests.patch(url, json=payload)

    assert response.status_code == 401, \
        f"Expected status code 401 for unauthorized access, got {response.status_code}. Response: {response.text}"
    response_data = response.json()
    assert "message" in response_data, "Response did not contain 'message' key for unauthorized error"
    print("Correctly handled unauthorized access to /user/name.")


def test_patch_user_name_invalid_data(authenticated_user):
    """
    Tests /user/name endpoint with invalid (too long) name data.
    Should return 422.
    """
    url = f"{BASE_URL}/user/name"
    token = authenticated_user["token"]
    long_name = "a" * 51

    headers = {"Authorization": f"Bearer {token}"}
    payload = {"name": long_name}
    print(f"\nTesting PATCH {url} with invalid (too long) name")
    response = requests.patch(url, headers=headers, json=payload)

    assert response.status_code == 422, \
        f"Expected status code 422 for invalid name, got {response.status_code}. Response: {response.text}"
    response_data = response.json()
    assert "type" in response_data and response_data["type"] == "validation", \
        f"Expected 'type: validation' in response, got {response_data}"
    assert "on" in response_data and response_data["on"] == "body", \
        f"Expected 'on: body' in response, got {response_data}"
    assert "found" in response_data, \
        f"Expected 'found' key in response for validation error, got {response_data}"
    assert "name" in response_data["found"], \
        f"Expected 'name' field within 'found' for validation error, got {response_data['found']}"

    print("Correctly handled invalid name data for /user/name.")
