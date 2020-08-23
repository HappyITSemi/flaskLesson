from flask import render_template, Blueprint

dashboard = Blueprint('dashboard', __name__,
                      template_folder='templates',
                      static_folder='static')


@dashboard.route('/dashboard')
def index():
    return render_template('dashboard/index.html')

