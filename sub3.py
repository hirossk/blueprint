from flask import Blueprint

# Blueprintのオブジェクトを生成する
app = Blueprint('func3', __name__)

@app.route('/sub3')
def sub1():
    return 'sub3'