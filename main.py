"""Sample Flask server for IoT

This is the entry point of the backend

"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


"""App default route
"""
@app.route('/')
def landing_page():
    return render_template('index.html')

"""Per table routing
So Josh, this will take in an argument called table_id
and route to a page (sample.html in this case)

sample.html is supposed to be a jinja template (like razor)
and process something based on table number
"""
@app.route('/table/<int:table_id>')
def show_menu(table_id=None):
    return render_template('sample.html', table_id=table_id)

if __name__ == 'main':
    app.run()