from .person import PersonsApi, PersonApi
from .auth import SignupApi, LoginApi


def initialize_routes(api):
    api.add_resource(PersonsApi, '/api/vi/persons')
    api.add_resource(PersonApi, '/api/v1/person/<id>')

    api.add_resource(SignupApi, '/api/v1/auth/signup')
    api.add_resource(LoginApi, '/api/v1/auth/login')
