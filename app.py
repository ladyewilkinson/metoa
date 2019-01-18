from flask import Flask, jsonify, render_template
from settings import *
from ArtObjectModel import *
import random

import requests
import json
import datetime


@app.route('/objects')
def get_all():
    objs = ArtObject.get_all()
    return render_template('objects.html', objs=objs)

@app.route('/objects/<int:id>')
def get_object(id):
    o = ArtObject.get(id)
    md = eval(o['metadata_date'])
    ro = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/' + str(id))
    oj = ro.json()
    return render_template('object.html', o=o, md = md, oj=oj)

@app.route('/')
@app.route('/random')
def get_random():
    obj_ids = ArtObject.get_all_ids()
    id = random.choice(obj_ids)
    o = ArtObject.get(id)
    ro = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/'+str(id))
    oj = ro.json()
    md = eval(o['metadata_date'])
    return render_template('object.html', o=o, md=md, oj=oj)

@app.route('/simple/<int:id>')
def get_simple(id):
    o = ArtObject.get(id)
    return render_template('simple.html', o=o)


if __name__ == "__main__":
    app.run(port=5000)
