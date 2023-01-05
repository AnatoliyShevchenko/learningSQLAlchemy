from flask import Flask, render_template, redirect, request
from datetime import datetime
from app import app, db
from services import Connecting
from werkzeug.security import check_password_hash


conn:Connecting = Connecting()

conn.create_superuser('genitalgrinder90@gmail.com', 'Brick92', '123456-qwe')

admin_id = ''

@app.route('/')
def main():
    return ('<h1>Not Yet</h1>')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    message = ''
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        check = conn.check_admin_login(login)
        if not check:
            message = 'Ты не админ, Вали отсюда'
            return render_template('admin.html', message=message)
        else:
            hash = check_password_hash(check[3], password)
            if login == check[2] and hash == False:
                message = 'Неправильный пароль'
                return render_template('admin.html', message=message)
            elif login == check[2] and hash == True:
                admin_id = check[0]
                return redirect('/admin/ok')
    return render_template('admin.html')

@app.route('/admin/ok')
def admin_ok():
    return ('<h2><a href="/admin/ok/set-genres">Добавьте жанры</a></h2><h2><a href="/admin/ok/add-game">Добавьте игры</h2><h2><a href="/admin/ok/add-key">Добавить ключи</a></h2>')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=4444)