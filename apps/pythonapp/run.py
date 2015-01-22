from flask import Flask
import requests
from flask import render_template
from operator import itemgetter

app = Flask(__name__)


@app.route('/')
def get_jenkins_stuff():
    try:
        # general apache url with lots of colors and jobs
        # url = "https://builds.apache.org/api/json?pretty=true"
        # LR builds
        url = "http://54.148.201.225:8080/api/json?pretty=true"
        response = requests.get(url)
        stuff = response.json()['jobs']
        # sort the array by the color tag (alphabetically)
        sorted_stuff = sorted(stuff, key=itemgetter('color'), reverse=True)

    except Exception, e:
        # it went wrong so send back some information for debug
        return render_template("error.html", error=e)

    return render_template("index.html", results=sorted_stuff)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
