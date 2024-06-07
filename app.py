from flask import Flask, jsonify, request

app = Flask(__name__)


animals = [
    {"id": 1, "species": "Tiger", "age": 5, "gender": "Male", "special_requirements": "Carnivore diet"},
    {"id": 2, "species": "Hipotalamus", "age": 10, "gender": "Female", "special_requirements": "Large enclosure"},
]

employees = [
    {"id": 1, "name": "Jason Bourne", "email": "jasonbourne@example.com", "phone": "123-456-7890", "role": "Zookeeper", "schedule": "9-5"},
    {"id": 2, "name": "John Wick", "email": "johnwick@example.com", "phone": "987-654-3210", "role": "Veterinarian", "schedule": "10-6"},
]

@app.route('/animals', methods=['GET'])
def get_animals():
    return jsonify(animals)

@app.route('/animals/<int:animal_id>', methods=['GET'])
def get_animal(animal_id):
    animal = next((animal for animal in animals if animal['id'] == animal_id), None)
    return jsonify(animal) if animal else (jsonify({'message': 'Animal not found'}), 404)

@app.route('/animals', methods=['POST'])
def create_animal():
    new_animal = request.get_json()
    new_animal['id'] = len(animals) + 1
    animals.append(new_animal)
    return jsonify(new_animal), 201

@app.route('/animals/<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    animal = next((animal for animal in animals if animal['id'] == animal_id), None)
    if animal:
        data = request.get_json()
        animal.update(data)
        return jsonify(animal)
    return jsonify({'message': 'Animal not found'}), 404

@app.route('/animals/<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    global animals
    animals = [animal for animal in animals if animal['id'] != animal_id]
    return jsonify({'message': 'Animal deleted'})


@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = next((employee for employee in employees if employee['id'] == employee_id), None)
    return jsonify(employee) if employee else (jsonify({'message': 'Employee not found'}), 404)

@app.route('/employees', methods=['POST'])
def create_employee():
    new_employee = request.get_json()
    new_employee['id'] = len(employees) + 1
    employees.append(new_employee)
    return jsonify(new_employee), 201

@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employee = next((employee for employee in employees if employee['id'] == employee_id), None)
    if employee:
        data = request.get_json()
        employee.update(data)
        return jsonify(employee)
    return jsonify({'message': 'Employee not found'}), 404

@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    global employees
    employees = [employee for employee in employees if employee['id'] != employee_id]
    return jsonify({'message': 'Employee deleted'})

if __name__ == '__main__':
    app.run(debug=True)