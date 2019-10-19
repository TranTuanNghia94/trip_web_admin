from flask import *
from flask_bootstrap import Bootstrap
from .data.database import DB
from .form.user_form import RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456790'
Bootstrap(app)
db = DB.init('user')


def check_password(data_1, data_2):
    return check_password_hash(data_1, data_2)


def convert_json(data):
    return list(data)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['Username']
        password = request.form['Password']
        result = db.find({'username': username}, {'_id': 0, 'password': 1})
        if result.count() > 0:
            data = convert_json(result)
            if check_password(data[0].get('password'), password):
                session['login'] = True
                return redirect('/admin')
            else:
                flash('wrong password')
        else:
            flash('this user is not exist')
    return render_template('login.html')


@app.route('/admin', methods=['GET', 'POST'])
def register():
    if session.get('login'):
        form = RegistrationForm()
        if form.is_submitted():
            if form.validate_on_submit():
                db.save(RegistrationForm().convert_to_json())
        return render_template('index.html', form=form)
    else:
        return redirect('/')


@app.route('/users')
def users():
    if session.get('login'):
        list_users = DB.get_all('user')
        return render_template('users.html', user=list_users)
    else:
        return redirect('/')


@app.route('/logout')
def logout():
    session['login'] = False
    return redirect('/')

if __name__ == '__main__':
    app.run()
