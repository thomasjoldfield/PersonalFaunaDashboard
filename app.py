#Yep, we're copying most of this. But at least I'm pretty sure I'm stealing the right things.
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
import numpy as np


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///data/belly_button_biodiversity.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)
# Save references to the table
Otu = Base.classes.otu
Samples = Base.classes.samples
Samples_meta = Base.classes.samples_metadata

session = Session(engine)

#index
@app.route("/")
def home():
    return render_template("index.html")

#next we start creating apis

@app.route('/names')
def names():
    results = session.query(Samples_meta.SAMPLEID).all()
    print(results)
    all_names = list(np.ravel(results))
    return jsonify(all_names)



