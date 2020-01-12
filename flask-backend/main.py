# Third-party libraries
from flask_login import current_user
from flask_cors import CORS
from app import create_app
from app.test.test_utils import populate_db

app = create_app()
CORS(app)
# with app.app_context():
#     populate_db()


@app.route("/")
def index():
    print(current_user)
    if current_user.is_authenticated:
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            "<div><p>Google Profile Picture:</p>"
            '<img src="{}" alt="Google profile pic"></img></div>'
            '<a class="button" href="/logout">Logout</a>'.format(
                current_user.username, current_user.email, current_user.profile_pic
            )
        )
    else:
        return '<a class="button" href="/login">Google Login</a>'


if __name__ == "__main__":
    app.run()
