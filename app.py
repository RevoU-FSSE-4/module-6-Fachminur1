from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


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
    """
    Get Animals list
    ---
    responses:
        200:
            description: getting list of animals
    """
    return jsonify(animals), 200

@app.route('/animals/<int:animal_id>', methods=['GET'])
def get_animal(animal_id):
    """
    Get Animal list specifically
    ---
    responses:
        201:
            description: getting list of animal specifically
    """
    animal = next((animal for animal in animals if animal['id'] == animal_id), None)
    return jsonify(animal) if animal else (jsonify({'message': 'Animal not found'}), 404)

@app.route('/animals', methods=['POST'])
def create_animal():
    """
    Create a new Animal
    ---
    parameters:
        - name: body
          in: body
          required: true
          schema:
            id: Animal
            required:
              - species
              - age
              - gender
              - special_requirements
            properties:
              species:
                type: string
                description: The species of the animal
              age:
                type: integer
                description: The age of the animal
              gender:
                type: string
                description: The gender of the animal
              special_requirements:
                type: string
                description: Special requirements for the animal
    responses:
        201:
            description: New animal created successfully
    """
    new_animal = request.get_json()
    new_animal['id'] = len(animals) + 1
    animals.append(new_animal)
    return jsonify(new_animal), 201

@app.route('/animals/<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    """
    Update an Animal
    ---
    parameters:
        - name: animal_id
          in: path
          type: integer
          required: true
          description: The ID of the animal to update
        - name: body
          in: body
          required: true
          schema:
            id: Animal
            properties:
              species:
                type: string
                description: The species of the animal
              age:
                type: integer
                description: The age of the animal
              gender:
                type: string
                description: The gender of the animal
              special_requirements:
                type: string
                description: Special requirements for the animal
    responses:
        200:
            description: Animal updated successfully
        404:
            description: Animal not found
    """
    animal = next((animal for animal in animals if animal['id'] == animal_id), None)
    if animal:
        data = request.get_json()
        animal.update(data)
        return jsonify(animal), 200
    return jsonify({'message': 'Animal not found'}), 404

@app.route('/animals/<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    """
    Delete an Animal
    ---
    parameters:
        - name: animal_id
          in: path
          type: integer
          required: true
          description: The ID of the animal to delete
    responses:
        200:
            description: Animal deleted successfully
        404:
            description: Animal not found
    """
    global animals
    animals = [animal for animal in animals if animal['id'] != animal_id]
    return jsonify({'message': 'Animal deleted'}), 200


@app.route('/employees', methods=['GET'])
def get_employees():
    """
    Get Employees list
    ---
    responses:
        200:
            description: Getting list of employees
    """
    return jsonify(employees), 200

@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    """
    Get Employee details
    ---
    parameters:
        - name: employee_id
          in: path
          type: integer
          required: true
          description: The ID of the employee to retrieve
    responses:
        200:
            description: Employee details retrieved successfully
        404:
            description: Employee not found
    """
    employee = next((employee for employee in employees if employee['id'] == employee_id), None)
    return jsonify(employee) if employee else (jsonify({'message': 'Employee not found'}), 404)

@app.route('/employees', methods=['POST'])
def create_employee():
    """
    Create a new Employee
    ---
    parameters:
        - name: body
          in: body
          required: true
          schema:
            id: Employee
            required:
              - name
              - email
              - phone
              - role
              - schedule
            properties:
              name:
                type: string
                description: The name of the employee
              email:
                type: string
                format: email
                description: The email address of the employee
              phone:
                type: string
                description: The phone number of the employee
              role:
                type: string
                description: The role of the employee
              schedule:
                type: string
                description: The schedule of the employee
    responses:
        201:
            description: New employee created successfully
    """
    new_employee = request.get_json()
    new_employee['id'] = len(employees) + 1
    employees.append(new_employee)
    return jsonify(new_employee), 201

@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    """
    Update an Employee
    ---
    parameters:
        - name: employee_id
          in: path
          type: integer
          required: true
          description: The ID of the employee to update
        - name: body
          in: body
          required: true
          schema:
            id: Employee
            properties:
              name:
                type: string
                description: The name of the employee
              email:
                type: string
                format: email
                description: The email address of the employee
              phone:
                type: string
                description: The phone number of the employee
              role:
                type: string
                description: The role of the employee
              schedule:
                type: string
                description: The schedule of the employee
    responses:
        200:
            description: Employee updated successfully
        404:
            description: Employee not found
    """
    employee = next((employee for employee in employees if employee['id'] == employee_id), None)
    if employee:
        data = request.get_json()
        employee.update(data)
        return jsonify(employee), 200
    return jsonify({'message': 'Employee not found'}), 404

@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    """
    Delete an Employee
    ---
    parameters:
        - name: employee_id
          in: path
          type: integer
          required: true
          description: The ID of the employee to delete
    responses:
        200:
            description: Employee deleted successfully
        404:
            description: Employee not found
    """
    global employees
    employees = [employee for employee in employees if employee['id'] != employee_id]
    return jsonify({'message': 'Employee deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)