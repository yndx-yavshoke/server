# AuthResponseUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**email** | **str** |  | 
**name** | **str** |  | 
**age** | **float** |  | [optional] 

## Example

```python
from api_client.models.auth_response_user import AuthResponseUser

# TODO update the JSON string below
json = "{}"
# create an instance of AuthResponseUser from a JSON string
auth_response_user_instance = AuthResponseUser.from_json(json)
# print the JSON string representation of the object
print(AuthResponseUser.to_json())

# convert the object into a dict
auth_response_user_dict = auth_response_user_instance.to_dict()
# create an instance of AuthResponseUser from a dict
auth_response_user_from_dict = AuthResponseUser.from_dict(auth_response_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


