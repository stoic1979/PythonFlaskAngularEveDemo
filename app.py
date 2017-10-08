import os
import jsonify
import json
import traceback
from flask import Flask, render_template, request
from db import Mdb
from bson import ObjectId
from eve import Eve


# simple flask
#app = Flask(__name__)
#mdb = Mdb()


# use when we use EVE Rest api framework
templ_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Eve('App', template_folder=templ_dir)
mdb = Mdb()


######################################################
#                                                    #
# Note: _id of mongodb collection was not getting    #
# json encoded, so had to create this json encoder   #
#                                                    #
######################################################
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

@app.route('/')
def main_page():
    return 'Welcome to Flask Angular Demo'


@app.route('/lst')
def lst():
    templ_data = {'title': 'list_data'}
    return render_template('list.html', **templ_data)


@app.route("/add_machine", methods=['POST'])
def add_machine():
    try:
        json_data = request.json['info']

        print "json data:", json_data
        deviceName = json_data['device']
        ipAddress = json_data['ip']
        userName = json_data['username']
        password = json_data['password']
        portNumber = json_data['port']

        mdb.save_machine(deviceName, ipAddress, userName, password, portNumber)
        return jsonify(status='OK', message='inserted successfully')

    except Exception as exp:
        return jsonify(status='ERROR', message=str(exp))


@app.route("/get_machine", methods=['POST'])
def get_machine():

    try:
        result = mdb.get_machine_data()
        return json.dumps(result)
    except Exception as exp:
        print 'get_machine() :: Got exception %s' % exp
        print(traceback.format_exc())


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)
