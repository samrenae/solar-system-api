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

# @planet_bp.route("/<planet_id>", methods=["GET"])
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)
    
#     return jsonify({
#         "id" : planet.id,
#         "name" : planet.name,
#         "planet description" : planet.description,
#         "type" : planet.type
#     })