# PostAuthLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from api_client.models.post_auth_login_request import PostAuthLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAuthLoginRequest from a JSON string
post_auth_login_request_instance = PostAuthLoginRequest.from_json(json)
# print the JSON string representation of the object
print(PostAuthLoginRequest.to_json())

# convert the object into a dict
post_auth_login_request_dict = post_auth_login_request_instance.to_dict()
# create an instance of PostAuthLoginRequest from a dict
post_auth_login_request_from_dict = PostAuthLoginRequest.from_dict(post_auth_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


