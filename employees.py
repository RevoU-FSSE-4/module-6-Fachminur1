# employees.py
from flask import Blueprint, jsonify, request
from flasgger import Swagger, swag_from

employees_bp = Blueprint('employees', __name__)

employees = [
    {"id": 1, "name": "Jason Bourne", "email": "jasonbourne@example.com", "phone": "123-456-7890", "role": "Zookeeper", "schedule": "9-5"},
    {"id": 2, "name": "John Wick", "email": "johnwick@example.com", "phone": "987-654-3210", "role": "Veterinarian", "schedule": "10-6"},
]

@employees_bp.route('/employees', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Getting list of employees',
            'schema': {
                'type': 'array',
                'items': {'$ref': '#/definitions/Employee'}
            }
        }
    },
    'definitions': {
        'Employee': {
            'type': 'object',
            'properties': {
                'id': {'type': 'integer'},
                'name': {'type': 'string'},
                'email': {'type': 'string', 'format': 'email'},
                'phone': {'type': 'string'},
                'role': {'type': 'string'},
                'schedule': {'type': 'string'}
            }
        }
    }
})
def get_employees():
    return jsonify(employees), 200

@employees_bp.route('/employees/<int:employee_id>', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'employee_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the employee to retrieve'
        }
    ],
    'responses': {
        200: {
            'description': 'Getting employee details',
            'schema': {'$ref': '#/definitions/Employee'}
        },
        404: {
            'description': 'Employee not found'
        }
    }
})
def get_employee(employee_id):
    employee = next((employee for employee in employees if employee['id'] == employee_id), None)
    return jsonify(employee) if employee else (jsonify({'message': 'Employee not found'}), 404)

@employees_bp.route('/employees', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'id': 'Employee',
                'required': ['name', 'email', 'phone', 'role', 'schedule'],
                'properties': {
                    'name': {'type': 'string', 'description': 'The name of the employee'},
                    'email': {'type': 'string', 'format': 'email', 'description': 'The email address of the employee'},
                    'phone': {'type': 'string', 'description': 'The phone number of the employee'},
                    'role': {'type': 'string', 'description': 'The role of the employee'},
                    'schedule': {'type': 'string', 'description': 'The schedule of the employee'}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'New employee created successfully'
        }
    }
})
def create_employee():
    new_employee = request.get_json()
    new_employee['id'] = len(employees) + 1
    employees.append(new_employee)
    return jsonify(new_employee), 201

@employees_bp.route('/employees/<int:employee_id>', methods=['PUT'])
@swag_from({
    'parameters': [
        {
            'name': 'employee_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the employee to update'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'id': 'Employee',
                'properties': {
                    'name': {'type': 'string', 'description': 'The name of the employee'},
                    'email': {'type': 'string', 'format': 'email', 'description': 'The email address of the employee'},
                    'phone': {'type': 'string', 'description': 'The phone number of the employee'},
                    'role': {'type': 'string', 'description': 'The role of the employee'},
                    'schedule': {'type': 'string', 'description': 'The schedule of the employee'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Employee updated successfully'
        },
        404: {
            'description': 'Employee not found'
        }
    }
})
def update_employee(employee_id):
    employee = next((employee for employee in employees if employee['id'] == employee_id), None)
    if employee:
        data = request.get_json()
        employee.update(data)
        return jsonify(employee), 200
    return jsonify({'message': 'Employee not found'}), 404

@employees_bp.route('/employees/<int:employee_id>', methods=['DELETE'])
@swag_from({
    'parameters': [
        {
            'name': 'employee_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the employee to delete'
        }
    ],
    'responses': {
        200: {
            'description': 'Employee deleted successfully'
        },
        404: {
            'description': 'Employee not found'
        }
    }
})
def delete_employee(employee_id):
    global employees
    employees = [employee for employee in employees if employee['id'] != employee_id]
    return jsonify({'message': 'Employee deleted'}), 200
