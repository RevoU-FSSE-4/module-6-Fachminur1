# animals.py
from flask import Blueprint, jsonify, request
from flasgger import Swagger, swag_from

animals_bp = Blueprint('animals', __name__)

animals = [
    {"id": 1, "species": "Tiger", "age": 5, "gender": "Male", "special_requirements": "Carnivore diet"},
    {"id": 2, "species": "Hippopotamus", "age": 10, "gender": "Female", "special_requirements": "Large enclosure"},
]

@animals_bp.route('/animals', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Getting list of animals',
            'schema': {
                'type': 'array',
                'items': {'$ref': '#/definitions/Animal'}
            }
        }
    },
    'definitions': {
        'Animal': {
            'type': 'object',
            'properties': {
                'id': {'type': 'integer'},
                'species': {'type': 'string'},
                'age': {'type': 'integer'},
                'gender': {'type': 'string'},
                'special_requirements': {'type': 'string'}
            }
        }
    }
})
def get_animals():
    return jsonify(animals), 200

@animals_bp.route('/animals/<int:animal_id>', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'animal_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the animal to retrieve'
        }
    ],
    'responses': {
        200: {
            'description': 'Getting animal details',
            'schema': {'$ref': '#/definitions/Animal'}
        },
        404: {
            'description': 'Animal not found'
        }
    }
})
def get_animal(animal_id):
    animal = next((animal for animal in animals if animal['id'] == animal_id), None)
    return jsonify(animal) if animal else (jsonify({'message': 'Animal not found'}), 404)

@animals_bp.route('/animals', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'id': 'Animal',
                'required': ['species', 'age', 'gender', 'special_requirements'],
                'properties': {
                    'species': {'type': 'string', 'description': 'The species of the animal'},
                    'age': {'type': 'integer', 'description': 'The age of the animal'},
                    'gender': {'type': 'string', 'description': 'The gender of the animal'},
                    'special_requirements': {'type': 'string', 'description': 'Special requirements for the animal'}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'New animal created successfully'
        }
    }
})
def create_animal():
    new_animal = request.get_json()
    new_animal['id'] = len(animals) + 1
    animals.append(new_animal)
    return jsonify(new_animal), 201

@animals_bp.route('/animals/<int:animal_id>', methods=['PUT'])
@swag_from({
    'parameters': [
        {
            'name': 'animal_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the animal to update'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'id': 'Animal',
                'properties': {
                    'species': {'type': 'string', 'description': 'The species of the animal'},
                    'age': {'type': 'integer', 'description': 'The age of the animal'},
                    'gender': {'type': 'string', 'description': 'The gender of the animal'},
                    'special_requirements': {'type': 'string', 'description': 'Special requirements for the animal'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Animal updated successfully'
        },
        404: {
            'description': 'Animal not found'
        }
    }
})
def update_animal(animal_id):
    animal = next((animal for animal in animals if animal['id'] == animal_id), None)
    if animal:
        data = request.get_json()
        animal.update(data)
        return jsonify(animal), 200
    return jsonify({'message': 'Animal not found'}), 404

@animals_bp.route('/animals/<int:animal_id>', methods=['DELETE'])
@swag_from({
    'parameters': [
        {
            'name': 'animal_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the animal to delete'
        }
    ],
    'responses': {
        200: {
            'description': 'Animal deleted successfully'
        },
        404: {
            'description': 'Animal not found'
        }
    }
})
def delete_animal(animal_id):
    global animals
    animals = [animal for animal in animals if animal['id'] != animal_id]
    return jsonify({'message': 'Animal deleted'}), 200
