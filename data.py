from generators import *
   
class ResponseCodes:
    created = 201
    server_error = 500
    bad_request = 400
    forbidden = 403
    ok = 200
    redirect = 302
    unauthorized = 401
    not_found = 404

class Responses:

    success = "'success': True"
    fail = "'success': False"
    user_already_exists = {"success": False, "message": "User already exists"}
    user_missing_data = {"success": False, "message": "Email, password and name are required fields"}
    login_missing_data = {"success": False, "message": "email or password are incorrect"}
    order_no_ingredients = {"success": False, "message": "Ingredient ids must be provided"}
    new_location = "/login"
 
class UserGeneratedData:
    correctly_generated = {
        "email": generate_email(),
        "password": generate_password(),
        "name": generate_login()
    }

    login_data = [
        {           # корректные данные логина
        "email": correctly_generated["email"],
        "password": correctly_generated["password"]
        },
        {           # данные входа с неправильным логином
        "email": generate_email(),
        "password": correctly_generated["password"]
        },
        {           # данные входа с неправильным паролем
        "email": correctly_generated["email"],
        "password": generate_password()
        }
    ]

    insufficient_params = [
        {           # данные регистрации без пароля
        "email": generate_email(),
        "password": "",
        "name": generate_login()
        },
        {           # данные регистрации без email
        "email": "",
        "password": generate_password(),
        "name": generate_login()
        },
        {           # данные регистрации без имени
        "email": generate_email(),
        "password": generate_password(),
        "name": ""
        }
    ]

class OrderGeneratedData:
    order_data = {"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]}
    empty_order_data = {"ingredients":[]}
    incorrect_order_data = {"ingredients": ["61c0c5a71d1f82001bdaaa6d","aaaaaaaaaaaaaaa"]}
