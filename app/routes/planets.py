from email import message
from urllib import response
from flask import Blueprint,jsonify, abort, make_response, request
from app import db
from app.models.planets import Planet



# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         abort(make_response({"message": f"planet {planet_id} invalid"}, 400))
    
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
#     abort(make_response({"message": f"planet {planet_id} not found."}, 404))

planet_bp = Blueprint("planet_bp",__name__, url_prefix="/planet")

def get_one_planet_or_abort(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        response_str = f"invalid planet_id: `{planet_id}`.Id must be an integer"
        abort(make_response(jsonify({'message':response_str}), 400))
    matching_planet = Planet.query.get(planet_id)
    if not matching_planet: 
        response_str = f"Planet with id {planet_id} was not found in the database"
        abort(make_response(jsonify({'message':response_str}), 400))
    return matching_planet


@planet_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        type = request_body["type"]
    )
    db.session.add(new_planet)
    db.session.commit()
    return {"id":new_planet.id}, 201


@planet_bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    response = []
    for planet in planets:
        planet_dict = {
            "id" : planet.id,
            "name" : planet.name,
            "planet description" : planet.description,
            "type" : planet.type
        }
        response.append(planet_dict)
    return jsonify(response), 200

@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    chosen_planet = get_one_planet_or_abort(planet_id)
    planet_dict = {
            "id" : chosen_planet.id,
            "name" : chosen_planet.name,
            "planet description" : chosen_planet.description,
            "type" : chosen_planet.type
        }
    return jsonify(planet_dict), 200

@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_one_planet(planet_id):
    chosen_planet = get_one_planet_or_abort(planet_id)
    request_body = request.get_json()
    if "name" not in request_body or \
        "description" not in request_body or \
        "type" not in request_body:
            return jsonify({"message": "request must include name, description, type "}), 400
    chosen_planet.name = request_body["name"]
    chosen_planet.description = request_body["description"]
    chosen_planet.type = request_body["type"]

    db.session.commit()
    return jsonify({"message": f"successfully replaced planet with id{planet_id}"}), 200


@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    chosen_planet = get_one_planet_or_abort(planet_id)
    db.session.delete(chosen_planet)
    db.session.commit()
    return jsonify({"message": f"successfully deleted planet with id{planet_id}"}), 200

