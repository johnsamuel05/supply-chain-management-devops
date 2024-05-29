from flask import Flask, request, jsonify

app = Flask(__name__)
deliveries = []

@app.route('/deliveries', methods=['GET'])
def get_deliveries():
    return jsonify(deliveries)

@app.route('/deliveries', methods=['POST'])
def add_delivery():
    delivery = request.json
    deliveries.append(delivery)
    return jsonify(delivery), 201

@app.route('/deliveries/<int:delivery_id>', methods=['GET'])
def get_delivery(delivery_id):
    delivery = next((d for d in deliveries if d['id'] == delivery_id), None)
    return jsonify(delivery) if delivery else ('', 404)

@app.route('/deliveries/<int:delivery_id>', methods=['PUT'])
def update_delivery(delivery_id):
    delivery = next((d for d in deliveries if d['id'] == delivery_id), None)
    if delivery:
        data = request.json
        delivery.update(data)
        return jsonify(delivery)
    return '', 404

@app.route('/deliveries/<int:delivery_id>', methods=['DELETE'])
def delete_delivery(delivery_id):
    global deliveries
    deliveries = [d for d in deliveries if d['id'] != delivery_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
