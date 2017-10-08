import os
from flask import Flask, render_template
from eve import Eve


# simple flask
app = Flask(__name__)


# use when we use EVE Rest api framework
# templ_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
# app = Eve('App', template_folder=templ_dir)


@app.route('/')
def home():
    return 'Welcome to Flask Angular Demo'


@app.route('/lst')
def lst():
    templ_data = {'title': 'list_data'}
    return render_template('list.html', **templ_data)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)
