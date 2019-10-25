# Data Scientist Nanodegree
# Capstone Project
## Project: Starbucks Promotion Strategy 

### Installations

This project requires **Python 3.x** and the following Python libraries installed:

- tqdm==4.31.1
- seaborn==0.9.0
- scikit-learn==0.21.3
- plotly==4.1.1
- pandas==0.24.2
- numpy==1.16.2
- matplotlib==3.0.3

You will also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html)

install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.

### Project Motivation

As per Udacity Data Scientist Nanodegree project Term 2. This porject is the Capstone project for this term nanodegree. I was intriguted to analyze the customers behavior and promotion strategies. 

for more information refer to the medium blogpost for this project:https://medium.com/@nesreensada/how-to-build-a-profitable-promotion-strategy-easily-with-uplift-modeling-26b2addc3e46?sk=042df27552127609e6b28f5e647ca99c .

### Summary of the project

we will analyze simulated data that mimics customer behavior on the Starbucks rewards mobile app. The data provides information about the user demographics, offer details, and the user event log.

Starbucks sends out an offer to users of the mobile app, once every few days. An offer can be merely an advertisement for a drink or an actual offer such as a discount or BOGO (buy one get one free). Also, some users might not receive an offer during certain weeks. The offers can be divided into 3 main types:
 - BOGO(buy-one-get-one): the user needs to spend a certain amount to get a reward equal to a threshold amount.
- Discount: the user gains a reward equal to a fraction of the amount spent.
- Informational: This offer contains no reward nor a minimum amount spent.

The main questions we are interested in answering from the analysis:

- Can we identify which groups of people are most responsive to each type of offer?
- Can we increase Starbucks ‘ profit by adopting a selective promotion strategy instead?

Furthermore, we will use RFM(Recency-Frequency-Monetary) clustering which is a method for customer segmentation. This method divides the customer’s into groups based on their purchase recency, frequency, and monetary value.


In this project, we presented the uplift modeling approach as a way to study the customer's response to offers. The current promotion strategy was to send offers to all the customers, this is a wasteful approach and costly since not all customers respond equally to offers. Additionally, RFM clustering was used in the model features and to segment the customer on purchasing behavior.

**So what we have demystified at the course of the analysis?**

Customer Demographics:

- Income: Most people are in the 40k-80k income-range, 19% of the earners which is the 50k-60k income range.
- Gender: 58% male users compared to 42% Females.
- Age: the age group with the highest percentage in the members is 48–58 with 24%, the smaller group consists of the older generation (88–98).

RFM Segments and Customer Groups

- RFM Segments Distribution: 41% of the customers are in the Low-value RFM group followed by the Mid-value RFM group, and the High RFM group with 23% of customers.
- Customer Groups Distribution: 40% of the customers are in the Treatment response(TR) while the CR group had 14.9% of the customers.  This can explain why the quadrant models performed worst on CN.
- Gender in the RFM segments: The Males are present in the low-value and mid-value RFM while the females have a higher percentage in the high-value segment.

The Purchasing Behavior in RFM Clusters

- Total spent vs RFM segment: there was a clear difference between the different segments in terms of amount spent.
- Customer segments vs RFM clusters: The mid and high-value segments had higher percentages of the response compared to the low-value segment. This indicates that high and mid-value customers are responsive to targeted marketing while it did not make a difference in the Low values.

Customer Groups vs Demographic

- Income vs Customer Segment: The highest income customers are in TR or CR group. 
- Total Spent vs customer segment: The difference in the amount of money spent between the treatment and control groups is significant.

Uplift Modeling 

- We have higher NIR for the base strategy in most of the offers which can be explained by the higher number of Treatment groups and the amount spent is not limited to the offer amount.
- The proposed promotion strategy gave a better IRR than the base strategy.
- The two model uplift approach performed the worst in terms of NIR and IRR for most offers. which can be due to the indirect uplift resulting.
- The Promotion strategies  that performed better than the base strategy in terms of NIR: D2_20_10_5, D3_10_7_2 , B4_5_5_5 and D4_10_10_2(almost the same as the base NIR and much higher IRR), I3_0_3_0, I3_0_4_0
- The Discount and informational offers seem to be responsive to these promotion strategies while only the BOGO offers for shorter duration and amount to spent are less responsive or modeled using this.

### File Descriptions
```
├── analyzed_transactions_offers.csv
├── analyzed_transactions_offers_RFM.csv
├── analyzed_tx_offers_RFM_profile.csv
├── data
│   ├── portfolio.json
│   ├── profile.json
│   └── transcript.json
├── README.md
├── requirements.txt
└── Starbucks_Capstone_Notebook.ipynb
```
- Data: folder containing the data required for the analysis(this folder and associated folders needed to be created as per Data instructions).
- Starbucks_Capstone_Notebook.ipynb: Main notebook for the analysis

### Run

In a terminal or command window, navigate to the top-level project directory `Starbucks_Project/` (that contains this README) and run one of the following commands:

```bash
ipython Starbucks_Capstone_Notebook.ipynb.ipynb
```  
or
```bash
jupyter Starbucks_Capstone_Notebook.ipynb.ipynb
```

This will open the iPython Notebook software and project file in your browser.

### Data

The data used in this project was acquired from Starbucks to udacity. 

profile.json: Rewards program users (17000 users x 5 fields)
	gender: (categorical) M, F, O, or null
	age: (numeric) missing value encoded as 118
	id: (string/hash)
	became_member_on: (date) format YYYYMMDD
	income: (numeric)
	portfolio.json
	Offers sent during 30-day test period (10 offers x 6 fields)

reward: (numeric) money awarded for the amount spent
	channels: (list) web, email, mobile, social
	difficulty: (numeric) money required to be spent to receive reward
	duration: (numeric) time for offer to be open, in days
	offer_type: (string) bogo, discount, informational
	id: (string/hash)
	transcript.json
	Event log (306648 events x 4 fields)

person: (string/hash)
	event: (string) offer received, offer viewed, transaction, offer completed
	value: (dictionary) different values depending on event type
	offer id: (string/hash) not associated with any "transaction"
	amount: (numeric) money spent in "transaction"
	reward: (numeric) money gained from "offer completed"
	time: (numeric) hours after start of test

### References

- https://towardsdatascience.com/a-brief-overview-of-outlier-detection-techniques-1e0b2c19e561
- https://machinelearningmastery.com/handle-missing-data-python/
- http://colingorrie.github.io/outlier-detection.html
- https://medium.com/datadriveninvestor/simple-machine-learning-techniques-to-improve-your-marketing-strategy-demystifying-uplift-models-dc4fb3f927a2
- https://towardsdatascience.com/market-response-models-baf9f9913298
- https://sureoptimize.com/targeted-marketing-with-customer-segmentation-and-rfm-analysis-part-1
- https://www.optimove.com/resources/learning-center/rfm-segmentation
- https://chrisalbon.com/machine_learning/preprocessing_structured_data/convert_pandas_categorical_column_into_integers_for_scikit-learn/
- https://www.amazon.com/Predictive-Analytics-Power-Predict-Click-ebook/dp/B00BGC2WGQ
- https://www.predictiveanalyticsworld.com/patimes/uplift-modeling-making-predictive-models-actionable/8578/
- https://stackoverflow.com/questions/38584184/imputer-on-some-dataframe-columns-in-python
- https://stackoverflow.com/questions/52384806/imputer-on-some-columns-in-a-dataframe
- https://stackoverflow.com/questions/33660836/impute-entire-dataframe-all-columns-using-scikit-learn-sklearn-without-itera
-http://cs229.stanford.edu/proj2018/report/296.pdf
- https://www.slideshare.net/odsc/victor-lomachinelearningpresentation
- http://proceedings.mlr.press/v67/gutierrez17a/gutierrez17a.pdf
-https://www.predictiveanalyticsworld.com/patimes/uplift-modeling-making-predictive-models-actionable/8578/
- https://pdfs.semanticscholar.org/e979/ba084f34345b2ac8783df2b4a3295ae9273f.pdf
- http://rikunert.com/SMOTE_explained
- https://github.com/s-heisler/pycon2017-optimizing-pandas/blob/master/MinneAnalytics%20materials/Minneanalytics_talk_slides.pdf
- https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6
- https://stackoverflow.com/questions/52673285/performance-of-pandas-apply-vs-np-vectorize-to-create-new-column-from-existing-c
- https://www.mwsug.org/proceedings/2017/BF/MWSUG-2017-BF03.pdf
- https://towardsdatascience.com/fine-tuning-xgboost-in-python-like-a-boss-b4543ed8b1e
- https://machinelearningmastery.com/gentle-introduction-xgboost-applied-machine-learning/
- https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/
- https://vishalmnemonic.github.io/DC16/
- https://towardsdatascience.com/a-step-by-step-guide-for-creating-advanced-python-data-visualizations-with-seaborn-matplotlib-1579d6a1a7d0
-https://machinelearningmastery.com/feature-importance-and-feature-selection-with-xgboost-in-python/
-https://towardsdatascience.com/how-to-target-promotions-with-conversion-prediction-model-to-maximize-net-incremental-revenue-f51dabdb6320
https://vishalmnemonic.github.io/DC16/

### Licensing, Authors, Acknowledgements 

- The Data was provided by Udacity from Starbucks.

- This project is part of Data scientist Nanodegree from udacity 

This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/). Please refer to [Udacity Terms of Service](https://www.udacity.com/legal) for further information.
