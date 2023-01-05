from flask import Flask, render_template, redirect, request
from datetime import datetime
from app import app, db
from models import Users


@app.route('/')
def main():
    return ('<h1>Not Yet</h1>')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=4444)