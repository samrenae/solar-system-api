from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    from .routes.planets import planet_bp
    app.register_blueprint(planet_bp)

    return app
