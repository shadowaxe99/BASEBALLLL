```python
from flask import Flask, request, jsonify
from database import db_session
from models import Contract

app = Flask(__name__)

@app.route('/contracts', methods=['GET'])
def get_contracts():
    contracts = Contract.query.all()
    return jsonify([contract.serialize() for contract in contracts])

@app.route('/contracts/<int:contract_id>', methods=['GET'])
def get_contract(contract_id):
    contract = Contract.query.get(contract_id)
    if contract is None:
        return jsonify({'error': 'Contract not found'}), 404
    return jsonify(contract.serialize())

@app.route('/contracts', methods=['POST'])
def add_contract():
    data = request.get_json()
    new_contract = Contract(**data)
    db_session.add(new_contract)
    db_session.commit()
    return jsonify(new_contract.serialize()), 201

@app.route('/contracts/<int:contract_id>', methods=['PUT'])
def update_contract(contract_id):
    data = request.get_json()
    contract = Contract.query.get(contract_id)
    if contract is None:
        return jsonify({'error': 'Contract not found'}), 404
    for key, value in data.items():
        setattr(contract, key, value)
    db_session.commit()
    return jsonify(contract.serialize())

@app.route('/contracts/<int:contract_id>', methods=['DELETE'])
def delete_contract(contract_id):
    contract = Contract.query.get(contract_id)
    if contract is None:
        return jsonify({'error': 'Contract not found'}), 404
    db_session.delete(contract)
    db_session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
```