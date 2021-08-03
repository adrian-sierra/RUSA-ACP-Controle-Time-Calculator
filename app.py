import flask
import os
from flask import Flask, redirect, url_for, request, render_template
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
#import config
import logging
from pymongo import MongoClient
from flask_restful import Resource, Api

###
# Globals
###

app = flask.Flask(__name__)
#CONFIG = config.configuration()
app.secret_key = " a "
api = Api(app) 

#client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
client = MongoClient(host="db", port=27017)
db = client.tododb

open_arr = []
close_arr = []
all_csv = []

@app.route('/')
def todo():
    return render_template('todo.html')

@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
#    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404

@app.route("/_calc_times")
def _calc_times():
    app.logger.debug("Got a JSON request")

    km = request.args.get('km', 999, type=float)
    b_date = request.args.get('b_date')
    b_time = request.args.get('b_time')
    brev = request.args.get('brev', type=int)

    date_string = b_date + ' ' + b_time + ':00'

    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))

    open_time = acp_times.open_time(km, brev, date_string)
    close_time = acp_times.close_time(km, brev, date_string)

    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)


@app.route('/new', methods=['POST'])
def new():
    db.tododb.remove({})
    l = bool((request.form.getlist('open')[0]) )
    i = 0
    while ((request.form.getlist('open')[i])):
        open_arr.append(request.form.getlist('open')[i])
        close_arr.append(request.form.getlist('close')[i])
        all_csv.append(request.form.getlist('open')[i])
        all_csv.append(request.form.getlist('close')[i])
        i += 1
    item_doc = {
        'open': open_arr,
        'close': close_arr
    }
    if (not l):
        flask.flash("ERROR: Trying to add empty data")  
    else:
        db.tododb.insert_one(item_doc)
    
    return redirect(url_for('todo'))

@app.route('/display', methods=['POST'])
def display():
    _items = db.tododb.find()
    if (db.tododb.count() == 0):
        flask.flash("ERROR: Trying to display empty data")
        return render_template('todo.html')
    else:
        items = [item for item in _items]
        return render_template('todo.html', items=items)

#app.debug = CONFIG.DEBUG
#if app.debug:
#    app.logger.setLevel(logging.DEBUG)

class All(Resource):
    def get(self):
        return { 'open' : open_arr, 'close' : close_arr }
class OpenOnly(Resource):
    def get(self):
        if (request.args.get('top')):
            k = int(request.args.get('top'))
            return { 'open' : open_arr[:k] }
        else:
            return { 'open' : open_arr }       
class CloseOnly(Resource):
    def get(self):
        if (request.args.get('top')):
            k = int(request.args.get('top'))
            return { 'close' : close_arr[:k] }
        else:
            return { 'close' : close_arr }
class AllCSV(Resource):
    def get(self):
        return  str(all_csv)[1:-1] 
class OpenCSV(Resource):
    def get(self):
        new_arr = []
        if (request.args.get('top')):
            k = int(request.args.get('top'))
            new_arr = open_arr[:k]
            return str(new_arr)[1:-1]
        else:
            return str(open_arr)[1:-1]
class CloseCSV(Resource):
    def get(self):
        new_arr = []
        if (request.args.get('top')):
            k = int(request.args.get('top'))
            new_arr = close_arr[:k]
            return str(new_arr)[1:-1]
        else:
            return str(close_arr)[1:-1]

api.add_resource(All, '/listAll', '/listAll/json')
api.add_resource(OpenOnly, '/listOpenOnly', '/listOpenOnly/json')
api.add_resource(CloseOnly, '/listCloseOnly', '/listCloseOnly/json')
api.add_resource(AllCSV, '/listAll/csv')
api.add_resource(OpenCSV, '/listOpenOnly/csv')
api.add_resource(CloseCSV, '/listCloseOnly/csv')

if __name__ == "__main__":
 #   print("Opening for global access on port {}".format(CONFIG.PORT))
 #   app.run(port=CONFIG.PORT, host="0.0.0.0", debug=True)
    app.run(host="0.0.0.0", port=80, debug=True)

