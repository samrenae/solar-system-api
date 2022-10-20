
from flask import Blueprint,jsonify
class Planet():
    def __init__(self, id, name, description, type):
        self. id = id
        self.name = name
        self.description = description
        self.type = type

planets = [
    Planet(1, "Mercury", "", "terrestrial"),
    Planet(2, "Venus", "", "terrestrial"),
    Planet(3, "Earth", "", "terrestrial"),
]

planet_bp = Blueprint("planet_bp",__name__, url_prefix="/planet")
@planet_bp.route("", methods=["GET"])

def get_all_planets():
    response = []
    for planet in planets:
        planet_dict = {
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "type" : planet.type
        }
        response.append(planet_dict)
    return jsonify(response), 200