from os.path import join, dirname, realpath
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from resources.errors import errors

app = Flask(__name__)
# app.config.join(dirname(realpath(__file__)), './.env')
app.config.from_envvar('ENV_FILE_LOCATION')

# imports requiring app
# from resources.routes import initialize_routes

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3500)
# app.run(port=3500)
