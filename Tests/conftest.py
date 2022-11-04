import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planets import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()
    with app.app_context():
        db.create_all()
        yield app
    with app.app_context():
        db.drop_all()
    
@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_planets(app):
    planet1 = Planet(
        name = "Mercury", 
        description = "Closest planet to sun, in the Milky Way Galaxy. Mercury has no moons and has a thin atmosphere.", 
        type = "terrestrial")
    planet2 = Planet(
        name = "Venus", 
        description = "Second planet from the sun, in the Milky Way Galaxy. Venus is dominated by volcanoes, impact craters, and sedimentation landforms.", 
        type = "terrestrial"
    )
    db.session.add(planet1)
    db.session.add(planet2)

    db.session.commit()
    