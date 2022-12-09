from django.urls import path
from Test1 import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns =[
    path('', views.homepage),
    path('diseasetype/', views.DiseaseTypeList.as_view()),
    path('diseasetype/<int:pk>/', views.DiseaseTypeDetail.as_view()),

    path('country/', views.CountryListApi.as_view()),
    path('country/<pk>/', views.CountryDetailApi.as_view()),

    path('disease/', views.DiseaseList.as_view()),
    path('disease/<pk>/', views.DiseaseDetail.as_view()),

    path('discover/', views.DiscoverList.as_view()),
    path('discover/<pk>/', views.DiscoverDetailApi.as_view()),
    
    path('doctor/', views.DoctorList.as_view()),
    path('doctor/<pk>/', views.DoctorDetailApi.as_view()),

    path('users/', views.UsersList.as_view()),
    path('users/<int:pk>/', views.UsersDetail.as_view()),

    path('publicservant/', views.PublicServantList.as_view()),
    path('publicservant/<pk>/', views.PublicServantDetailApi.as_view()),
    
    path('specialize/', views.SpecializeList.as_view()),
    path('specialize/<int:pk>/', views.SpecializeDetail.as_view()),

    path('record/', views.RecordList.as_view()),
    path('record/<pk>/', views.RecordDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)