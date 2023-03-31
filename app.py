import streamlit as st
import pickle
import pandas as pd
import numpy as np
import xgboost
from xgboost import XGBRegressor

pipe = pickle.load(open('pipe.pkl','rb'))

teams = ['Australia','India','Bangladesh','New Zealand','South Africa',
         'England','West Indies','Afghanistan','Pakistan','Sri Lanka']

cities = ['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Auckland',
 'Cape Town',
 'London',
 'Pallekele',
 'Barbados',
 'Sydney',
 'Melbourne',
 'Durban',
 'St Lucia',
 'Wellington',
 'Lauderhill',
 'Hamilton',
 'Centurion',
 'Manchester',
 'Abu Dhabi',
 'Mumbai',
 'Nottingham',
 'Southampton',
 'Mount Maunganui',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Cardiff',
 'Christchurch',
 'Trinidad']

st.title('Cricket Score Predictor')

col1,col2 = st.columns(2)

with col1:
    Batting_team = st.selectbox('Select Batting Team',sorted(teams))   #CREATING A PART IN WEBSITE FOR CHOOSING BATTING TEAM AND PROVIDING WITH DROP MENU OF TEAMS IN ACSENDING ORDER AND STORING THE CHOOSEN TEAM IN A VARIABLE
with col2:
    Bowling_team = st.selectbox('Select Bowling Team',sorted(teams))   #CREATING A PART IN WEBSITE FOR CHOOSING BOWLING TEAM AND PROVIDING WITH DROP MENU OF TEAMS IN ACSENDING ORDER AND STORING THE CHOOSEN TEAM IN A VARIABLE

city = st.selectbox('Select City',sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    Cure_sr = st.number_input('Current Score')
with col4:
    Overs = st.number_input('Overs Done(overs > 5)')
with col5:
    wickets = st.number_input('Wickets Out')

last_five = st.number_input('Runs In Last Five Overs')

if st.button('Predict Score'):
    Balls_left = 120 - (Overs*6)
    wickets_left = 10 - wickets
    crr = Cure_sr /Overs

    input_df = pd.DataFrame(
        {'batting_team': [Batting_team],'bowling_team': [Bowling_team],'city': [city],
         'current_score': [Cure_sr],'balls_left': [Balls_left],'wickets_left':[wickets],'crr': [crr],'last_five': [last_five]}
    )

    result = pipe.predict(input_df)
    st.header ("Predicted Score : " + str(int(result[0])))

