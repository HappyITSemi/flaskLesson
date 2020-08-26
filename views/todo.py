#
from flask import render_template, Blueprint
from sqlalchemy import text

from models.todo_model import Todo, Category
from setting import session

todo = Blueprint('todo', __name__,
                 template_folder='templates',
                 static_folder='static')


@todo.route('/todo', methods=['GET'])
def todo_index():
    sql = 'select t.*, c.name from todo as t left outer join category as c ' \
          'on t.category_id = c.id;'
    todos = session.query(Todo).all()
    categories = session.query(Category).all()
    dts = session.query(Todo, Category).outerjoin(Category, Category.id==Todo.category_id).order_by(text('todo.id')).all()
    return render_template('todo/index.html', todos=todos, categories=categories, dts=dts)


def todo_new():
    pass
