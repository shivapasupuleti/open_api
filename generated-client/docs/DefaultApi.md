# openapi_client.DefaultApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**items_get**](DefaultApi.md#items_get) | **GET** /items | Get all items
[**items_item_id_get**](DefaultApi.md#items_item_id_get) | **GET** /items/{item_id} | Get item by ID
[**items_item_id_put**](DefaultApi.md#items_item_id_put) | **PUT** /items/{item_id} | Update an item
[**items_post**](DefaultApi.md#items_post) | **POST** /items | Create a new item


# **items_get**
> List[ItemsGet200ResponseInner] items_get()

Get all items

Returns a list of all items

### Example


```python
import openapi_client
from openapi_client.models.items_get200_response_inner import ItemsGet200ResponseInner
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get all items
        api_response = api_instance.items_get()
        print("The response of DefaultApi->items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->items_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ItemsGet200ResponseInner]**](ItemsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_item_id_get**
> ItemsGet200ResponseInner items_item_id_get(item_id)

Get item by ID

Returns a specific item by its ID

### Example


```python
import openapi_client
from openapi_client.models.items_get200_response_inner import ItemsGet200ResponseInner
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    item_id = 56 # int | 

    try:
        # Get item by ID
        api_response = api_instance.items_item_id_get(item_id)
        print("The response of DefaultApi->items_item_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->items_item_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

### Return type

[**ItemsGet200ResponseInner**](ItemsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Item found |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_item_id_put**
> ItemsGet200ResponseInner items_item_id_put(item_id, items_post_request)

Update an item

Updates an existing item

### Example


```python
import openapi_client
from openapi_client.models.items_get200_response_inner import ItemsGet200ResponseInner
from openapi_client.models.items_post_request import ItemsPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    item_id = 56 # int | 
    items_post_request = openapi_client.ItemsPostRequest() # ItemsPostRequest | 

    try:
        # Update an item
        api_response = api_instance.items_item_id_put(item_id, items_post_request)
        print("The response of DefaultApi->items_item_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->items_item_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **items_post_request** | [**ItemsPostRequest**](ItemsPostRequest.md)|  | 

### Return type

[**ItemsGet200ResponseInner**](ItemsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Item updated successfully |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_post**
> ItemsGet200ResponseInner items_post(items_post_request)

Create a new item

Creates a new item

### Example


```python
import openapi_client
from openapi_client.models.items_get200_response_inner import ItemsGet200ResponseInner
from openapi_client.models.items_post_request import ItemsPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    items_post_request = openapi_client.ItemsPostRequest() # ItemsPostRequest | 

    try:
        # Create a new item
        api_response = api_instance.items_post(items_post_request)
        print("The response of DefaultApi->items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items_post_request** | [**ItemsPostRequest**](ItemsPostRequest.md)|  | 

### Return type

[**ItemsGet200ResponseInner**](ItemsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Item created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

