from django.conf.urls import url
from django.urls import path
from app import views


app_name = 'app'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),
    url(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name='detail')
    ]
