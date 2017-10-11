"""Sample Flask server for IoT

This is the entry point of the backend

"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/table/<int:table_id>')
def show_menu(table_id=None):
    return render_template('sample.html', table_id=table_id)
