from flask import Flask
from flask import render_template, redirect, url_for
from flask import request, session, jsonify
import requests
import random
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

@app.route('/assignment11/users')
def assignment11_func():
    query = ' select * from users;'
    users = interact_db(query=query, query_type='fetch')
    response = jsonify(users)
    return response


def get_user(num):
    res = requests.get(f'https://reqres.in/api/users/{num}')
    res = res.json()
    return res


@app.route('/assignment11/outer_source')
def assignment11_func1():
    num = 3
    if "number" in request.args:
        num = int(request.args['number'])
    user = get_user(num)
    return render_template('assignment11_outerSource.html', User=user)


@app.route('/assignment12/restapi_users', defaults={'user_id': 12})
@app.route('/assignment12/restapi_users/<int:user_id>')
def get_users_func(user_id):
    query = 'select * from users where id=%s;' % user_id
    users = interact_db(query=query, query_type='fetch')
    if len(users) == 0:
        return_dict = {
            'status': 'failed',
            'message': 'user not found'
        }
    else:
        return_dict = {
            'status': 'success',
            f'id': users[0].id,
            'name': users[0].name,
            'email': users[0].email,
        }
    return jsonify(return_dict)


if __name__ == '__main__':
    app.run(debug=True)