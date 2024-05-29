from flask import Flask, request, jsonify


app = Flask(__name__)
inventory = []

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

@app.route('/inventory', methods=['POST'])
def add_inventory():
    item = request.json
    inventory.append(item)
    return jsonify(item), 201

@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_inventory_item(item_id):
    item = next((i for i in inventory if i['id'] == item_id), None)
    return jsonify(item) if item else ('', 404)

@app.route('/inventory/<int:item_id>', methods=['PUT'])
def update_inventory_item(item_id):
    item = next((i for i in inventory if i['id'] == item_id), None)
    if item:
        data = request.json
        item.update(data)
        return jsonify(item)
    return '', 404

@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_inventory_item(item_id):
    global inventory
    inventory = [i for i in inventory if i['id'] != item_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
