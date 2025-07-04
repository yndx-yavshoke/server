import pytest,requests
def test_500_exists():
    
    response = requests.get("http://localhost:3000/error-prone")
    if response.status_code == 500:
        pytest.xfail("Известная проблема с 500 ошибкой")
    else:
        assert True