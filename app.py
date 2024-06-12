# main.py
from flask import Flask
from flasgger import Swagger
from animals import animals_bp
from employees import employees_bp

app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(animals_bp)
app.register_blueprint(employees_bp)

if __name__ == '__main__':
    app.run(debug=True)
