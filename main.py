from flask import Flask
from flask_restful import Api

from api.User import CreateUser, UpdateUser, DeleteUser, GetUserToken, GetUser, ValidateUser
from api.basics import HelloWorld, Echo, CheckAPI
from mail.mail import get_mail

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'TVNQUl9DYWZlOmVwc2kyMDIz'

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'natsu.974.tm@example.com'
app.config['MAIL_PASSWORD'] = 'Branchie29canardindien190'

mail = get_mail(app=app)

####### Test Appel API Basique

api.add_resource(HelloWorld, '/')
api.add_resource(CheckAPI, '/check')
api.add_resource(Echo, '/echo')

####### API User qui récupère nos usagers et les stockes

api.add_resource(CreateUser, '/create_user')
api.add_resource(UpdateUser, '/update_user/<string:user_id>')
api.add_resource(DeleteUser, '/delete_user/<string:user_id>')
api.add_resource(GetUser, '/get_user/<string:user_id>')
api.add_resource(GetUserToken, '/get_user_token')
api.add_resource(ValidateUser, '/validate_user/<string:user_id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=("C:\\Users\\thalg\\PycharmProjects\\CERTI2\\server.crt",
                                                                "C:\\Users\\thalg\\PycharmProjects\\CERTI2\\server.key"))
