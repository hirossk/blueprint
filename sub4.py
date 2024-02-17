from flask import Blueprint

# Blueprintのオブジェクトを生成する
app = Blueprint('func4', __name__)

@app.route('/sub4')
def sub1():
    return 'sub4'