from flask import Blueprint

# Blueprintのオブジェクトを生成する
app = Blueprint('func2', __name__)

@app.route('/sub2')
def sub2():
    return 'sub2'