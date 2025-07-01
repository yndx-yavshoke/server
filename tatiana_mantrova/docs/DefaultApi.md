# api_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health**](DefaultApi.md#get_health) | **GET** /health | 
[**get_user_me**](DefaultApi.md#get_user_me) | **GET** /user/me | Get current user data
[**patch_user_name**](DefaultApi.md#patch_user_name) | **PATCH** /user/name | Update user name
[**post_auth_login**](DefaultApi.md#post_auth_login) | **POST** /auth/login | Sign in the user
[**post_auth_register**](DefaultApi.md#post_auth_register) | **POST** /auth/register | Sign up the user
[**post_exist**](DefaultApi.md#post_exist) | **POST** /exist | Check if user exists


# **get_health**
> get_health()

### Example


```python
import api_client
from api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_client.DefaultApi(api_client)

    try:
        api_instance.get_health()
    except Exception as e:
        print("Exception when calling DefaultApi->get_health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_me**
> GetUserMe200Response get_user_me()

Get current user data

Returns the authenticated user's profile information

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import api_client
from api_client.models.get_user_me200_response import GetUserMe200Response
from api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_client.DefaultApi(api_client)

    try:
        # Get current user data
        api_response = api_instance.get_user_me()
        print("The response of DefaultApi->get_user_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetUserMe200Response**](GetUserMe200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User data retrieved successfully |  -  |
**401** | Unauthorized - Invalid or missing token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_user_name**
> GetUserMe200Response patch_user_name(patch_user_name_request)

Update user name

Updates the authenticated user's display name

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import api_client
from api_client.models.get_user_me200_response import GetUserMe200Response
from api_client.models.patch_user_name_request import PatchUserNameRequest
from api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_client.DefaultApi(api_client)
    patch_user_name_request = api_client.PatchUserNameRequest() # PatchUserNameRequest | 

    try:
        # Update user name
        api_response = api_instance.patch_user_name(patch_user_name_request)
        print("The response of DefaultApi->patch_user_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->patch_user_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_user_name_request** | [**PatchUserNameRequest**](PatchUserNameRequest.md)|  | 

### Return type

[**GetUserMe200Response**](GetUserMe200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User name updated successfully |  -  |
**401** | Unauthorized - Invalid or missing token |  -  |
**422** | Validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_login**
> AuthResponse post_auth_login(post_auth_login_request)

Sign in the user

### Example


```python
import api_client
from api_client.models.auth_response import AuthResponse
from api_client.models.post_auth_login_request import PostAuthLoginRequest
from api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_client.DefaultApi(api_client)
    post_auth_login_request = api_client.PostAuthLoginRequest() # PostAuthLoginRequest | 

    try:
        # Sign in the user
        api_response = api_instance.post_auth_login(post_auth_login_request)
        print("The response of DefaultApi->post_auth_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->post_auth_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_auth_login_request** | [**PostAuthLoginRequest**](PostAuthLoginRequest.md)|  | 

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully logged in |  -  |
**422** | Invalid credentials |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_register**
> AuthResponse post_auth_register(post_auth_register_request)

Sign up the user

### Example


```python
import api_client
from api_client.models.auth_response import AuthResponse
from api_client.models.post_auth_register_request import PostAuthRegisterRequest
from api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_client.DefaultApi(api_client)
    post_auth_register_request = api_client.PostAuthRegisterRequest() # PostAuthRegisterRequest | 

    try:
        # Sign up the user
        api_response = api_instance.post_auth_register(post_auth_register_request)
        print("The response of DefaultApi->post_auth_register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->post_auth_register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_auth_register_request** | [**PostAuthRegisterRequest**](PostAuthRegisterRequest.md)|  | 

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully registered |  -  |
**422** | User already exists |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_exist**
> PostExist200Response post_exist(post_exist_request)

Check if user exists

### Example


```python
import api_client
from api_client.models.post_exist200_response import PostExist200Response
from api_client.models.post_exist_request import PostExistRequest
from api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_client.DefaultApi(api_client)
    post_exist_request = api_client.PostExistRequest() # PostExistRequest | 

    try:
        # Check if user exists
        api_response = api_instance.post_exist(post_exist_request)
        print("The response of DefaultApi->post_exist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->post_exist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_exist_request** | [**PostExistRequest**](PostExistRequest.md)|  | 

### Return type

[**PostExist200Response**](PostExist200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, text/plain
 - **Accept**: application/json, multipart/form-data, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

