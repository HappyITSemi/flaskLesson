from flask import Flask


# bcrypt = Bcrypt()
# login_manager = LoginManager()
# login_manager.login_view = 'users.login'
# login_manager.login_message_category = 'info'
# mail = Mail()
app = Flask(__name__)


def create_app():
    # bcrypt.init_app(app)
    # login_manager.init_app(app)
    # mail.init_app(app)

    from .views.home import home
    from .views.dashboard import dashboard
    from .views.api import api
    from .views.todo import todo
    from .views.admin import admin
    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    app.register_blueprint(todo)
    app.register_blueprint(admin)
    app.register_blueprint(api)
    return app


# app = create_app()
