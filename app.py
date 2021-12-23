from flask import Flask
from flask import render_template, redirect, url_for

app = Flask(__name__)


@app.route('/home_page')
@app.route('/home')
@app.route('/')
def home_func():  # put application's code here
    return render_template('CV.html')


@app.route('/assignment8')
def assignment8_func():  # put application's code here
    return render_template('assignment8.html',films= ('Drama','Documentary','Cartoon'),Hobbies=['Painting','Dancing','SQL'] )


if __name__ == '__main__':
    app.run(debug=True)
