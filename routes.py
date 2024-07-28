from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from app import app, db
from models import User, Post, Like, Comment, Category
from forms import RegistrationForm, LoginForm, PostForm, CommentForm
from sqlalchemy import desc
import os

# ==================================================
# ルーティング
# ==================================================
@app.route('/')
def index():
    return redirect(url_for('login'))

# ホーム画面(投稿一覧画面)
@app.route('/home', methods=['GET', 'POST'])
# @login_required ログイン機能実装後（ログインしていないとlogin.htmlに遷移）
def home():
    form = PostForm()
    form.category.choices = [(c.id, c.name) for c in Category.query.all()]
    
    if form.validate_on_submit():
        message = form.message.data
        category_id = form.category.data
        
        # 画像の保存
        image_path = None
        if form.image.data:
            image = form.image.data
            filename = secure_filename(image.filename)
            image_folder = app.config['UPLOAD_FOLDER']
            if not os.path.exists(image_folder):
                os.makedirs(image_folder)
            image_path = os.path.join('uploads', filename)
            image.save(os.path.join(image_folder, filename))

        #ログイン実装後 -> user_id=current_user.id
        post = Post(message=message, image_path=f'uploads/{filename}', category_id=category_id)
        
        db.session.add(post)
        db.session.commit()
        
        return redirect(url_for('home'))
    
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('home.html', form=form, posts=posts)

# ユーザー登録
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=form.password.data,
            faculty=form.faculty.data,
            year=form.year.data
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# ログイン
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password_hash == form.password.data:
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html', form=form)

# ログアウト
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
