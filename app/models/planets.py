from app import db

class Planet(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    type = db.Column(db.String)

    def to_dict(self):
        planet_dict = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "type": self.type
        }
        return planet_dict
    
    @classmethod
    def from_dict(cls, data_dict):
        if "name" in data_dict and "description" in data_dict and "type" in data_dict:
            new_planet = cls(name=data_dict["name"],
            description=data_dict["description"],
            type=data_dict["type"])

            return new_planet