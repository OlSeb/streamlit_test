import streamlit as st
import requests
import urllib.parse
# import datetime
import pandas as pd
import numpy as np
'''
# VerbaMachina
'''

# Set the page configuration
st.set_page_config(
    page_title="My App",
    page_icon=":guardsman:",
    layout="wide",
    initial_sidebar_state="expanded",
    page_bg_img="harry_potter_image.jpg"
)

st.write(f"Number of passenger(s):5")

# parameters = {
#     'pickup_datetime': date_time,
#     'passenger_count': passengers,
#     'pickup_latitude': picklat,
#     'pickup_longitude': picklon,
#     'dropoff_latitude': droplat,
#     'dropoff_longitude': droplon,
# }


# response = requests.get(api, params=parameters).json()
# fare = response["fare"]
# f'''
# ## Fare Estimation: ${round(fare, 2)}
# '''

# df = pd.DataFrame(
#     np.array([(float(picklat), float(picklon)), (float(droplat), float(droplon))]),
#     columns=['lat', 'lon'])

# st.map(df, zoom=5)
