# from flask import Flask, escape, request, render_template
import flask
import datetime
import platform
import os

app = flask.Flask(__name__)


@app.route('/')
def hello():
    name = flask.request.args.get("name", "Flask App")
    time = datetime.datetime.now()
    python_version = platform.python_version()
    aws_platform = os.environ.get('PLATFORM', 'Amazon Web Services')
    return flask.render_template('hello.html',
                                 platform=aws_platform,
                                 flask_version=flask.__version__,
                                 python_version=python_version,
                                 flask_url='https://palletsprojects.com/p/flask/',
                                 time=time,
                                 name=name)

@app.route('/factorial')
def factorial():
    num = flask.request.args.get('num')
    factorialOutput = factorial(int(num))
    time = datetime.datetime.now()
    python_version = platform.python_version()
    aws_platform = os.environ.get('PLATFORM', 'Amazon Web Services')
    return flask.render_template('Factorial.html',
                                 time=time,
                                 factorialOutput=factorialOutput)
def factorial(n):
    return 1 if (n==1 or n<=0) else n * factorial(n - 1);


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )
