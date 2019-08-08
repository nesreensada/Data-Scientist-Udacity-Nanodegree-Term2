import json
import plotly
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar, Layout, Figure
from sklearn.externals import joblib
from sqlalchemy import create_engine

import numpy as np

app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///../data/DisasterResponse.db')
df = pd.read_sql_table('messages', engine)

# load model
model = joblib.load("../models/classifier.pkl")

# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    graphs = []
    # extract data needed for visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)
    
    graph_one = []
    graph_one.append(
        Bar(
                x=genre_names,
                y=genre_counts
            )
        )
    layout_one = Layout(title = 'Distribution of Message Genres',
               yaxis = {'title': "Count"},
                xaxis = {'title': "Genre"}
                )

    graphs.append(dict(data=graph_one, layout=layout_one))

     #Show Distribution of different categories
    category_name = list(df.columns[4:])
    category_counts = [np.sum(df[col]) for col in category_name]

    graph_two = []
    graph_two.append(
            Bar(
                x=category_name,
                y=category_counts
            )
        )
    layout_two =  Layout(title = 'Distribution of Message Categories',
                yaxis = {'title': "Count"},
                xaxis = {'title': "Genre"})

    graphs.append(dict(data=graph_two, layout=layout_two))

    # extract data exclude related
    categories = df.iloc[:,4:]
    categories_mean = categories.mean().sort_values(ascending=False)[1:11]
    categories_names = list(categories_mean.index)

    graph_three = []
    graph_three.append(
            Bar(
                x=category_name,
                y=category_counts
            )
        )
    layout_three =  Layout(title = 'Top 10 Message Categories',
                yaxis = {
                    'title': "Percentage", 
                    'titlefont': {'color': 'black', 'size': 12}
                },
                xaxis = {
                'title': "Category", 
                'titlefont': {'color': 'black', 'size': 12},
                'tickangle':45,
                'automargin': True
                  }
                )
    
    graphs.append(dict(data=graph_three, layout=layout_three))

    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()