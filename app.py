import os
import uuid

from ufrn import system
from infosystem.common import authorization
from infosystem import database
from flask import Flask

app = Flask(__name__)
app.config['BASEDIR'] = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['BASEDIR'] + '/ufrn.db'

database.db.init_app(app)
with app.app_context():
    database.db.drop_all()
    database.db.create_all()

    domain = system.subsystems['domain'].manager.create(data={'name': 'default'})
    user_data = {'name': 'admin', 'email':'admin@example.com', 'password':'123456',
                 'domain_id': domain.id}
    user = system.subsystems['user'].manager.create(data=user_data)
    role = system.subsystems['role'].manager.create(data={'domain_id': domain.id, 'name':'admin'})
    system.subsystems['grant'].manager.create(data={'user_id': user.id, 'role_id':role.id})


for subsystem in system.subsystems.values():
    app.register_blueprint(subsystem)


app.before_request(authorization.protect)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

def load_app():
    return app
