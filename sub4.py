from flask import Blueprint

# Blueprintのオブジェクトを生成する
app = Blueprint('func1', __name__)

@app.route('/sub1')
def sub1():
    return 'sub1'