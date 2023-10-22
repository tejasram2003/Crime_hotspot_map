from django.shortcuts import render
from django.http import JsonResponse
from random import random
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import random
from . import predction
from geopy.geocoders import Nominatim
import datetime
from .predict import *
import random
from . import models
from tqdm import tqdm
import math

# Create your views here.
def index(request):
    return  render(request, 'index.html')

# with open('mapsite/maps/Randomforest.pth','rb') as file:
#     model = pickle.load(file)
#     print("Loaded model")


@csrf_exempt
def update_marker_coordinates(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # print((latitude, longitude))s
        # geolocator = Nominatim(user_agent="geoapiExercises")

        # location = geolocator.reverse((latitude, longitude), exactly_one=True,timeout=30)

        # block = get_block_name(location.raw['address']['road'])

        date = datetime.datetime.today()
        print(date)



        # Do something with the latitude and longitude

        # input_df = get_parameters(latitude, longitude,date)

        # progress = predict(input_df,model)
        coord = (float(latitude), float(longitude))
        progress = predction.predict(coord)
        print(progress)
        return JsonResponse({'status': 'success', 'progress': progress})
    else:
        return JsonResponse({'status': 'error'})
    
def history_dashboard(request,latitude,longitude):
    
    # latitude = request.GET.get('latitude')
    # longitude = request.GET.get('longitude')

    # dataset = pd.read_csv('./Dataset\Chicago_Crimes_2012_to_2017.csv',on_bad_lines='skip')
    # row = dataset.loc[1238,:]

    print(f"latitude: {latitude}, longitude: {longitude}")

    latitude = float(latitude)
    longitude = float(longitude)

    curr_latlong_row = models.PastCrimeRecords.objects.filter(Latitude = latitude, Longitude = longitude).first()

    print(curr_latlong_row)

    if curr_latlong_row:
        block = curr_latlong_row.Block
        required_rows = models.PastCrimeRecords.objects.filter(Block = block)
    else:
        lat_min = float(latitude) - 0.25/111.32
        lat_max = float(latitude) + 0.205/111.32
        lng_min = float(longitude) - (0.250 / (111.32 * math.cos(math.radians(latitude))))
        lng_max = float(longitude) + (0.250 / (111.32 * math.cos(math.radians(latitude))))
        query = Q(
            Latitude__gte=lat_min,
            Latitude__lte=lat_max,
            Longitude__gte=lng_min,
            Longitude__lte=lng_max
        )

        required_rows = models.PastCrimeRecords.objects.filter(query)
    print(len(required_rows))


    
    return render(request,'PastRecords.html',{'required_rows':required_rows,'crime_count':len(required_rows)} )
    
def get_row(latitude,longitude):
    table = models.Crime_records.objects.get(latitude=latitude,longitude=longitude)

def create_database(request):
    dataset = pd.read_csv('../Dataset\Chicago_Crimes_2012_to_2017.csv',on_bad_lines='skip')
    for i in tqdm(range(len(dataset))):
        try:
            Row_ID = dataset.loc[i,'ID']
            Case_Number = dataset.loc[i,'Case Number']
            Date = dataset.loc[i,'Date']
            Block = dataset.loc[i,'Block']
            IUCR = dataset.loc[i,'IUCR']
            Primary_Type = dataset.loc[i,'Primary Type']
            Description = dataset.loc[i,'Description']
            Location_Description = dataset.loc[i,'Location Description']
            Arrest = dataset.loc[i,'Arrest']
            Domestic = dataset.loc[i,'Domestic']
            Beat = dataset.loc[i,'Beat']
            District = dataset.loc[i,'District']
            Ward = dataset.loc[i,'Ward']
            Community_Area = dataset.loc[i,'Community Area']
            FBI_Code = dataset.loc[i,'FBI Code']
            Updated_On = dataset.loc[i,'Updated On']
            Latitude = dataset.loc[i,'Latitude']
            Longitude = dataset.loc[i,'Longitude']

            New_crime = models.PastCrimeRecords.objects.create(Row_ID=Row_ID, Case_Number=Case_Number,Date=Date, Block=Block, IUCR=IUCR, Primary_Type=Primary_Type, Description=Description,
                                            Location_Description=Location_Description, Arrest=Arrest, Domestic=Domestic, Beat=Beat, District=District, Ward=Ward,
                                            Community_Area=Community_Area, FBI_Code=FBI_Code, Updated_On=Updated_On, Latitude=Latitude,Longitude=Longitude)
        except Exception as e:
            print(f"Exception {e} at row {i}")


    return HttpResponse('<h1>Created database.</h1>')


