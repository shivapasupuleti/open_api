from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
import yaml

app = Flask(__name__)
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
        return item, 201

@api.route('/items/<int:item_id>')
@api.param('item_id', 'The item identifier')
@api.response(404, 'Item not found')
class Item(Resource):
    @api.doc('get_item')
    @api.marshal_with(item_model)
    def get(self, item_id):
        """Fetch an item given its identifier"""
        for item in items:
            if item['id'] == item_id:
                return item
        api.abort(404, f"Item {item_id} not found")

    @api.doc('update_item')
    @api.expect(item_model)
    @api.marshal_with(item_model)
    def put(self, item_id):
        """Update an item given its identifier"""
        for item in items:
            if item['id'] == item_id:
                data = request.json
                item['name'] = data['name']
                return item
        api.abort(404, f"Item {item_id} not found")

if __name__ == '__main__':
    app.run(debug=True, port=8000) 