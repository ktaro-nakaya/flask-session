from flask import Flask
from counter import bp_counter

# Flaskのインスタンス生成
app = Flask(__name__, static_url_path='/')

# Sessionの暗号化キー
app.secret_key = b'abcdefghijklmn'

# カウントするモジュールを登録
app.register_blueprint(bp_counter)


if __name__=='__main__':
    app.run()