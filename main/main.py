from flask import Flask, request
from flask import jsonify

# -*- coding: utf-8 -*-
# Flask APP
app = Flask(__name__)


@app.route("/java/maven", methods=["POST"])
def java_maven():
    print("Webhook MAVEN entered \n{0}".format(request))


@app.route("/npm", methods=["POST"])
def npm():
    print("Webhook NPM entered \n{0}".format(request))
    return jsonify([1, 2, 3])


@app.route("/", methods=["GET"])
def test():
    print("Webhook NPM entered \n{0}".format(request))
    return jsonify([1])


@app.route("/", methods=["POST"])
def test_post():
    print("Webhook NPM POST entered \n{0}".format(request))
    return jsonify([1])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
