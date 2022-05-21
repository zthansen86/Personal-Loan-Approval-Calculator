# Project-4
[Project Proposal](https://docs.google.com/document/d/13jzh5GitPx-FSpSME1IUk7DL0JOcLpmYqXXHkqt1ff8/edit?usp=sharing)

## Background
#### Personal Loan Approval Prediction for Machine Learning 
In the financial industry, credit card scores are commonly used for risk assesment. Using [loan_data.csv](https://github.com/zthansen86/Project-4/blob/main/loan_data.csv) the probability of future defaults and borrowing pattens can be reasonably using supervised machine learning algorithms such as logistic regression and random forest classifier.  

### Data Source 
[Kaggle's Credit Card Approval Prediction Dataset for Machine Learning](https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction)

## CSVs
#### CVS Used
1. [loan_data.csv](https://github.com/zthansen86/Project-4/blob/main/loan_data.csv)
#### CSV Exported
3. [Main_Doc.csv](https://github.com/zthansen86/Project-4/blob/main/Main_Doc.csv)

### Data Cleaning 
* columns null values were removed
    * ["Loan_ID", "Gender", "Education", "Credit_History", "Property_Area"]
* columns were split into quantitative and categorical
* non-numeric data, 'Loan_Status' was converted to numeric of 0 or 1.
* X data set was created by drop its label
* dataset was scaled
### Data ML Model
* data was split trained and tested
* 1) logistic regression 
    * dataset was fitted 
    ### Scores
      * Training Data Score: 0.7219917012448133
      * Testing Data Score: 0.6652892561983471
* 2) DecisionTreeClassifier
    * also fitted
    * confusion_matrix
* 3) RandomForestClassifier
    * also fitted/scaled
    * classification report
    * confusion_matrix
* Correlation heat map
* Plotting of trainning and testing data

Presentation: https://docs.google.com/presentation/d/1rY4BF-SAj9msDPIQxVRDQ5mH76-0-ZXXoaN7_1-oM6U/edit?usp=sharing 
