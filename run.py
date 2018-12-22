import flask
from Entities.config import config
from DAL.DatabaseConfig import DatabaseConfig
print("Trying to run python project: "+config.projectTitle)
print("Project is running...")

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "Jacco stinkt"

app.run()