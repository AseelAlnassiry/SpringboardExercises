from flask import Flask, request
import operations

app = Flask(__name__)


@app.route('/add')
def add():
    a, b = int(request.args['a']), int(request.args['b'])
    return str(operations.add(a, b))


@app.route('/sub')
def sub():
    a, b = int(request.args['a']), int(request.args['b'])
    return str(operations.sub(a, b))


@app.route('/mult')
def mult():
    a, b = int(request.args['a']), int(request.args['b'])
    return str(operations.mult(a, b))


@app.route('/div')
def div():
    a, b = int(request.args['a']), int(request.args['b'])
    return str(operations.div(a, b))
