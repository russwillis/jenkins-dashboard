from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_jenkins_stuff():
    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
