from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://python14:python14@stuq.ceshiren.com:23306/python14'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "seveniruby_user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class TestCase(db.Model):
    __tablename__ = "seveniruby_testcase"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=False)
    data = db.Column(db.String(1024), unique=False, nullable=False)

    def __repr__(self):
        return '<TestCase %r>' % self.name


class TestCaseApi(Resource):
    def get(self):
        return {'hello': 'world'}


class LoginApi(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(TestCaseApi, '/testcase')
api.add_resource(LoginApi, '/login')

if __name__ == '__main__':
    app.run(debug=True)
