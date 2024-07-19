from .app import db

#==================================================
# モデル
#==================================================
class User(db.Model):
    # テーブル名
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    faculty = db.Column(db.String(20))
    year = db.Column(db.Integer)