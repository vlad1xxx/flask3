from flask import Flask, render_template
from data import db_session
from data.users import Jobs, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def main():
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template('index.html', jobs=jobs)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
