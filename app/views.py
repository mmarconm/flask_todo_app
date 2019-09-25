from flask import (
    Blueprint,
    render_template,
    url_for,
    request,
    url_for,
    redirect,
    current_app
)

from app.models import Todo

task = Blueprint('task', __name__)


@task.route('/about', methods=['GET'])
def about():
    return render_template('index.html')


@task.route('/', methods=['GET', 'POST'])
def todo_app():
    if request.method == 'POST':
        if request.form['task']:
            new_todo = Todo(task=request.form['task'])
            current_app.db.session.add(new_todo)
            current_app.db.session.commit()
            return redirect(url_for('task.todo_app'))
    else:
        todos = Todo.query.all()
        return render_template(
            'index.html',
            todos=todos
        )


@task.route('/remove_task/<int:_id>', methods=['GET'])
def remove_task(_id=None):
    todo = Todo.query.filter_by(id=_id).first()
    current_app.db.session.delete(todo)
    current_app.db.session.commit()
    return redirect(url_for('task.todo_app'))
