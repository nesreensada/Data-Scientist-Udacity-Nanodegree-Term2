# import libraries
import sys
import sqlite3
import pandas as pd
from sqlalchemy import create_engine
from string import punctuation
import numpy as np

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

from sklearn.ensemble import AdaBoostClassifier

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib

import nltk
nltk.download('punkt')
nltk.download('wordnet')

def load_data(database_filepath):
    """
    This function loads data from given database path 
    and returns a dataframe
    Input:
        database_filepath: database file path
    Output:
        X: traing message list
        Y: training target
        category names  
    """
    # load data from database
    engine = create_engine('sqlite:///'+ database_filepath)
    df = pd.read_sql_table('messages',engine)
    
    # define features and target
    X = df.message
    y = df.iloc[:,4:]
    category_names = list(df.columns[4:])
    
    return X, y, category_names

def tokenize(text):
    """
    Tokenization function to process the text data to normalize, lemmatize, and tokenize text. 
    Input: Text data
    Output: List of clean tokens 
    """
     # remove punctations
    text =  ''.join([c for c in text if c not in punctuation])
    
    #tokenize text
    tokens = word_tokenize(text)
    
    # initiate lemmatizer
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for token in tokens:
        # lemmatize, normalize case, and remove leading/trailing white space
        clean_tok = lemmatizer.lemmatize(token).lower().strip()
        clean_tokens.append(clean_tok)
    return clean_tokens

def build_model():
    """
    Build Machine learning pipleine using adaboost classifier
    Input:
       None
    Output: 
        clf: gridSearch Model
    """
    ada_pipeline =  Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier((AdaBoostClassifier())))
    ])
    # grid search parameters
    parameters = {
    'tfidf__norm':['l2','l1'],
    'vect__stop_words': ['english',None],
    'clf__estimator__learning_rate' :[0.1, 0.5, 1, 2],
    'clf__estimator__n_estimators' : [50, 60, 70],
    }
    #create grid search object
    clf_grid_model = GridSearchCV(ada_pipeline, parameters)
    return clf_grid_model

def evaluate_model(model, X_test, Y_test, category_names):
    """
    Prints the classification report for the given model and test data
    Input:
        model: trained model
        X_test: test data for the predication 
        Y_test: true test labels for the X_test data
    Output:
        None 
    """
    # predict 
    y_pred = model.predict(X_test)
    # print the metrics
    for i, col in enumerate(category_names):
        print('{} category metrics: '.format(col))
        print(classification_report(Y_test.iloc[:,i], y_pred[:,i]))
    


def save_model(model, model_filepath):
    """
    This method is used to export a model as a pickle file
    Input:
        model: trained model 
        model_filepath: location to store the model
    Output: None
    """
    joblib.dump(model, model_filepath)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()