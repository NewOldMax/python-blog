from flask.ext.login import LoginManager
from flask.ext.openid import OpenID

from rom import util

from server import app

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)