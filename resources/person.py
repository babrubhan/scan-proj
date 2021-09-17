from flask import Response, request
from database.models import Person, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, PersonAlreadyExistsError, InternalServerError, \
    UpdatingPersonError, DeletingPersonError, PersonNotExistsError


class PersonsApi(Resource):
    def get(self):
        query = Person.objects()
        persons = Person.objects().to_json()
        return Response(persons, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            person = Person(**body, added_by=user)
            person.save()
            user.update(push__persons=person)
            user.save()
            id = person.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise PersonAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class PersonApi(Resource):
    @jwt_required()
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            person = Person.objects.get(id=id, added_by=user_id)
            body = request.get_json()
            Person.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingPersonError
        except Exception:
            raise InternalServerError

    @jwt_required()
    def delete(self, id):
        try:
            user_id = get_jwt_identity()
            person = Person.objects.get(id=id, added_by=user_id)
            person.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingPersonError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            persons = Person.objects.get(id=id).to_json()
            return Response(persons, mimetype="application/json", status=200)
        except DoesNotExist:
            raise PersonNotExistsError
        except Exception:
            raise InternalServerError
