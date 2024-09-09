import streamlit as st
import pandas as pd
import numpy as np
import joblib

# loading the model
model = r"C:\Users\Admin\AIML Jupyter folder\KNN_model.pkl"
load_model = joblib.load(model)


# heading of the program
st.header("IRIS FLOWER PREDICTION KNN MODEL")

# taking input from the user 
sepal_length = st.number_input("please enter the sepal_length")
sepal_width = st.number_input("please enter the sepal_width")
petal_length = st.number_input("please enter the petal_length")
petal_width = st.number_input("please enter the petal_width")


# if user didnt entered the value 

# creating a numpy array of input
feature_column = [sepal_length, sepal_width ,  petal_length, petal_width]
x_user = np.array([feature_column])

# making the prediction
y_pred =load_model.predict(x_user)

result_dict = {0:"Iris-setosa" , 1 :"Iris-versicolor"  , 2:"Iris-virginica"}

pred_flower = result_dict[y_pred[0]] # accessing the index 0 of the y_pred array to its value 
# creating a submit button
button = st.button("SUBMIT")

# to show the prediction once button is clicked
if (button):
    if (sepal_length ==0 or sepal_width ==0 or petal_length == 0 or petal_width == 0):
     st.info("please enter the valid length of the flowers")

    else:
       st.write(f"the information you provided shows the flower is :  {pred_flower}")