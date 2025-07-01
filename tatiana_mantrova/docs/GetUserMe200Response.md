# GetUserMe200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from api_client.models.get_user_me200_response import GetUserMe200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserMe200Response from a JSON string
get_user_me200_response_instance = GetUserMe200Response.from_json(json)
# print the JSON string representation of the object
print(GetUserMe200Response.to_json())

# convert the object into a dict
get_user_me200_response_dict = get_user_me200_response_instance.to_dict()
# create an instance of GetUserMe200Response from a dict
get_user_me200_response_from_dict = GetUserMe200Response.from_dict(get_user_me200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


