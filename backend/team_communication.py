```python
from flask import Flask, request, jsonify
from database import SQLite

app = Flask(__name__)
db = SQLite()

@app.route('/team', methods=['POST'])
def add_team():
    team_data = request.get_json()
    db.add_team(team_data)
    return jsonify({'message': 'Team added successfully'}), 201

@app.route('/team/<int:team_id>', methods=['PUT'])
def update_team(team_id):
    team_data = request.get_json()
    db.update_team(team_id, team_data)
    return jsonify({'message': 'Team updated successfully'}), 200

@app.route('/team/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    db.delete_team(team_id)
    return jsonify({'message': 'Team deleted successfully'}), 200

@app.route('/team/<int:team_id>', methods=['GET'])
def get_team(team_id):
    team = db.get_team(team_id)
    return jsonify(team), 200

@app.route('/teams', methods=['GET'])
def get_teams():
    teams = db.get_teams()
    return jsonify(teams), 200

@app.route('/communication', methods=['POST'])
def add_communication():
    communication_data = request.get_json()
    db.add_communication(communication_data)
    return jsonify({'message': 'Communication added successfully'}), 201

@app.route('/communication/<int:communication_id>', methods=['PUT'])
def update_communication(communication_id):
    communication_data = request.get_json()
    db.update_communication(communication_id, communication_data)
    return jsonify({'message': 'Communication updated successfully'}), 200

@app.route('/communication/<int:communication_id>', methods=['DELETE'])
def delete_communication(communication_id):
    db.delete_communication(communication_id)
    return jsonify({'message': 'Communication deleted successfully'}), 200

@app.route('/communication/<int:communication_id>', methods=['GET'])
def get_communication(communication_id):
    communication = db.get_communication(communication_id)
    return jsonify(communication), 200

@app.route('/communications', methods=['GET'])
def get_communications():
    communications = db.get_communications()
    return jsonify(communications), 200

if __name__ == '__main__':
    app.run(debug=True)
```