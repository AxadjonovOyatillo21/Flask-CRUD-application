from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    phone = db.Column(db.String(25), nullable = False)
    

    def __repr__(self):
        return '<User %r>' % self.id 