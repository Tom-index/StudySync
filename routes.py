from flask import render_template, request, redirect, url_for, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from app import app, db
from models import User, Post, Like, Comment, Category
from forms import RegistrationForm, LoginForm, PostForm, CommentForm
import os


# ==================================================
# ルーティング
# ==================================================

# ホーム画面(投稿一覧画面)
@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
    form = PostForm()
    comment_form = CommentForm()
    categories = Category.query.all()
    form.category.choices = [(c.id, c.name) for c in categories]
    
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

        post = Post(message=message, image_path=f'uploads/{filename}', category_id=category_id, user_id=current_user.id)
        
        db.session.add(post)
        db.session.commit()
        
        return redirect(url_for('home'))
    
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('home.html', form=form, comment_form=comment_form, posts=posts, categories=categories, current_user=current_user)

# 投稿削除
@app.route('/delete_post/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    if post:
        comments = Comment.query.filter_by(post_id=post_id).all()
        for comment in comments:
            db.session.delete(comment)
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('home'))

# コメント追加
@app.route('/comment/<int:post_id>', methods=['POST'])
@login_required
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    text = request.form.get('text')
    if text:
        comment = Comment(text=text, user_id=current_user.id, post_id=post_id)
        db.session.add(comment)
        db.session.commit()
        return jsonify({'status': 'success', 'comment': {'text': comment.text, 'username': current_user.username}})
    return jsonify({'status': 'error', 'message': 'コメントを入力してください'})

# コメント取得
@app.route('/comments/<int:post_id>', methods=['GET'])
def get_comments(post_id):
    comments = Comment.query.filter_by(post_id=post_id).all()
    comments_data = [{'text': comment.text, 'username': comment.user.username} for comment in comments]
    return jsonify({'status': 'success', 'comments': comments_data})

# ユーザー登録
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    form.year.choices = [(None, ''),('1',1), ('2',2),('3',3),('4',4)]
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
