from rest_framework import serializers

from .models import covid_india,covid_vaccine_statewise_mode,statewise_testing



class covid_india_Serializer(serializers.ModelSerializer):
    class Meta:
        model = covid_india
        fields = ('Date', 'Time','State','ConfirmedIndianNational','ConfirmedForeignNational','Cured','Deaths','Confirmed')


class covid_vaccine_statewise_mode_Serializer(serializers.ModelSerializer):
    class Meta:
        model = covid_vaccine_statewise_mode
        fields = ('Date', 'State','total_doses_adminstered','Total_Sessions_Conducted','Total_Sites','First_Dose_Administered','Second_Dose_Administered','Male_Vaccinated','Female_Vaccinated','Transgender_Vaccinated','Total_Covaxin_Administered','Total_CoviShield_Administered','Total_Sputnik_Administered','AEFI','age_18_45','age_60_plus','age_45_60','Total_Individuals_Vaccinated')


class statewise_testing_Serializer(serializers.ModelSerializer):

    class Meta:
        model = statewise_testing
        fields = ('Date', 'State', 'TotalSamples', 'Positive', 'Negative')
