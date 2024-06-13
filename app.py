from flask import Flask
from flasgger import Swagger
from animals import animals_bp
from employees import employees_bp
from reports import reports_bp
from feedings import feedings_bp

def create_app():
    app = Flask(__name__)
    swagger = Swagger(app)

    # Register blueprints
    app.register_blueprint(animals_bp)
    app.register_blueprint(employees_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(feedings_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
