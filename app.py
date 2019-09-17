from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
import json

app = Flask(__name__)
api = Api(app, prefix="/api/v1")
auth = HTTPBasicAuth()

USER_DATA = {
    "admin": "SuperSecretPwd"
}


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password


class PrivateResource(Resource):
    @auth.login_required
    def get(self):
        with open('response.txt') as json_file:
            data = json.load(json_file)
            print(data)
            print(type(data))
        return data


api.add_resource(PrivateResource, '/private')

if __name__ == '__main__':
    app.run(debug=True)

