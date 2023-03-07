import streamlit as st
# import requests
# import urllib.parse
# import datetime
import pandas as pd
import numpy as np

# # Set the page configuration
import base64


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('./harry_potter_image.jpg')


# Add some CSS to the Streamlit app to align the text to the right
st.markdown(
    """
    <style>
    body {
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Write some text to the app
'''
# Chat with Harry Potter
'''

st.write("Hey there, I'm Harry!")







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
