from flask import Flask, Response, redirect, url_for, request, session, abort
from flask_login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user
from flask import session

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        return f'''
            Hello {session["username"]}. Welcome to our amazing API! <br><br>
            If you're ready to logout then head over to <a href="http://127.0.0.1:5000/logout">logout</a>
            <br> Hope to see you again soon 👋 %s<br>
        ''' % session['username']
    return 'To get started please <a href="http://127.0.0.1:5000/login">login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username required>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
