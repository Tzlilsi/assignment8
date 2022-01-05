from flask import Flask
from flask import render_template, redirect, url_for
from flask import request, session
from interact_with_DB import *


app = Flask(__name__)
app.secret_key = '12345'

@app.route('/home_page')
@app.route('/home')
@app.route('/')
def home_func():  # put application's code here
    return render_template('CV.html')
    nickname = session.get('nickname')
    return render_template('CV.html', nickname=nickname)


@app.route('/assignment8')
def assignment8_func():  # put application's code here
    return render_template('assignment8.html', films=('Drama', 'Documentary', 'Cartoon'),
                           Hobbies=['Painting', 'Dancing', 'SQL'])
    nickname = session.get('nickname')
    return render_template('forms.html', nickname=nickname)


users = {'user1': {'name': 'Tzlil', 'email': 'tzlilsimka@gmail.com'},
        'user2': {'name': 'Daniel', 'email': 'daniel1@gmail.com'},
        'user3': {'name': 'Limor', 'email': 'limor@gmail.com'},
        'user4': {'name': 'Tali', 'email': 'Tali776@gmail.com'},
        'user5': {'name': 'Liam', 'email': 'Liam@gmail.com'},
         'user6' : {'name': 'Roy', 'email': 'Roy69@gmail.com'},
         'user7': {'name': 'Gal', 'email': 'arnon69@gmail.com'}}




@app.route('/assignment9', methods=["get", "post"])
def assignment9_func():
    if request.method == "POST":
        session["nickname"] = request.form.get("nickname")
        return redirect(url_for('assignment9_func'))
    else:
        nickname = session.get('nickname')
        if 'name' in request.args:
            name = request.args['name']
            if name == '':
                return render_template('assignment9.html', users=list(users.values()), nickname=nickname)
            else:
                new_one = []
                for i in users.values():
                    if i['name'] == name:
                        new_one.append(i)
                return render_template('assignment9.html', users=new_one, nickname=nickname)
        return render_template('assignment9.html', nickname=nickname)


@app.route('/logout')
def logout():
    session['nickname'] = None
    return redirect(url_for('home'))

## assignment10
from assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)
