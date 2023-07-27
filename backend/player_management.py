```python
from flask import Flask, request, jsonify
from database import SQLite

app = Flask(__name__)
db = SQLite()

@app.route('/player', methods=['POST'])
def add_player():
    data = request.get_json()
    player_id = db.insert('Players', data)
    return jsonify({'player_id': player_id}), 201

@app.route('/player/<int:player_id>', methods=['GET'])
def get_player(player_id):
    player = db.select('Players', {'id': player_id})
    return jsonify(player), 200

@app.route('/player/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    data = request.get_json()
    db.update('Players', {'id': player_id}, data)
    return jsonify({'message': 'Player updated successfully'}), 200

@app.route('/player/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    db.delete('Players', {'id': player_id})
    return jsonify({'message': 'Player deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```