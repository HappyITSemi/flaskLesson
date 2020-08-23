import os
from flask import render_template, Blueprint

api = Blueprint('api', __name__,
                template_folder='templates',
                static_folder='static')


@api.route('/api')
def index():
    return render_template('api/index.html')

