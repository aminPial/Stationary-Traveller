from flask import render_template
from flask import redirect
from server import app


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/categories')
def go_categories():
    return render_template('prev/categories.html', categories={'Classic': [], 'Fiction': [],
                                                               'Thriller': [], 'History': [],
                                                               'Others': []})


@app.route('/profile')
def go_profile():
    return render_template('prev/profile.html')


@app.route('/registration')
def go_registration():
    return render_template('prev/register.html')


@app.route('/shops')
def go_shops():
    return render_template('prev/shop.html', shops=['BookStore', 'Websites', 'Buy PDF'])


@app.route('/about_us')
def go_about_us():
    return render_template('prev/about_us.html')


@app.route('/reviews')
def go_reviews():
    return render_template('prev/reviews.html')


@app.route('/authors')
def go_authors():
    return render_template('prev/authors.html')


@app.route('/read_in')
def go_read_in():
    return render_template('prev/read_in.html')


@app.route('/login')
def go_login():
    return render_template('prev/login.html')
