from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, TextAreaField, FileField, SelectField
from wtforms.validators import DataRequired, Email, Length, Optional
from flask_wtf.file import FileRequired, FileAllowed
from models import Category

#==================================================
# フォーム
#==================================================

#新規作成
class RegistrationForm(FlaskForm):
    username = StringField('ユーザー名', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('メールアドレス', validators=[DataRequired(), Email(), Length(max=255)])
    password = PasswordField('パスワード', validators=[DataRequired(), Length(min=6,max=255)])
    faculty = StringField('学部', validators=[Optional(),Length(max=20)])
    year = IntegerField('年次', validators=[Optional()])
    submit = SubmitField('新規作成')

#ログイン
class LoginForm(FlaskForm):
    email = StringField('メールアドレス', validators=[DataRequired(), Email(), Length(max=255)])
    password = PasswordField('パスワード', validators=[DataRequired(), Length(min=6,max=255)])
    submit = SubmitField('ログイン')

#投稿
class PostForm(FlaskForm):
    message = TextAreaField('内容')
    image = FileField('画像', validators=[
        DataRequired(), 
        FileAllowed(['jpg', 'png', 'jpeg'], '画像ファイル（"jpg","png","jpeg"）のみ！')
    ])
    category = SelectField('カテゴリ', coerce=int, validators=[DataRequired()])

#コメント
class CommentForm(FlaskForm):
    content = TextAreaField('コメント', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('送信')