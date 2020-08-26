from flask import Blueprint, render_template
from setting import session

home = Blueprint('home', __name__,
                 template_folder='templates',
                 static_folder='static')


from models.one2one_model import Address
from models.one2many_model import User


@home.route('/')
def index():
    users = session.query(User).all()
    addresses = session.query(Address).all()
    dts = session.query(User, Address).outerjoin(Address, User.id==Address.user_id).all()
    return render_template('home/index.html', users=users, addresses=addresses, dts=dts)

