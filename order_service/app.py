from flask import Flask, request, jsonify

app = Flask(__name__)
orders = []

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def add_order():
    order = request.json
    orders.append(order)
    return jsonify(order), 201

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    return jsonify(order) if order else ('', 404)

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    if order:
        data = request.json
        order.update(data)
        return jsonify(order)
    return '', 404

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    global orders
    orders = [o for o in orders if o['id'] != order_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
