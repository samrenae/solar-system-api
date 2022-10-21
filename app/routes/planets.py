from http.cookies import BaseCookie
from flask import Blueprint,jsonify, abort, make_response

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        abort(make_response({"message": f"planet {planet_id} invalid"}, 400))
    
    for planet in planets:
        if planet.id == planet_id:
            return planet
    abort(make_response({"message": f"planet {planet_id} not found."}, 404))

class Planet():
    def __init__(self, id, name, description, type):
        self. id = id
        self.name = name
        self.description = description
        self.type = type

planets = [
    Planet(1, "Mercury", "Closest planet to sun, in the Milky Way Galaxy. Mercury has no moons and has a thin atmosphere.", "terrestrial"),
    Planet(2, "Venus", "Second planet from the sun, in the Milky Way Galaxy. Venus is dominated by volcanoes, impact craters, and sedimentation landforms.", "terrestrial"),
    Planet(3, "Earth", "Third planet from the sun, in the Milky Way Galaxy. Earth has one moon, and is covered in 70% water.", "terrestrial"),
    Planet(4, "Mars", "Fourth planet from the sun, in the Milky Way Galaxy. Mars is a dusty, cold desert with a very thin atmosphere.", "terrestrial"),
    Planet(5, "Jupiter", "Fifth planet from the sun, in the Milky Way Galaxy. Jupiter is covered in cloud stripes and big storms (Great Red Spot) and is a gas giant with no solid surface.", "jovian"),
    Planet(6, "Saturn", "Sixth planet from the sun, in the Milky Way Galaxy. Saturn is a gas giant made of mostly hydrogen and helium, and has dozens of moons and the most complex rings.", "jovian"),
    Planet(7, "Uranus", "Seventh planet from the sun, in the Milky Way Galaxy. Uranus is an ice giant and is made of water, methan, hydrogen, and helium, and is blue in color.", "jovian"),
    Planet(8, "Neptune", "Eighth planet from the sun, in the Milky Way Galaxy. Neptune is an ice giant and is made of water, ammonia, and methane and has a thick, windy atmosphere.", "jovian"),
    Planet(9, "Pluto", "Ninth planet from the sun, in the Milky Way Galaxy. Pluto is a dwarf planet and is about half the width of the United States of America. It is a real planet.", "dwarf")
]

planet_bp = Blueprint("planet_bp",__name__, url_prefix="/planet")

@planet_bp.route("", methods=["GET"])
def get_all_planets():
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
    planet = validate_planet(planet_id)
    
    return jsonify({
        "id" : planet.id,
        "name" : planet.name,
        "planet description" : planet.description,
        "type" : planet.type
    })