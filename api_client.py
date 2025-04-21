from openapi_client import ApiClient
from openapi_client.api.default_api import DefaultApi
from openapi_client.models import ItemsGet200ResponseInner, ItemsPostRequest  # This will depend on the models generated

# Configure the API client
api_client = ApiClient()
api_instance = DefaultApi(api_client)

# Example: Get all items
try:
    items = api_instance.items_get()
    print("Items:", items)
except Exception as e:
    print("Error while fetching items:", e)

# Example: Post a new item
new_item = ItemsPostRequest(name="New Item")
try:
    created_item = api_instance.items_post(new_item)
    print("Created Item:", created_item)
except Exception as e:
    print("Error while creating item:", e)

# Example: Put (update) an item by ID
item_id = 3
updated_item = ItemsPostRequest(name="Updated Item")
try:
    updated_item_response = api_instance.items_item_id_put(item_id, updated_item)
    print("Updated Item:", updated_item_response)
except Exception as e:
    print("Error while updating item:", e)
