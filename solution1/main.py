from flask import Flask, render_template
from solution1.data import db_session
from solution1.data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("solution1/db/blogs.db")
    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    captain = User()
    captain.surname = 'Scott'
    captain.name = 'Ridley'
    captain.age = 21
    captain.position = 'captain'
    captain.speciality = 'research engineer'
    captain.address = 'module_1'
    captain.email = 'scott_chief@mars.org'
    captain.hashed_password = '111'
    db_sess.add(captain)

    member1 = User()
    member1.surname = 'Scott'
    member1.name = 'Travis'
    member1.age = 52
    member1.position = 'member'
    member1.speciality = 'engineer'
    member1.address = 'module_2'
    member1.email = 'travis@outlook.org'
    member1.hashed_password = '111'
    db_sess.add(member1)

    member2 = User()
    member2.surname = 'Michael'
    member2.name = 'Jordan'
    member2.age = 67
    member2.position = 'member'
    member2.speciality = 'engineer'
    member2.address = 'module_3'
    member2.email = 'jordan@mail.org'
    member2.hashed_password = '111'
    db_sess.add(member2)

    member3 = User()
    member3.surname = 'Kylian'
    member3.name = 'Mbappe'
    member3.age = 26
    member3.position = 'member'
    member3.speciality = 'engineer'
    member3.address = 'module_4'
    member3.email = 'mbapPe@gmail.org'
    member3.hashed_password = '111'
    db_sess.add(member3)
    db_sess.commit()
    return render_template('base.html')


if __name__ == '__main__':
    main()
