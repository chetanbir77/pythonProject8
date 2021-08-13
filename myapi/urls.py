from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
#router = routers.SimpleRouter()
# router.register(r'state_date', views.statewise_testing_viewset)
# router.register(r'state_date_multiple', views.statewise_testing_viewset_multiple, basename='texts')
router.register(r'get_state_info', views.get_state_info, basename='texts2')
router.register(r'pinpoint_state_info', views.Pinpoint_state_info, basename='texts3')
router.register(r'get_date_info', views.get_date_info, basename='texts4')
#router.register(r'date_22', views.statewise_date_View)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('pinpoint_state_info/', views.Pinpoint_state_info, name='texts3'),
    path('get_state_info/', views.get_state_info, name='texts4'),
    path('get_date_info/',views.get_date_info, name='texts5'),

    #path('state_date_multiple/', views.statewise_testing_viewset_multiple.as_view(), name="instances")
]