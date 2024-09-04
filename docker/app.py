from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! This is a simple Flask app running in a Docker container."

@app.route('/about')
def about():
    return "This is the about page of our Flask app."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
