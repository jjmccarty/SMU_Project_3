# Project 3 -How lifestyle factors impact Diabetes Risk

## Project Objectives
1.To develop a chatbot that assists users with Christmas shopping for book ideas for specific people on their gift list.

### Team

The following team members were all original contributors to project
- Casandra Murray
- Armando Zamora
- Jessica McCarty
- Philip Klimkewicz
- Gazala Siddiqi

## Project Files
The following files are the core code for the project
- ```'Resources/diabetes_data.csv`` - data file backing the project dataframe
- ```data_outcomes.py``` - python file that loads and cleans the data 
- ```diabetes_data.ipynb``` - notebook for running the models and building the test and train data sets
- ```data_models.py``` - python file that is used for running the models 
- ```interface.py```- python file that is used for our UI and prediction of new data.

## Data Sources
Data sources for this analysis come from existing publicly available sources on https://openlibrary.org/. Additionaly for our LLM model we are using Gemini. 


## Data Processing & Data Outcomes
In this project, our goal was to assist Christmas shoppers in finding gift ideas for people on their holiday lists. Initially, we planned to identify retail stores that could generate random gift suggestions. However, due to limitations in API access, we had to pivot our approach. This led us to explore the Open Library API, which allowed us to make personalized book recommendations based on user preferences.


## Outcomes/Conclusions
One of our key conclusions is that sufficient access to data is essential for a large language model (LLM) to perform effectively. In our case, limited access to retail APIs hindered the model's functionality. Additionally, we discovered that the search criteria significantly influence the results the model retrieves. Properly defining these criteria is crucial for achieving accurate and relevant outputs.