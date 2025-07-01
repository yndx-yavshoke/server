# PatchUserNameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User&#39;s display name | 

## Example

```python
from api_client.models.patch_user_name_request import PatchUserNameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchUserNameRequest from a JSON string
patch_user_name_request_instance = PatchUserNameRequest.from_json(json)
# print the JSON string representation of the object
print(PatchUserNameRequest.to_json())

# convert the object into a dict
patch_user_name_request_dict = patch_user_name_request_instance.to_dict()
# create an instance of PatchUserNameRequest from a dict
patch_user_name_request_from_dict = PatchUserNameRequest.from_dict(patch_user_name_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


