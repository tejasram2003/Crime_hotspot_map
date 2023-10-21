from django.db import models

# Create your models here.
class PastCrimeRecords(models.Model):
    Row_ID = models.IntegerField(unique=True, db_index=True)
    Case_Number = models.CharField(unique=True,max_length=10)
    Date = models.CharField(max_length=100)
    Block = models.CharField(max_length=100)
    IUCR = models.CharField(max_length=10)
    Primary_Type = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    Location_Description = models.CharField(max_length=500)
    Arrest = models.BooleanField()
    Domestic = models.BooleanField()
    Beat = models.FloatField(max_length=10)
    District = models.FloatField(max_length=10)
    Ward = models.FloatField(max_length=10)
    Community_Area = models.FloatField(max_length=10)
    FBI_Code = models.CharField(max_length=10)
    Updated_On = models.CharField(max_length=100)
    # Location = models.CharField(max_length=1000, null=False)
    Latitude = models.CharField(max_length=100,null=False)
    Longitude = models.CharField(max_length=100,null=False)

    

