# Code for 'main_app.py' file.

# Importing the necessary Python modules.
import streamlit as st
import numpy as np
import pandas as pd

# Import the individual Python files
import data
import plots
import predict
import home

# Configure your home page by setting its title and icon that will be displayed in a browser tab.
st.set_page_config(page_title = 'Car Price Prediction',
                    page_icon = ':car:',
                    layout = 'centered',
                    initial_sidebar_state = 'auto'
                    )

# Loading the dataset.
@st.cache()
def load_data():
    # Reading the dataset
    df = pd.read_csv("car-prices.csv")
    # selecting only 4 features obtained after applying RFE. The column 'price' is the target variable.
    df = df[['enginesize', 'horsepower', 'carwidth', 'drivewheel', 'price']]
    # Converting the non-numeric 'drivewheel' feature to numeric using the 'map()' function.
    df['drivewheel'] = df['drivewheel'].map({'rwd': 0, 'fwd': 1, '4wd': 2})     
    return df
  
car_df = load_data()

# Adding a navigation in the sidebar using radio buttons
# Create a dictionary.
pages_dict = {
                "Home": home,
                "View Data": data, 
                "Visualise Data": plots, 
                "Predict": predict
            }

# Add radio buttons in the sidebar for navigation and call the respective pages based on user selection.
st.sidebar.title('Navigation')
user_choice = st.sidebar.radio("Go to", tuple(pages_dict.keys()))
if user_choice == "Home":
    home.app() 
else:
    selected_page = pages_dict[user_choice]
    selected_page.app(car_df) 
# This 'app()' function is defined in all the 'home.py', data.py', 'plots.py' and 'predict.py' files. 
# Whichever option out of "View Data", "Visualise Data" and "Predict" a user selects, that option gets stored in the 
# 'selection' variable and the correspoding value to that key gets stored in the 'page' variable and then the 'app()'
# function gets called from that Python file 
# which could be either of 'home.py', 'data.py', 'plots.py' and 'predict.py' files in this case.