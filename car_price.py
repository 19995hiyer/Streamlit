import pandas as pd
import numpy as np
import streamlit as st
import datetime
import pickle

cars_df=pd.read_excel("./cars24.xlsx")
st.write( 

    "# Cars 24 Price Prediction"   
)                                           
st.dataframe(cars_df.head())

Fuel_type = st.selectbox(
    "Select the Fuel Type",
    ("Diesel", "Petrol", "CNG","LPG","Electric")
)

Engine = st.slider("Set the Engin Power", 500, 5000, step= 100)
Trans_type = st.selectbox(
    "Select the Transition Type",
    ("Automatic", "Manual")
)
Seater = st.selectbox(
    "Select the # of Seats",
    (4,5,7,9,11)
)

encode_dict={
    "Fuel_type":{"Diesel":1, "Petrol":2,"CNG":3, "LPG":4, "Electric":5},
    "Seller_Type":{"Dealer":1, "Individual":2, "Trustmark Dealer":3},
    "Trans_type":{"Automatic":2, "Manual":1}
}

def model_pred(Fuel_type, Trans_type, Engine, Seater):
    
    ##Load Model
    with open("car_pred",'rb') as file:
        reg_model=pickle.load(file)
        input_features=[2018.0, 1, 4000, Fuel_type, \
                        Trans_type, 19.70, Engine, 86.30,\
                        Seater                       
                       ]
        return reg_model.predict([input_features])


if st.button('Predict Price'):
    Fuel_type=encode_dict['Fuel_type'][Fuel_type]
    Trans_type=encode_dict['Trans_type'][Trans_type]
    price=model_pred(Fuel_type, Trans_type, Engine, Seater)
    st.text(f"The price of the car is {price[0]:.2f} Lakhs Rupees") 