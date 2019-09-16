from flask import Flask
import flask

app=Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('home.html')

@app.route('/about')
def about():
    return 'Flask app about page'

if __name__ == '__main__':
    app.run(debug=True)
