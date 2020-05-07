from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Home Page</h1>"

@app.route('/about')
def about():
    return "<h1>About Page</h1>"

@app.route('/main')
def mainpage():
    return "<h1>Main Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)