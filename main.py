import imp
from flask import Flask, request

from user.dto.user_register_request import UserRegisterRequest
from user.service.user_service import UserService
from user.service.exception import UserExistsException
from user.repository.user_repository import UserRepository
app = Flask(__name__)


@app.route("/")
def index():
    message = "<h1> Code-Server-API 首页<h1>"
    return message


@app.route("/register",methods=["POST"])
def register():
    body = request.get_json()
    username = body["username"]
    password = body["password"]
    user_register_request=UserRegisterRequest(username,password)

    user_repository = UserRepository()

    user_service=UserService(user_repository)
    try :
        user_service.register(user_register_request)

        return "OK",201
    except UserExistsException:
        return "ERROR",500