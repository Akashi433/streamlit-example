from flask import Flask
from pinterest_routes import pinterest_routes

app = Flask(__name__)

# Register blueprint for Pinterest routes
app.register_blueprint(pinterest_routes)

if __name__ == '__main__':
    app.run(debug=True)
