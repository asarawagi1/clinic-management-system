from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
data_file = 'db.txt'

def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return {'patients': [], 'appointments': []}

def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file)

@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.json
    db = load_data()
    patient = {
        'name': data['name'],
        'age': data['age'],
        'gender': data['gender'],
        'diagnosis': data['diagnosis']
    }
    db['patients'].append(patient)
    save_data(db)
    return jsonify({'message': 'Patient added successfully'}), 201

@app.route('/patients', methods=['GET'])
def get_patients():
    db = load_data()
    return jsonify(db['patients'])

@app.route('/appointments', methods=['POST'])
def add_appointment():
    data = request.json
    db = load_data()
    appointment = {
        'patientName': data['patientName'],
        'date': data['date'],
        'time': data['time'],
        'doctor': data['doctor']
    }
    db['appointments'].append(appointment)
    save_data(db)
    return jsonify({'message': 'Appointment scheduled successfully'}), 201

@app.route('/appointments', methods=['GET'])
def get_appointments():
    db = load_data()
    return jsonify(db['appointments'])

if __name__ == '__main__':
    app.run(debug=True)
