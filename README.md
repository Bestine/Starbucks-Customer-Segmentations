
# Starbucks Customer Data

## Problem statement, project aims and objectives

My project is based on a data provided by Starbucks on a promotional campaign that was held for a month. In my research I’m going to analyse and simulate the customer demographics and transactional activities during this period. The campaign served a variety of offers to customers, it’s merely an advertisement for beverages & food which the customer receives on their mobile app, it could be an advertisement or BOGO (Buy one get one free). Some customers don’t receive the same offers, or don’t receive offers at all, and that is the challenge to solve with this data set. 


The purpose of my project is to understand and evaluate which customers response to which offer in order to come up with a better approach for the business to attract more customers. And a suitable approach for existing customers.
With the data that I have customers are categorized into segments based on their transactional activities, this helps me separate customers knowing the specific suggestion that can be given to each individual to boost the stores revenue, brand awareness and customers satisfaction. Customer segmentation also helps with targeting new customers, which brings me to one of the challenges of this project to solve with the data set. 


## Aim
My Aim for this project is to enhance my own skill in analysing data as well as Help the business understand their customers better, improve sales, improve customer targeting, reduces costs, and allows for the creation of better problem-solving strategies for the Stakeholders to take advantage of. As part of my project, I chose to implement an interactive web application that showcases the data and displays the results with some visual effects and making sense of the patterns to help the user pay attention to areas that indicate errors or that require more attention and keep track of the progress. 

## Objective
The data set contains 17,000 customers, including their age, gender, income, and date of becoming a member. Customers received offers every few days throughout the campaign month via a variety of promotional channels, (Email, Text, Phone call). However not every customer has gotten the same amount of offers.
In order to best understand the data and provide the correct analysis I must have a strategy on how to segment the customers and a technique to do so. 
    **1. Data Wrangling** 
Data will read into three Pandas DataFrames. Each DataFrame will be cleaned and altered during data wrangling to prepare them for analysis. 
    **2. Exploratory Data Analysis (EDA)**
To fully understand the data, I will first perform EDA on each of the three DataFrames separately. All DataFrames will undergo univariate analysis which produces a summary of the statistics for all variables related to each subject (offers, clients, and events) in the data. 
    **3. Most popular offers & What made them popular?** 
To answer this business question, I first need to find a better approach to sending customer specific deals. Firstly, I need to identify the best performance in the past and figure out the key factors that contribute to the high performance. Therefore, I analyse data of offers and data on offers related to the events combined.
    **4. Customer Segmentation**
In regards of grouping customers by behaviour, I will use customer segmentation based on shared characteristics. K-means Clustering is a method used to find customer segments that share similar behaviour patterns, I will use this technique as I have previous experience with it.

    **5. RFM Clustering** 
Following Customer segmentation (RFM) Recency, Frequency, Monetary, is another effective technique use in marketing to segment customer into similar clusters and target them according to their demographic and transactional activities. 
Information about the promotional offers that are possible to receive, and basic information about each one including the promotional type, duration of the promotion, reward, and how the promotion was distributed to customers. 

## Database

Data
About file

Information about the promotional offers that are possible to receive, and basic information about each one including the promotional type, duration of the promotion, reward, and how the promotion was distributed to customers.


Dimensional data about each person, including their age, salary, and gender, there is one unique customer for each record.

Records show the different steps of promotional offers that a customer received. The different values of receiving a promotion are receiving, viewing, and completing. You also see the different transactions that a person made in the time since he became a customer. With all records, you see the day that they interacted with Starbucks and the amount that is worth

Create an Interactive Dashboard in Python
Here is an example of the way I would like my project to be displayed 
    • https://towardsdatascience.com/the-easiest-way-to-create-an-interactive-dashboard-in-python-77440f2511d1
