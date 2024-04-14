from flask import Flask, render_template, redirect
from data import db_session
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, TextAreaField, EmailField, StringField
from wtforms.validators import DataRequired
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class RegisterForm(FlaskForm):
    login = EmailField('Login / email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    re_password = PasswordField('Password', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/register', methods=['GET', 'POST'])
def main():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.re_password.data:
            return render_template('index.html', title='Register form',
                                   form=form,
                                   message='Пароли не совпадают')
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.login.data).first():
            return render_template('index.html', title='Регистрация',
                                   form=form,
                                   message='Такой пользователь уже есть')
        user = User(
            email=form.login.data,
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/complete')
    return render_template('index.html', title='Регистрация', form=form)


@app.route('/complete')
def complete():
    return render_template('complete.html', title='Регистрация')


if __name__ == '__main__':
    db_session.global_init('db/blogs.db')
    app.run(port=8000, host='127.0.0.1')
