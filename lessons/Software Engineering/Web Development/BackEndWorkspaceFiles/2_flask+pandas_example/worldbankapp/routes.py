from worldbankapp import app
from flask import render_template
import pandas as pd
from wrangling_scripts.wrangling import data_wrangling

import plotly.graph_objs as go
import plotly, json

data = data_wrangling()

print(data)
country = data[0][0]
x_val = data[0][1]
y_val = data[0][2]
"""
graph_one = [go.Scatter(
    x = data[0][1],
    y = data[0][2],
    mode = 'lines',
    name = country
)]
"""
graph_one = []
for data_tuple in data:
    graph_one.append(go.Scatter(
    x = data_tuple[1],
    y = data_tuple[2],
    mode = 'lines',
    name = data_tuple[0]
    ))
    
layout_one = dict(title ='Change in hectares arable land <br> per Person 1990 to 2015',
                 xaxis = dict(title='Year', autotick=False, tick0=1990, dtick=25),
                 yaxis=dict(title ='Hectares'))
figures = []
figures.append(dict(data=graph_one, layout=layout_one))

#plot ids for the html tag
ids = ['figure-{}'.format(i) for i,_ in enumerate(figures)]

# convert plotly figures to JSON for javascript in html template

figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', ids=ids, figuresJSON=figuresJSON)
    
    