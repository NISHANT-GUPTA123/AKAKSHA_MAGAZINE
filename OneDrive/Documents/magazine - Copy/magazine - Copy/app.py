# from flask import Flask, render_template

# app = Flask(__name__, static_url_path='/static')

# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
import os
from config import Config
from database import mysql, db, migrate
from models import User, Article, Comment, PhotoOfMonth
from forms import LoginForm, ArticleForm, CommentForm, RegistrationForm
import MySQLdb

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)

# Initialize extensions
mysql.init_app(app)
db.init_app(app)
migrate.init_app(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Utility functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def save_image(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return f'/static/uploads/{filename}'
    return None

# Routes
@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    articles = Article.query.order_by(Article.created_at.desc()).paginate(page=page, per_page=6)
    photo = PhotoOfMonth.query.order_by(PhotoOfMonth.created_at.desc()).first()
    return render_template('index.html', articles=articles, photo=photo)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Create new user
        new_user = User(
            username=form.username.data,
            email=form.email.data
        )
        new_user.set_password(form.password.data)  # Assuming you have a method for hashing passwords
        db.session.add(new_user)
        db.session.commit()
        
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))  # Redirect to login page after signup
    
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/article/new', methods=['GET', 'POST'])
@login_required
def new_article():
    form = ArticleForm()
    if form.validate_on_submit():
        image_url = None
        if 'image' in request.files:
            image_url = save_image(request.files['image'])
            
        article = Article(
            title=form.title.data,
            content=form.content.data,
            category=form.category.data,
            image_url=image_url,
            user_id=current_user.id
        )
        db.session.add(article)
        db.session.commit()
        flash('Article created successfully!')
        return redirect(url_for('article', id=article.id))
    return render_template('new_article.html', form=form)

@app.route('/article/<int:id>')
def article(id):
    article = Article.query.get_or_404(id)
    comments = Comment.query.filter_by(article_id=id).order_by(Comment.created_at.desc()).all()
    form = CommentForm()
    return render_template('article.html', article=article, comments=comments, form=form)

@app.route('/article/<int:id>/comment', methods=['POST'])
@login_required
def add_comment(id):
    article = Article.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(
            content=form.content.data,
            article_id=article.id,
            user_id=current_user.id
        )
        db.session.add(comment)
        db.session.commit()
        flash('Comment added successfully!')
    return redirect(url_for('article', id=id))

@app.route('/search')
def search():
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    articles = Article.query.filter(
        (Article.title.ilike(f'%{query}%')) |
        (Article.content.ilike(f'%{query}%'))
    ).order_by(Article.created_at.desc()).paginate(page=page, per_page=10)
    return render_template('search.html', articles=articles, query=query)

@app.route('/category/<category>')
def category(category):
    page = request.args.get('page', 1, type=int)
    articles = Article.query.filter_by(category=category)\
        .order_by(Article.created_at.desc())\
        .paginate(page=page, per_page=10)
    return render_template('category.html', articles=articles, category=category)

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)