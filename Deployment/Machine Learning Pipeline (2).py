#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error, r2_score

import pandas as pd
import numpy as np


# In[3]:


path = 'DataMarch.csv'
df = pd.read_csv(path)


# In[4]:


df


# In[15]:


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop(['EMI', 'ELA', 'ROI'], axis=1), df[['EMI', 'ELA', 'ROI']], test_size=0.2, random_state=42)


# In[16]:


# Define the preprocessing steps for the numerical and categorical features
numerical_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())])

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])


# In[17]:


# Combine the preprocessing steps using ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, ['Amount', 'Interest', 'LoanDuration', 'IncomeTotal', 'LiabilitiesTotal', 'DebtToIncome', 'FreeCash']),
        ('cat', categorical_transformer, ['Gender', 'Status', 'Education', 'EmploymentStatus', 'MaritalStatus', 'HomeOwnershipType', 'UseOfLoan'])
    ])


# # Linear Regressor

# In[19]:


import pickle
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

# Define the regression model
model = LinearRegression()

# Define the pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('model', model)])

# Fit the pipeline on the training data
pipeline.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = pipeline.predict(X_test)

# Evaluate the performance of the model using mean squared error and R-squared
print('Mean squared error:', mean_squared_error(y_test, y_pred))
print('R-squared:', r2_score(y_test, y_pred))



# In[20]:


with open('regression_pipeline23','wb') as f:
    pickle.dump(pipeline,f)    


# # Gradient Boosting Classifier

# In[25]:


from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def fit_and_evaluate(X_train, y_train, X_test, y_test, target):
    y_train_target = y_train[target]
    y_test_target = y_test[target]

    Classification_Pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', GradientBoostingRegressor(random_state=0))
    ])

    Classification_Pipeline.fit(X_train, y_train_target)
    y_pred = Classification_Pipeline.predict(X_test)

    mse = mean_squared_error(y_test_target, y_pred)
    r2 = r2_score(y_test_target, y_pred)

    print(f"{target}:\nMean squared error: {mse}\nR-squared: {r2}\n")


# Run the function for each target variable
fit_and_evaluate(X_train, y_train, X_test, y_test, 'ELA')
fit_and_evaluate(X_train, y_train, X_test, y_test, 'ROI')
fit_and_evaluate(X_train, y_train, X_test, y_test, 'EMI')


# # Save the model

# In[26]:




# Define the three GradientBoostingRegressor models for each target variable
models = {
    'ELA': GradientBoostingRegressor(random_state=0),
    'ROI': GradientBoostingRegressor(random_state=0),
    'EMI': GradientBoostingRegressor(random_state=0)
}

# Create a dictionary to store the model pipelines
model_pipelines = {}

# Loop through the models and create a pipeline for each one
for target_var, model in models.items():
    # select only the target variable
    y_train_ela = y_train[target_var]
    y_test_ela = y_test[target_var]

    # create a pipeline
    model_pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', model)
    ])

    # fit the model
    model_pipeline.fit(X_train, y_train_ela)

    # add the pipeline to the dictionary
    model_pipelines[target_var] = model_pipeline

# Save the model pipelines into a single pickle file

    
with open('classification23','wb') as f:
    pickle.dump(model_pipelines,f)     
    


# In[ ]:




