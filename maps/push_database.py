import pandas as pd
from .views import create_database

dataset = pd.read_csv('Dataset\Chicago_Crimes_2012_to_2017.csv',on_bad_lines='skip')

# for i in tqdm(range(len(dataset))):
#     try:
#         ID = dataset.loc[i,'ID']
#         Case_Number = dataset.loc[i,'Case Number']
#         Date = dataset.loc[i,'Date']
#         Block = dataset.loc[i,'Block']
#         IUCR = dataset.loc[i,'IUCR']
#         Primary_Type = dataset.loc[i,'Primary Type']
#         Description = dataset.loc[i,'Description']
#         Location_Description = dataset.loc[i,'Location Description']
#         Arrest = dataset.loc[i,'Arrest']
#         Domestic = dataset.loc[i,'Domestic']
#         Beat = dataset.loc[i,'Beat']
#         District = dataset.loc[i,'District']
#         Ward = dataset.loc[i,'Ward']
#         Community_Area = dataset.loc[i,'Community Area']
#         FBI_Code = dataset.loc[i,'FBI Code']
#         Updated_On = dataset.loc[i,'Updated On']
#         Location = dataset.loc[i,'Location']

#         New_crime = Crime_records.objects.create(ID=ID, Case_Numbe=Case_Number,Date=Date, Block=Block, IUCR=IUCR, Primary_Type=Primary_Type, Description=Description,
#                                         Location_Description=Location_Description, Arrest=Arrest, Domestic=Domestic, Beat=Beat, District=District, Ward=Ward,
#                                         Community_Area=Community_Area, FBI_Code=FBI_Code, Updated_On=Updated_On, Location=Location)
#     except:
#         pass

if __name__ == "__main__":
    create_database(dataset)
