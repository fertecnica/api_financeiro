from flask import Flask

app = Flask(__name__)

from calls import calls as calls_blueprint

app.register_blueprint(calls_blueprint)

with app.app_context():
    if __name__ == '__main__':
        app.run(debug=True,port=6700,host="0.0.0.0")