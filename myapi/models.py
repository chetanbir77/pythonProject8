#
from django.db import models


class covid_vaccine_statewise_mode(models.Model):
    # UpdatedOn=DateField(**{'format':'%d/%m/%Y'})
    Date = models.TextField(null = True)
    State = models.TextField(null = True)
    total_doses_adminstered = models.TextField(null = True)
    Total_Sessions_Conducted = models.TextField(null = True)
    Total_Sites = models.TextField(null = True)
    First_Dose_Administered = models.TextField(null = True)
    Second_Dose_Administered = models.TextField(null = True)
    Male_Vaccinated = models.TextField(null = True)
    Female_Vaccinated = models.TextField(null = True)
    Transgender_Vaccinated = models.TextField(null = True)
    Total_Covaxin_Administered = models.TextField(null = True)
    Total_CoviShield_Administered = models.TextField(null = True)
    Total_Sputnik_Administered = models.TextField(null = True)
    AEFI = models.TextField(null = True)
    age_18_45 = models.TextField(null = True)
    age_60_plus = models.TextField(null = True)
    age_45_60 = models.TextField(null = True)
    Total_Individuals_Vaccinated = models.TextField(null = True)

    class Meta:
        db_table = 'covid_statewise'

    # class MyCsvModel(covid_vaccine_statewise):
    #     class Meta:
    #         dbModel = covid_vaccine_statewise
    #         delimiter = ","
    #         has_header = True

class covid_india(models.Model):
    # UpdatedOn=DateField(**{'format':'%d/%m/%Y'})
    Date = models.TextField(null = True)
    Time = models.TextField(null = True)
    State = models.TextField(null = True)
    ConfirmedIndianNational = models.TextField(null = True)
    ConfirmedForeignNational = models.TextField(null = True)
    Cured = models.TextField(null = True)
    Deaths = models.TextField(null = True)
    Confirmed = models.TextField(null = True)

    class Meta:
        db_table = 'covid_india'

class statewise_testing(models.Model):
    # UpdatedOn=DateField(**{'format':'%d/%m/%Y'})

    Date = models.TextField(null = True)
    State = models.TextField(null = True)
    TotalSamples = models.TextField(null = True)
    Negative = models.TextField(null = True)
    Positive = models.TextField(null = True)

    class Meta:
        db_table = 'statewise_test'

#p=statewise_testing(Date=row['Date'],State=row['State'],TotalSamples=row['TotalSamples'],Negative=row['Negative'],Positive=row['Positive'])
#p=covid_india(Date=row['Date'],Time=row['Time'],State_UnionTerritory=row['State/UnionTerritory'],ConfirmedIndianNational=row['ConfirmedIndianNational'],ConfirmedForeignNational=row['ConfirmedForeignNational'],Cured=row['Cured'],Deaths=row['Deaths'],Confirmed=row['Confirmed'])
#p=covid_vaccine_statewise_mode(UpdatedOn=row['Updated On'],State=row['State'],total_doses_adminstered=row['Total Doses Administered'],Total_Sessions_Conducted=row['Total Sessions Conducted'],Total_Sites=row['Total Sites '],First_Dose_Administered=row['First Dose Administered'],Second_Dose_Administered=row['Second Dose Administered'],Male_Vaccinated=row['Male(Individuals Vaccinated)'],Female_Vaccinated=row['Female(Individuals Vaccinated)'],Transgender_Vaccinated=row['Transgender(Individuals Vaccinated)'],Total_Covaxin_Administered=row['Total Covaxin Administered'],Total_CoviShield_Administered=row['Total CoviShield Administered'],Total_Sputnik_Administered=row['Total Sputnik V Administered'],AEFI=row['AEFI'],age_18_45=row['18-45 years (Age)'],age_60_plus=row['60+ years (Age)'],age_45_60=row['45-60 years (Age)'],Total_Individuals_Vaccinated=row['Total Individuals Vaccinated'])