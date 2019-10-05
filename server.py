import flask
from main import *
from flask import jsonify

app = Flask(__name__)

@app.route("/fetch")
def fetch():
	print(a)
	return flask.jsonify(a)


if __name__ == "__main__":
	app.run()


    