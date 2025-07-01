# PostAuthRegisterRequest

Expected an email and password (+ age if experiment enabled)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email (max 50 characters) | 
**password** | **str** | User password (5-20 characters) | 
**age** | **float** | User age (0-99, optional) | [optional] 

## Example

```python
from api_client.models.post_auth_register_request import PostAuthRegisterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAuthRegisterRequest from a JSON string
post_auth_register_request_instance = PostAuthRegisterRequest.from_json(json)
# print the JSON string representation of the object
print(PostAuthRegisterRequest.to_json())

# convert the object into a dict
post_auth_register_request_dict = post_auth_register_request_instance.to_dict()
# create an instance of PostAuthRegisterRequest from a dict
post_auth_register_request_from_dict = PostAuthRegisterRequest.from_dict(post_auth_register_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


