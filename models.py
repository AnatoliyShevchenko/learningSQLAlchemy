from app import db
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    login = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(512))
    wallet = db.Column(db.Float)
    date_reg = db.Column(db.DateTime, default=datetime.utcnow)
    photo = db.Column(db.LargeBinary)

    def __repr__(self):
        return f'<users {self.id}>'


class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    year_of_issue = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<games {self.id}>'


class Genres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<genres {self.id}>'


class GameGenres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))   

    def __repr__(self):
        return f'<gg {self.id}>' 


class Codes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    code = db.Column(db.String, unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<code {self.id}>' 


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    login = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(512))
    date_reg = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.id}'


class UserGames(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    game_key = db.Column(db.String(25), unique=True, nullable=False)

    def __repr__(self):
        return f'<usergames {self.id}>'


class Basket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))

    def __repr__(self):
        return f'<basket {self.id}>'