import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)

# ==================================================
# Flaskに対する設定
# ==================================================
# 乱数を設定
app.config['SECRET_KEY'] = os.urandom(24)
base_dir = os.path.dirname(__file__)
database = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# データベースの設定
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# モデルのインポート（循環インポートを避けるため、ここで行う）
from models import init_db

# データベースの初期化
with app.app_context():
    init_db()

# ==================================================
# 実行
# ==================================================
if __name__ == '__main__':
    app.run()