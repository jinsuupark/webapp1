from django.urls import path
from bookmark.views import *

app_name = 'bookmark' #해당 어플리케이션의 네임스페이스명
urlpatterns = [


    # class-based views
    path('',BookmarkLV.as_view(),name='index'),
    path('<int:pk>',BookmarkDV.as_view(),name='detail'),
    # (URL pattern,
    # <int:pk> <- path variable 경로변수

    # Example: /bookmark/add
    path('add/',BookmarkCV.as_view(),name='add'),
    # Example: /bookmark/add
    path('change/',BookmarkChangeLV.as_view(),name='change'),
    # Example: /bookmark/add
    path('<int:pk>/update',BookmarkUV.as_view(),name='update'),
    # Example: /bookmark/add
    path('<int:pk>/delete',BookmarkDV.as_view(),name='delete'),



]