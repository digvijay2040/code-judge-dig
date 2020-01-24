from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class Quiz_model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)

    def to_dict(self):
        quiz = {}
        for column in self.__table__.columns:
            quiz[column.name] = getattr(self, column.name)
        return quiz

class Question_model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    options = db.Column(db.String(300))
    correct_option = db.Column(db.Integer)
    quiz = db.Column(db.Integer, db.ForeignKey('quiz_model.id'))
    points = db.Column(db.Integer)

    def to_dict(self):
        question = {}
        for column in self.__table__.columns:
            question[column.name] = getattr(self, column.name)
        return question

def initiate_db():
    print("Creating database")
    db.create_all()
    print('database created')