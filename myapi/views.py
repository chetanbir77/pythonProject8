from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
import django_filters
from rest_framework import filters
from .serializers import statewise_testing_Serializer,covid_india_Serializer,covid_vaccine_statewise_mode_Serializer
from .models import statewise_testing,covid_india,covid_vaccine_statewise_mode
from rest_framework import viewsets, filters
from rest_framework import renderers
from rest_framework import permissions
from rest_framework_csv import renderers as csv_renderers
from django_filters.rest_framework import DjangoFilterBackend
from drf_multiple_model.views import ObjectMultipleModelAPIView
from drf_multiple_model.viewsets import FlatMultipleModelAPIViewSet
from rest_framework.decorators import api_view, permission_classes
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet
from rest_framework.permissions import IsAuthenticated
class statewise_testing_viewset(viewsets.ModelViewSet):

    queryset = statewise_testing.objects.all().order_by('Date')


    serializer_class = statewise_testing_Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Date']


class statewise_testing_viewset_multiple(ObjectMultipleModelAPIViewSet):
    #queryset = statewise_testing.objects.all().order_by('Date')

    querylist = [
        {'queryset': statewise_testing.objects.all(), 'serializer_class': statewise_testing_Serializer,'label': 'statewise',},
        {'queryset': covid_india.objects.all(), 'serializer_class': covid_india_Serializer,'label': 'inddia'}
        # {'queryset': Poem.objects.filter(style='Sonnet'), 'serializer_class': PoemSerializer},
    ]
    #serializer_class = statewise_testing_Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Date']





class get_state_info(ObjectMultipleModelAPIViewSet):
    permission_classes = [IsAuthenticated,]

    querylist = [
        {'queryset': statewise_testing.objects.all(), 'serializer_class': statewise_testing_Serializer,'label': 'statewise_testing',},
        {'queryset': covid_india.objects.all(), 'serializer_class': covid_india_Serializer,'label': 'covid_india'},
        {'queryset': covid_vaccine_statewise_mode.objects.all(), 'serializer_class': covid_vaccine_statewise_mode_Serializer, 'label': 'covid_vaccine_statewise'}
        # {'queryset': Poem.objects.filter(style='Sonnet'), 'serializer_class': PoemSerializer},
    ]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['State']



class Pinpoint_state_info(ObjectMultipleModelAPIViewSet):
    #permission_classes = [permissions.DjangoModelPermissions]
    permission_classes = [IsAuthenticated, ]
    querylist = [
        {'queryset': statewise_testing.objects.all(), 'serializer_class': statewise_testing_Serializer,'label': 'statewise_testing',},
        {'queryset': covid_india.objects.all(), 'serializer_class': covid_india_Serializer,'label': 'covid_india'},
        {'queryset': covid_vaccine_statewise_mode.objects.all(), 'serializer_class': covid_vaccine_statewise_mode_Serializer, 'label': 'covid_vaccine_statewise'}
        # {'queryset': Poem.objects.filter(style='Sonnet'), 'serializer_class': PoemSerializer},
    ]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['State','Date']


class get_date_info(ObjectMultipleModelAPIViewSet):
    #permission_classes = [permissions.DjangoModelPermissions]
    permission_classes = [IsAuthenticated, ]
    querylist = [
        {'queryset': statewise_testing.objects.all(), 'serializer_class': statewise_testing_Serializer,'label': 'statewise_testing',},
        {'queryset': covid_india.objects.all(), 'serializer_class': covid_india_Serializer,'label': 'covid_india'},
        {'queryset': covid_vaccine_statewise_mode.objects.all(), 'serializer_class': covid_vaccine_statewise_mode_Serializer, 'label': 'covid_vaccine_statewise'}
        # {'queryset': Poem.objects.filter(style='Sonnet'), 'serializer_class': PoemSerializer},
    ]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Date']

# class EventFilter(filters.OrderingFilter):
#     timestamp_gte = django_filters.DateTimeFilter(name="Date")
#     class Meta:
#         model = statewise_testing
#         fields = ['Date', 'State','TotalSamples','Positive','Negative']
#
# class statewise_date_View(viewsets.ReadOnlyModelViewSet):
#     """
#     A read only view that returns all audit events in JSON or CSV.
#     """
#     #filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
#     filter_backends = [DjangoFilterBackend]
#     queryset = statewise_testing.objects.all()
#     serializer_class = statewise_testing_Serializer
#     filter_class = EventFilter