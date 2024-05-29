from flask import Flask, request, jsonify

app = Flask(__name__)
suppliers = []

@app.route('/suppliers', methods=['GET'])
def get_suppliers():
    return jsonify(suppliers)

@app.route('/suppliers', methods=['POST'])
def add_supplier():
    supplier = request.json
    suppliers.append(supplier)
    return jsonify(supplier), 201

@app.route('/suppliers/<int:supplier_id>', methods=['GET'])
def get_supplier(supplier_id):
    supplier = next((s for s in suppliers if s['id'] == supplier_id), None)
    return jsonify(supplier) if supplier else ('', 404)

@app.route('/suppliers/<int:supplier_id>', methods=['PUT'])
def update_supplier(supplier_id):
    supplier = next((s for s in suppliers if s['id'] == supplier_id), None)
    if supplier:
        data = request.json
        supplier.update(data)
        return jsonify(supplier)
    return '', 404

@app.route('/suppliers/<int:supplier_id>', methods=['DELETE'])
def delete_supplier(supplier_id):
    global suppliers
    suppliers = [s for s in suppliers if s['id'] != supplier_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
