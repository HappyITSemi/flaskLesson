import os
from flask import render_template, Blueprint

admin = Blueprint('admin', __name__,
                  template_folder='templates',
                  static_folder='static')


@admin.route('/admin')
def index():
    return render_template('admin/index.html')
