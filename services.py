from werkzeug.security import generate_password_hash
from typing import Any
from models import (
    Users, 
    UserGames, 
    Basket, 
    GameGenres, 
    Games, 
    Genres, 
    Codes, 
    Admin,
)
from app import db, app


class Connecting():
    def __new__(cls: type[Any]):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Connecting, cls).__new__(cls)

        return cls.instance

    def create_superuser(self, email, login, password):
        try:
            hash = generate_password_hash(password)
            admin:Admin = Admin(
                email=f'{email}', 
                login=f'{login}', 
                password=hash
                )
            with app.app_context():
                db.session.add(admin)
                db.session.commit()
            print('Пользователь создан!')
        except:
            print('must be only one!')

    def check_admin_login(self, login):
        with app.app_context():
            data = Admin.query.filter_by(login = f'{login}').first()
        result = f'{data.id}, {data.email}, {data.login}, {data.password}'
        result_list = result.split(', ')
        print(result_list)
        return result_list