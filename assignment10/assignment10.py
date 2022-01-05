from flask import Blueprint, render_template, request, redirect
from interact_with_DB import interact_db

# assignment10 blueprint definition
assignment10 = Blueprint('assignment10', __name__, static_folder='static',  template_folder='templates')


# Routes
@assignment10.route('/assignment10')
def index():
    query = "select * from users;"
    users = interact_db(query= query, query_type='fetch')
    return render_template('assignment10.html',users=users)


@assignment10.route('/insert_user',methods=['post'])
def insert_user_func():
    #get the data
    name = request.form['name']
    email = request.form['email']
    password =request.form['password']

    #insert
    query = "insert into users(name,email,password) values ('%s','%s','%s')"%(name,email,password)
    interact_db(query=query,query_type='commit')
    return redirect('/assignment10')


@assignment10.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['id']
    query = "DELETE FROM users WHERE id = '%s';" % user_id
    interact_db(query=query, query_type='commit')
    return redirect('assignment10')




## update user
@assignment10.route('/Update_users',methods=['POST'])
def Update_users_func():
    user_id = request.form['id']
    name = request.form['name']
    email = request.form['email']
    query = "UPDATE users SET name='%s',email='%s' WHERE id='%s';" % (name, email, user_id)
    interact_db(query=query, query_type='commit')
    return redirect('assignment10')
