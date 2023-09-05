# from django.conf.urls import url
from django.urls import path, re_path
from . import views
app_name = 'client'


urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^logout/$',views.user_logout, name='logout'),
    re_path(r'^profile/(?P<pk>\d+)/$', views.ProfileDetailView.as_view(), name='profile'),


#url(r'^profile/(?P<pk>\d+)/edit/$', views.profile_update, name='edit_profile'),
]
