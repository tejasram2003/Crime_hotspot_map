import pickle
import pandas as pd
from geopy.geocoders import Nominatim


def get_parameters(latitude, longitude,date):
    data = pd.read_csv('./Dataset\Chicago_Crimes_2012_to_2017.csv',on_bad_lines='skip')
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse((latitude, longitude), exactly_one=True,timeout=30)
    block = get_block_name(location.raw['address']['road'])

    for index,row in data.iterrows():
        if row['Block'] == block:
            location_description = row['Location Description']
            beat = row['Beat']
            district = row['District']
            ward = row['Ward']
            community_area = row['Community Area']
            print('ward and stuff figured out')
            break
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    day_of_week = date.weekday

    morning_start = pd.to_datetime('06:00:00').time()
    evening_end = pd.to_datetime('18:00:00').time()

    time = date.dt.time

    if morning_start < time < evening_end:
        morning = 1
        evening = 0
    else:
        morning = 0
        evening = 1
    
    input_df = pd.DataFrame({'Block':block,'Location Description':location_description, 'Beat':beat,'District':district,'Ward':ward,'Community Area':community_area,'Year':year,'Month':month,'Day':day,'Hour':hour,'DayOfWeek':day_of_week,'Latitude':latitude,'Longitude':longitude,'Crime Period_Evening':evening,'Crime Period_Morning':morning})
    print('Preprocessing Complete')
    return input_df

def get_block_name(block):
    blocklist = block.split(' ')[:-1]
    block = ""
    news = blocklist[0][0].upper()
    blocklist.pop(0)

    block+=news+' '

    for i in blocklist:
        block+=i+" "

    return (block[:-1].upper())

def predict(input_df,model):
    
    print('Model Loaded')
    y_pred = model.predict(input_df)
    print("Prediction Complete")
    return y_pred
    