from flask import Blueprint, jsonify, request
from flasgger import swag_from

feedings_bp = Blueprint('feedings', __name__)

feeding_schedules = [
    {"id": 1, "terminal_id": 101, "enclosure_id": 1, "food_type": "Meat", "feeding_time": "09:00"},
    {"id": 2, "terminal_id": 102, "enclosure_id": 2, "food_type": "Vegetables", "feeding_time": "10:00"},
]

@feedings_bp.route('/feedings', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Retrieve a list of all feeding schedules in the zoo.',
            'schema': {
                'type': 'array',
                'items': {
                    '$ref': '#/definitions/FeedingSchedule'
                }
            }
        }
    }
})
def get_feedings():
    return jsonify(feeding_schedules), 200

@feedings_bp.route('/feedings/<int:feeding_id>', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'feeding_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the feeding schedule to retrieve'
        }
    ],
    'responses': {
        200: {
            'description': 'Retrieve a specific feeding schedule by its id.',
            'schema': {
                '$ref': '#/definitions/FeedingSchedule'
            }
        },
        404: {
            'description': 'Feeding schedule not found'
        }
    }
})
def get_feeding(feeding_id):
    feeding = next((f for f in feeding_schedules if f['id'] == feeding_id), None)
    return jsonify(feeding) if feeding else (jsonify({'message': 'Feeding schedule not found'}), 404)

@feedings_bp.route('/feedings', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                '$ref': '#/definitions/FeedingSchedule'
            }
        }
    ],
    'responses': {
        201: {
            'description': 'New feeding schedule created successfully',
            'schema': {
                '$ref': '#/definitions/FeedingSchedule'
            }
        }
    }
})
def create_feeding():
    new_feeding = request.get_json()
    new_feeding['id'] = len(feeding_schedules) + 1
    feeding_schedules.append(new_feeding)
    return jsonify(new_feeding), 201

@feedings_bp.route('/feedings/<int:feeding_id>', methods=['PUT'])
@swag_from({
    'parameters': [
        {
            'name': 'feeding_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the feeding schedule to update'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                '$ref': '#/definitions/FeedingSchedule'
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Feeding schedule updated successfully',
            'schema': {
                '$ref': '#/definitions/FeedingSchedule'
            }
        },
        404: {
            'description': 'Feeding schedule not found'
        }
    }
})
def update_feeding(feeding_id):
    feeding = next((f for f in feeding_schedules if f['id'] == feeding_id), None)
    if feeding:
        data = request.get_json()
        feeding.update(data)
        return jsonify(feeding), 200
    return jsonify({'message': 'Feeding schedule not found'}), 404

@feedings_bp.route('/feedings/<int:feeding_id>', methods=['DELETE'])
@swag_from({
    'parameters': [
        {
            'name': 'feeding_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the feeding schedule to delete'
        }
    ],
    'responses': {
        204: {
            'description': 'Feeding schedule deleted successfully'
        },
        404: {
            'description': 'Feeding schedule not found'
        }
    }
})
def delete_feeding(feeding_id):
    global feeding_schedules
    feeding_schedules = [f for f in feeding_schedules if f['id'] != feeding_id]
    return jsonify({'message': 'Feeding schedule deleted'}), 204

definitions = {
    'FeedingSchedule': {
        'type': 'object',
        'properties': {
            'id': {'type': 'integer'},
            'terminal_id': {'type': 'integer'},
            'enclosure_id': {'type': 'integer'},
            'food_type': {'type': 'string'},
            'feeding_time': {'type': 'string'}
        }
    }
}
