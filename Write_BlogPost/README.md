# Data Scientist Nanodegree
# Introduction to data science
## Project: Amsterdam airbnb listings Analysis 2019 

### Installations

This project requires **Python 3.x** and the following Python libraries installed:

- scikit-learn==0.21.2
- pandas==0.24.2
- numpy==1.16.4
- matplotlib==3.1.0
- seaborn==0.9.0

You will also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html)

install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.

### Project Motivation

As per Udacity Data Scientist Nanodegree project Term 2 project to write a Data science blogpost using CRISP-DM. I was intriguted to analyze and find business related questions about airbnb listings for Amsterdam city. This interest stem from being a frequent user of airbnb and a curious traveler that is  interested in knowning the trends in prices and what can affect.

This can can be modified to analyze other data sets other than amsterdam data.

for more information refer to the medium blogpost for this project: https://medium.com/@nesreensada/this-is-why-an-amsterdam-airbnb-listing-is-expansive-593029aec0df.

### summary of the project

In this notebook I wanted to analyze the Amsterdam airbnb listings. I used descriptive statistics and Kmean clustering to answer the following questions:


1) Is it more expansive to book a listing during the high seasons?

I compared the price of a listing to the availability of listing to produce the supply demand curve which shows the inverse relation between the availability of listings and the average listings price.

2)Most expansive month to visit Amsterdam?

The peak in prices occur in the period between May and June and the cheapest period is between april and feb.

3) Most expansive and least expansive Neighbourhood in Amsterdam?
- The Most Expansive neighbourhood is Centrum-Oost followed by Centrum-West which is reasonable since it is the city center of amsterdam city while the cheapest listings are in Bijlmer-Centrum and Bijlmer-Oost which is part of Amsterdam-Southeast part. 

- The prices in the center is around double the prices in the southeast and westernmost neighbourhoods of Amsterdam. 
 

4) What are the attributes associated with the price of a listing?

    - Property type

    - Neighbourhood

    - Reviews in terms of review count and the recency of the reviews

    - Room Type


### File Descriptions

- Data: folder containing the airbnb data required for the analysis(this folder and associated folders needed to be created as per Data instructions).

- Amsterdam_Airbnb_Data_Analysis.ipnyb:a notebook containing the analysis for the data.

### Run

In a terminal or command window, navigate to the top-level project directory `Write_BlogPost/` (that contains this README) and run one of the following commands:

```bash
ipython notebook Amsterdam_Airbnb_Data_Analysis.ipynb
```  
or
```bash
jupyter Amsterdam_Airbnb_Data_Analysis.ipynb
```

This will open the iPython Notebook software and project file in your browser.

### Data

The data used in this project was acquired from airbnb repo for Amsterdam city using the following [link](http://insideairbnb.com/get-the-data.html). 

create a data directory containing the following required downloaded files from the above repo:
 - listings: summarized listings data for amsterdam city.
 - listings: detailed listings data for amsterdam city and rename this file to detailed_listings.csv
 - calendar: detailed calendar data for amsterdam city.

### Licensing, Authors, Acknowledgements 

- data was acquired from insideairbnb [repo](http://insideairbnb.com/get-the-data.html)
- This project is part of Data scientist Nanodegree from udacity 

This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/). Please refer to [Udacity Terms of Service](https://www.udacity.com/legal) for further information.

