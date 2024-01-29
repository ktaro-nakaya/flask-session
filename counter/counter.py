from flask import (Blueprint, session, jsonify)

# Blueprintのインスタンス生成
bp_counter = Blueprint('counter', __name__, url_prefix='/api/count')

# /でカウントアップするRest APIの定義
@bp_counter.get('/')
def count_up():

    # sessionはdic型なのでキーが存在するか確認
    if 'count' in session:
        # すでにキーが存在する場合はカウントアップ
        current_count = session['count'] + 1
        session['count'] = current_count
    else:
        # キーが存在しない場合は初期値を格納
        session['count'] = 1

    # レスポンスのメッセージを生成してJSONに変換してHTTPステータスコード200で返す
    message = {'number': session['count']}

    return jsonify(message), 200
