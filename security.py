from hmac import compare_digest
from user import UserRepository


def authenticate(username, password):
    user_repository = UserRepository()
    user = user_repository.find_by_username(username)
    if user and compare_digest(user.password, password):
        return user


def identity(payload):
    user_repository = UserRepository()
    user_id = payload['identity']
    return user_repository.find_by_id(user_id)
