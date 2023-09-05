from django.urls import path, re_path
# from django.conf.urls import url
from knapsack_solution import views


#app_name = 'make_predictions'

app_name = 'knapsack'
urlpatterns = [

    re_path(r'^(?P<pk>\d+)$', views.PredictRisk, name='knapsack')
]
