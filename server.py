import db
import time
import flask
from flask_login import LoginManager, login_required

app = flask.Flask (__name__, static_folder="client/build", static_url_path="")

login_manager = LoginManager()
login_manager.init_app(app)

#
#Sample auth
#

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/settings")
@login_required
def settings():
    pass


################################################################################
#	Client Routes
################################################################################

@app.route("/")
def home_route():
	return flask.send_from_directory(app.static_folder, "index.html")

################################################################################
#	Api Routes
################################################################################


@app.route("/api/item")
def item_route():
	# TODO: add db calls/ arguments that this route will take
	return { "msg"	: "this feature is not implemented yet" }

@app.route("/api/list")
def list_route():
	# TODO: add db calls/ arguments that this route will take
	return { "msg"	: "this feature is not implemented yet" }

@app.route("/api/user")
def user_route():
	# TODO: add db calls/ arguments that this route will take
	return { "msg"	: "this features isn't implemented yet" }

################################################################################
#	Test Routes
################################################################################


@app.route("/api/test")
def test_route():
	return {	"msg"	: "Hello, frontend!",
				"time"	: time.time() }

@app.route("/api/test2")
def test2_route():
	return { "msg"	: "this is test route 2" }

################################################################################
#	Meme Routes
################################################################################

@app.route("/api/shaq")
def shaq_route():
	return { "msg"	: "Shaq ist die Liebe. Shaq ist das Leben." }

if __name__ == '__main__':
	app.run(debug=True)
