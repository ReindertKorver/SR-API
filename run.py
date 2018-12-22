import flask
from Entities.config import config
from DAL.DBTestConnection import DBTestConnection
print("Trying to run python project: "+config.projectTitle)
print("Project is running...")

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/users', methods=['GET'])
def home():
    result = DBTestConnection.connectAsTest() 
    return flask.Response(result,mimetype='application/json')

app.run()