from flask import Flask
import jenkins
import sys

app = Flask(__name__)

@app.route('/')
def get_jenkins_stuff():
    try:
        # Jenkins(url, username, password)
        j = jenkins.Jenkins('https://builds.apache.org/')

        info = j.get_info()
        jobs = info['jobs']
    except jenkins.JenkinsException, e:
        #it went wrong so send back some information for debug
        return '<p>Error reported from request:</p><p> %s</p>' % (e)

    #Everything worked so return an OK message
    #return '<p>OK</p><p> %s </p>' % (jobs[0])

    #lets do a litle debug print out to see what we've got
    return '<p> %s </p>' % (info)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
