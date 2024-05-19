# # 1. importing the neccessary packages to process the program
# import pandas as pd
# from sklearn.neural_network import MLPClassifier
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import classification_report, confusion_matrix
# import numpy as np
# import warnings
# warnings.filterwarnings("ignore")
#
# # 2. reading the data from the file using read method and delimiter ,  and storing that into data variable
# data = pd.read_csv('data_file.csv', delimiter=',')
#
# # printing some of the data to show for the user
# print(data.head())
#
# # 3. Perform encoding for categorical features for purchase,gender,education,occupation
# lEncoder = LabelEncoder()
# data['purchased'] = lEncoder.fit_transform(data['purchased'])
# data['gender'] = lEncoder.fit_transform(data['gender'])
# data['education'] = lEncoder.fit_transform(data['education'])
# data['occupation'] = lEncoder.fit_transform(data['occupation'])
#
# # after performing categorical features on purchase,gender,education,occupation , need to print and check data has changed or not
# print(data.head())
#
# # 4. Define input features and target variable , to generate the training and training subsets
# X = data.drop(columns=['purchased'])
#
# y = data['purchased']
#
# # 5. creating the variables spliting data into the  training and testing subnets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
#
# # 6. Creating a MLP classifier model so that we can train the model
# mlp = MLPClassifier(hidden_layer_sizes=(10, 20))
#
# # 7. Training the model on training data
# mlp.fit(X_train, y_train)
#
# # 8. Making predictions on the test set and printing on the console
# predictions = mlp.predict(X_test)
#
# # 9. Evaluating the model
# print(confusion_matrix(y_test, predictions))
# print(classification_report(y_test, predictions))
#
#
# # Alternatively, you can create a new numpy array for a new customer
# # and use the model to predict whether they will make a purchase or not
# # importing numpy and creating a new customer to check the prediction using array method of numpy
# # Using the predict method predicting the data if he will buy the product or not
# # processing the result and showing the on the console using
#
# new_customer = np.array([[35, 41212, 2, 2, 1, 2]])
# prediction = mlp.predict(new_customer)
# if prediction == 0:
#     print('This customer is unlikely to purchase the product.')
# else:
#     print('This customer is likely to purchase the product.')

