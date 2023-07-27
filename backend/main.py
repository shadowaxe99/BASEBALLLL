```python
from flask import Flask, render_template, request, redirect, url_for
import player_management
import team_communication
import contract_negotiation
import scouting_report_integration
import reporting_analytics
import speed_improvements
import database

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/player_management', methods=['GET', 'POST'])
def manage_players():
    if request.method == 'POST':
        player_management.add_player(request.form)
        return redirect(url_for('dashboard'))
    players = player_management.get_all_players()
    return render_template('player_management.html', players=players)

@app.route('/team_communication', methods=['GET', 'POST'])
def communicate_with_teams():
    if request.method == 'POST':
        team_communication.send_message(request.form)
        return redirect(url_for('dashboard'))
    messages = team_communication.get_all_messages()
    return render_template('team_communication.html', messages=messages)

@app.route('/contract_negotiation', methods=['GET', 'POST'])
def negotiate_contracts():
    if request.method == 'POST':
        contract_negotiation.update_contract(request.form)
        return redirect(url_for('dashboard'))
    contracts = contract_negotiation.get_all_contracts()
    return render_template('contract_negotiation.html', contracts=contracts)

@app.route('/scouting_report_integration')
def integrate_scouting_reports():
    reports = scouting_report_integration.get_all_reports()
    return render_template('scouting_report_integration.html', reports=reports)

@app.route('/reporting_analytics')
def view_reports_and_analytics():
    reports = reporting_analytics.get_all_reports()
    return render_template('reporting_analytics.html', reports=reports)

@app.route('/speed_improvements')
def improve_speed():
    improvements = speed_improvements.get_all_improvements()
    return render_template('speed_improvements.html', improvements=improvements)

if __name__ == '__main__':
    database.init_db()
    app.run(debug=True)
```