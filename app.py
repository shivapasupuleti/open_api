import logging
import time
import boto3
from logging import StreamHandler
from botocore.exceptions import NoCredentialsError
from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
import yaml
from openapi_client import ApiClient
from openapi_client.api.default_api import DefaultApi

# Initialize the Flask app
app = Flask(__name__)

# Set up CloudWatch Logs client
log_group_name = "/openapi_logs"  # Your CloudWatch log group
log_stream_name = "api_requests"  # Your CloudWatch log stream

# Initialize a CloudWatch Logs client
cloudwatch_logs_client = boto3.client('logs')

def create_log_group_if_not_exists():
    try:
        # Describe log groups and check if log group exists
        response = cloudwatch_logs_client.describe_log_groups(logGroupNamePrefix=log_group_name)
        log_groups = response.get('logGroups', [])
        
        # If the log group does not exist, create it
        if not any(group['logGroupName'] == log_group_name for group in log_groups):
            cloudwatch_logs_client.create_log_group(logGroupName=log_group_name)
            print(f"Log group {log_group_name} created.")
        else:
            print(f"Log group {log_group_name} already exists.")
    
    except Exception as e:
        print(f"Error checking or creating log group: {e}")

# Create log stream if it doesn't exist
def create_log_stream():
    try:
        # Try to create a log stream
        cloudwatch_logs_client.create_log_stream(
            logGroupName=log_group_name,
            logStreamName=log_stream_name
        )
    except cloudwatch_logs_client.exceptions.ResourceAlreadyExistsException:
        print(f"Log stream {log_stream_name} already exists.")
    except Exception as e:
        print(f"Error creating log stream: {e}")

# Call these functions before using the log stream
create_log_group_if_not_exists()
create_log_stream()


# Set up Flask logging to use CloudWatch
def create_cloudwatch_handler():
    """Create a CloudWatch log handler."""
    handler = logging.StreamHandler()  # Standard stream handler (stdout or stderr)
    handler.setLevel(logging.INFO)  # Log level (can be changed to DEBUG, ERROR, etc.)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    # Add the handler to the Flask app logger
    app.logger.addHandler(handler)

    return handler

# Function to log messages to CloudWatch
# Function to log messages to CloudWatch
def log_to_cloudwatch(message, level="INFO"):
    """Send logs to AWS CloudWatch with specific log level."""
    try:
        # Log the message at the given level
        if level == "INFO":
            app.logger.info(message)
        elif level == "ERROR":
            app.logger.error(message)
        else:
            # If level is something else, log as INFO by default
            app.logger.info(message)
        
        # Send logs to CloudWatch as well
        cloudwatch_logs_client.put_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            logEvents=[
                {
                    'timestamp': int(round(time.time() * 1000)),  # Current timestamp in milliseconds
                    'message': message
                },
            ],
        )
    except NoCredentialsError:
        app.logger.error("AWS credentials not found.")
    except Exception as e:
        app.logger.error(f"Error logging to CloudWatch: {e}")

# Initialize OpenAPI Client
api_client = ApiClient()
api_instance = DefaultApi(api_client)

# Initialize Flask-RESTX API
api = Api(app, version='1.0', title='Sample API',
          description='A sample API for testing OpenAPI specifications')

# Load OpenAPI specification
with open('openapi.yaml', 'r') as file:
    openapi_spec = yaml.safe_load(file)

# Define models
item_model = api.model('Item', {
    'id': fields.Integer(readonly=True, description='The item unique identifier'),
    'name': fields.String(required=True, description='The item name')
})

items = []
item_id_counter = 1

@api.route('/items')
class ItemList(Resource):
    @api.doc('list_items')
    @api.marshal_list_with(item_model)
    def get(self):
        """List all items"""
        log_to_cloudwatch(f"GET /items called. Returning items: {items}", level="INFO")
        return items

    @api.doc('create_item')
    @api.expect(item_model)
    @api.marshal_with(item_model, code=201)
    def post(self):
        """Create a new item"""
        global item_id_counter
        data = request.json
        item = {
            'id': item_id_counter,
            'name': data['name']
        }
        items.append(item)
        item_id_counter += 1
        log_to_cloudwatch(f"Created item with ID: {item['id']} and Name: {item['name']}", level="INFO")
        return item, 201

# Item Resource - to get, update a specific item
@api.route('/items/<int:item_id>')
@api.param('item_id', 'The item identifier')
@api.response(404, 'Item not found')
class Item(Resource):
    @api.doc('get_item')
    @api.marshal_with(item_model)
    def get(self, item_id):
        """Fetch an item given its identifier"""
        log_to_cloudwatch(f"GET /items/{item_id} called. Searching for item...", level="INFO")
        for item in items:
            if item['id'] == item_id:
                log_to_cloudwatch(f"Found item: {item}", level="INFO")
                return item
        log_to_cloudwatch(f"Item {item_id} not found", level="ERROR")
        api.abort(404, f"Item {item_id} not found")

    @api.doc('update_item')
    @api.expect(item_model)
    @api.marshal_with(item_model)
    def put(self, item_id):
        """Update an item given its identifier"""
        log_to_cloudwatch(f"PUT /items/{item_id} called. Updating item...", level="INFO")
        for item in items:
            if item['id'] == item_id:
                data = request.json
                item['name'] = data['name']
                log_to_cloudwatch(f"Updated item: {item}", level="INFO")
                return item
        log_to_cloudwatch(f"Item {item_id} not found", level="ERROR")
        api.abort(404, f"Item {item_id} not found")

# Start the Flask app
if __name__ == '__main__':
    create_cloudwatch_handler()
    app.run(debug=True, port=8000)
