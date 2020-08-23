#
from flask import render_template, Blueprint, Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import engine, create_engine, text
from sqlalchemy.orm import Session, sessionmaker
from config import Config
from models import Todo, TodoCategory
from sqlalchemy.ext.declarative import declarative_base

todo = Blueprint('todo', __name__,
                 template_folder='templates',
                 static_folder='static')

todoModel = Flask(__name__)
todoModel.config.from_object(Config)
engine = create_engine('postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
        'user': 'admin',
        'password': 'password',
        'host': '127.0.0.1',
        'name': 'postgres_db'
    }))

# engine = create_engine('postgresql://username:password@hostname/mydatabase')
# engine = create_engine('oracle://username:password@127.0.0.1:1521/sidname')
# engine = create_engine('oracle://username:password@tnsname')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

db = SQLAlchemy(todoModel)
db.init_app(todoModel)


@todo.route('/todo', methods=['GET'])
def index():
    todos = session.query(Todo).all()
    lists = session.query(TodoCategory).all()
    if not todos or not lists:
        raise
    objects = todos
    return render_template('todo/index.html', lists=lists, todos=todos)

