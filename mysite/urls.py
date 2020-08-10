"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bookmark.views import BookmarkLV, BookmarkDV

from mysite.views import Homeview, UserCreateView, UserCreateDoneTV

# from bookmark.views import index,detail

urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),

    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),


    path('tinymce/',include('tinymce.urls')),
    # class-based views
    # path('bookmark/',BookmarkLV.as_view(),name='index'),
    # path('bookmark/<int:pk>',BookmarkDV.as_view(),name='detail'),
    # (URL pattern,
    # <int:pk> <- path variable 경로변수

    # path('bookmark/',index,name='index'),
    # path('bookmark/<int:pk>',detail,name='detail')

]
