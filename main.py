from flask import Flask
import sub1
import sub2

app = Flask(__name__)
# 分割したblueprintを登録する
app.register_blueprint(sub1.app)
app.register_blueprint(sub2.app)

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)