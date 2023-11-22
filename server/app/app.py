from flask import Flask
from flask_cors import CORS
from routes import user_routes, asset_routes  
from auth import jwt  

# Create a Flask app
app = Flask(__name__)

# Configure CORS to allow cross-origin requests if needed
CORS(app)

# Configure Flask-JWT-Extended for authentication
# Replace with your secret key
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt.init_app(app)

# Register your route blueprints
app.register_blueprint(user_routes)
app.register_blueprint(asset_routes)

# Define a root route for testing purposes


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
