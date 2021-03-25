![Automotive Image](images/pic.jpg)

## Automotive Value Analysis 

Heroku Web App: https://vehicle-price.herokuapp.com/

## Background

Transportation is a major type of expense in Canada. It costs generally around 20% of after-tax income for a middle-class household in Canada. In addition, the rapid depreciation of cars increases the burden of car owners. According to research, new vehicles usually shed 10% of their value as soon as the vehicles are driven off, and another 10% by the end of the first year. If depreciation is taken into consideration, owning a new vehicle costs between $8,600 and $13,000 a year, which is close to the $11,940 that Canadians pay on average in rent for a two-bedroom apartment. Due to this fact, purchasing used vehicles have been extremely popular and the used-car market is very mature in Canada. Therefore, we developed this used vehicle pricing prediction app to determine the most optimal price for selling and buying a used vehicle based on various features to help used-car buyers and sellers to make decisions.
	
## Objective

To analyze the depreciation value of cars over the years by analyzing the sale prices on resale posts. This analysis will also include analysis on various factors like vehicle type, manufacturer, year and so on. The objective is to create a recommendation system to provide users with a reasonable price point for their used car. 

### Data Sources

Data from a Web Scrapper on Kaggle  [https://www.kaggle.com/austinreese/craigslist-carstrucks-data, csv format] – Craiglist was scrapped every few months to collect information from sale postings of used cars.

### Project Development Process

1. Clean and transform raw data.
2. Preprocess data with One-Hot Encoding for category features and Standard Scale for numerical features. 
3. Select algorithm using PyCaret.
4. Select the Machine Learning model using Feature Engineering.
5. Build the Machine Learning model using Random Forest.
6. Develop the app using HTML and CSS as well as Flask to create API routes for the app.

### Future Work

* When computing resources available, add back "model" column to increase prediction accuracy.
* Further Feature Engineering Tasks to reduce the model complexity while maintaining accuracy.
* Perform ELT process to load big datafile onto Data Base and use cloud resources to query and perform transformation and load back clean data sets. 

## Credits
Thanks to teammates: **Kelvin Deng, Thao Hoang, May Ang, Yijing Su**
